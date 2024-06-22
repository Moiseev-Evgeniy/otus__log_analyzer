# log_format ui_short '$remote_addr  $remote_user $http_x_real_ip [$time_local] "$request" '
#                     '$status $body_bytes_sent "$http_referer" '
#                     '"$http_user_agent" "$http_x_forwarded_for" "$http_X_REQUEST_ID" "$http_X_RB_USER" '
#                     '$request_time';


import gzip
import json
import re
from datetime import datetime
from os import listdir
from pathlib import Path
from statistics import median
from string import Template

from structlog import getLogger

log = getLogger()

ROOT_DIR = Path(__file__).parent.parent.parent
log_file_name_prefix = "nginx-access-ui.log-"
self_log_file_name = "self_log.json"


def event_logging(config: dict, message: str, level: str, data: dict) -> None:
    """Event logging function."""

    if config["SELF_LOG_DIR"]:
        write_log_to_file(config, message, level, data)
    else:
        getattr(log, level)(message, **data)


def write_log_to_file(config: dict, message: str, level: str, data: dict) -> None:
    """The function of writing logs to a file."""

    with open(ROOT_DIR / config["SELF_LOG_DIR"] / self_log_file_name, "a", encoding="utf-8") as log_file:
        info = {"datetime": datetime.now().ctime(), "level": level, "message": message}
        if data:
            info["data"] = data
        json.dump(info, log_file)
        log_file.write("\n")


def update_config(config: dict, external_config_path: str) -> None:
    """The function of updating the configuration from an external file."""

    external_config_path = ROOT_DIR / external_config_path

    if not external_config_path.exists() or not external_config_path.is_file():
        raise FileNotFoundError("Config file not found.")

    with open(external_config_path, "r", encoding="utf-8") as conf_file:
        try:
            config.update(json.load(conf_file))
        except json.decoder.JSONDecodeError:
            pass


def make_report(config: dict, file_name: str) -> list[dict] | None:
    """The function of parsing, calculating and creating reporting data."""

    open_func, mode = (gzip.open, "rt") if file_name.endswith(".gz") else (open, "r")
    rows_gen = (row for row in open_func(ROOT_DIR / config["LOG_DIR"] / file_name, mode, encoding="utf-8"))

    parsing_result = {}
    total_count = 0
    total_time_sum = 0
    errors_count = 0

    for row in rows_gen:
        total_count += 1
        row = row.split()

        try:
            url = row[6]
            request_time = float(row[-1])
        except (IndexError, ValueError):
            errors_count += 1
            continue

        total_time_sum += request_time

        if parsing_result.get(url):
            parsing_result[url]["count"] += 1
            parsing_result[url]["time_list"].append(request_time)
            parsing_result[url]["time_sum"] += request_time
        else:
            parsing_result[url] = {"count": 1, "time_list": [request_time], "time_sum": request_time}

    if errors_count / total_count >= config["ERROR_THRESHOLD"]:
        event_logging(
            config,
            "The number of errors is higher than the acceptable level when parsing the log file",
            "debug",
            {"file_name": file_name},
        )
        return

    parsing_result = sorted(parsing_result.items(), key=lambda x: x[1]["time_sum"], reverse=True)
    parsing_result = parsing_result[:config["REPORT_SIZE"]]

    result = []
    digits_num = 3

    for url, params in parsing_result:
        count = params["count"]
        time_list = params["time_list"]
        time_sum = params["time_sum"]

        result.append(
            {
                "url": url,
                "count": count,
                "count_perc": round((count / total_count) * 100, digits_num),
                "time_sum": round(time_sum, digits_num),
                "time_perc": round((time_sum / total_time_sum) * 100, digits_num),
                "time_avg": round((time_sum / count), digits_num),
                "time_max": round(max(time_list), digits_num),
                "time_med": round(median(time_list), digits_num),
            }
        )

    return result


def create_report_file(config: dict, file_date: str, reporting_data: list[dict]) -> None:
    """A function for creating a report file."""

    with (
        open(ROOT_DIR / config["TEMPLATES_DIR"] / "report.html", "r", encoding="utf-8") as temp_file,
        open(ROOT_DIR / config["REPORT_DIR"] / f"report-{file_date}.html", "w", encoding="utf-8") as rep_file,
    ):
        template = Template(temp_file.read())
        rep_file.write(template.safe_substitute(table_json=json.dumps(reporting_data)))


def main(config: dict):
    file_names = [
        name for name in listdir(ROOT_DIR / config["LOG_DIR"])
        if re.match(rf"{log_file_name_prefix.replace(".", r"\.")}\d{{8}}(\.gz|$)$", name)
    ]
    if not file_names:
        event_logging(config, "There are no log files", "info", {"dir": str(ROOT_DIR / config["LOG_DIR"])})
        return

    file_name = max(file_names)
    date_str = file_name[len(log_file_name_prefix):len(log_file_name_prefix) + 8]
    file_date = datetime.strptime(date_str, "%Y%m%d").date().strftime("%Y.%m.%d")

    if f"report-{file_date}.html" in listdir(ROOT_DIR / config["REPORT_DIR"]):
        event_logging(
            config,
            "There is already a report for this log file",
            "info",
            {"log_file_name": file_name, "report_file_name": f"report-{file_date}.html"},
        )
        return

    if reporting_data := make_report(config, file_name):
        create_report_file(config, file_date, reporting_data)

    event_logging(config, "The report has been generated", "info", {})
