"""Tests for application functions."""

import json
from datetime import datetime
from os import remove
from pathlib import Path

import pytest

from log_analyzer import config
from src.app.log_analyzer import make_report, create_report_file, update_config, main
from tests.testdata import make_report_data, create_report_file_data, main_data


@pytest.mark.parametrize("file_name, logs, expected_output", make_report_data())
def test_make_report(file_name: str, logs: str, expected_output: list):
    full_path = f"./logs/{file_name}"
    with open(full_path, "w", encoding="utf-8") as file:
        file.write(logs)

    result = make_report(config, file_name)
    remove(full_path)

    assert result == expected_output


@pytest.mark.parametrize("file_date, reporting_data", create_report_file_data())
def test_create_report_file(file_date: str, reporting_data: list):
    create_report_file(config, file_date, reporting_data)
    full_path = f"./reports/report-{file_date}.html"

    assert Path(full_path).exists()

    remove(full_path)


def test_update_config():
    tmp_config = config.copy()
    full_path = "./test_config.json"
    test_config = {
        "REPORT_SIZE": 33,
        "REPORT_DIR": "spam",
        "LOG_DIR": "eggs",
        "SELF_LOG_DIR": "foo",
        "TEMPLATES_DIR": "python_is_cool",
        "ERROR_THRESHOLD": 0.878787,
    }
    with open(full_path, "w", encoding="utf-8") as file:
        json.dump(test_config, file)

    update_config(config, full_path)

    assert config == test_config

    config.update(tmp_config)
    remove(full_path)


@pytest.mark.parametrize("file_date, logs, expected_data, expected_log", main_data())
def test_main(file_date: str, logs: str, expected_data: str, expected_log: dict):
    config.update({"REPORT_SIZE": 5})
    log_full_path = f"./{config["LOG_DIR"]}/nginx-access-ui.log-{file_date}"
    report_file_date = datetime.strptime(str(file_date), "%Y%m%d").date().strftime("%Y.%m.%d")
    report_full_path = f"./{config["REPORT_DIR"]}/report-{report_file_date}.html"
    with open(log_full_path, "w", encoding="utf-8") as file:
        file.write(logs)

    main(config)

    with open(report_full_path, "r", encoding="utf-8") as rep_file:
        report_data = rep_file.read()
        print(type(report_data))
    with open(f"./{config["LOG_DIR"]}/self_log.json", "r", encoding="utf-8") as log_file:
        log_data = json.loads(log_file.readlines()[-1])

    assert expected_data in report_data
    assert expected_log.get("level") == log_data.get("level")
    assert expected_log.get("message") == log_data.get("message")

    remove(log_full_path)
    remove(report_full_path)
