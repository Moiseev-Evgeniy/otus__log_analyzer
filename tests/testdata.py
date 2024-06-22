"""Test data for tests."""

from collections import namedtuple


def make_report_data() -> list:
    """Test data for test_make_report."""

    TestData = namedtuple("TestData", ["file_name", "logs", "expected_output"])

    return [
        TestData(
            file_name="test_log_1",
            logs="""1.196.116.32 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/25019354 HTTP/1.1" 200 927 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-2190034393-4708-9752759" "dc7161be3" 0.390
                1.99.174.176 3b81f63526fa8  - [29/Jun/2017:03:50:22 +0300] "GET /api/1/photogenic_banners/list/?server_name=WIN7RB4 HTTP/1.1" 200 12 "-" "Python-urllib/2.7" "-" "1498697422-32900793-4708-9752770" "-" 0.133
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 0.704
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/16852664 HTTP/1.1" 200 19415 "-" "Slotovod" "-" "1498697422-2118016444-4708-9752769" "712e90144abee9" 0.199
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 0.704
                1.168.65.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/internal/banner/24294027/info HTTP/1.1" 200 407 "-" "-" "-" "1498697422-2539198130-4709-9928846" "89f7f1be37d" 0.146
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 1.704
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/group/1769230/banners HTTP/1.1" 200 1020 "-" "Configovod" "-" "1498697422-2118016444-4708-9752747" "712e90144abee9" 0.628
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 3.704
                1.194.135.240 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/group/7786679/statistic/sites/?date_type=day&date_from=2017-06-28&date_to=2017-06-28 HTTP/1.1" 200 22 "-" "python-requests/2.13.0" "-" "1498697422-3979856266-4708-9752772" "8a7741a54297568b" 0.067
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/1717161 HTTP/1.1" 200 2116 "-" "Slotovod" "-" "1498697422-2118016444-4708-9752771" "712e90144abee9" 0.138
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 0.704
                1.166.85.48 -  - [29/Jun/2017:03:50:22 +0300] "GET /export/appinstall_raw/2017-06-29/ HTTP/1.0" 200 28358 "-" "Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)" "-" "-" "-" 0.003
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4822/groups HTTP/1.1" 200 22 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752773" "2a828197ae235b0b3cb" 0.157""",
            expected_output=[{'url': '/api/v2/slot/4705/groups', 'count': 5, 'count_perc': 35.714, 'time_sum': 7.52, 'time_perc': 80.162, 'time_avg': 1.504, 'time_max': 3.704, 'time_med': 0.704}, {'url': '/api/v2/group/1769230/banners', 'count': 1, 'count_perc': 7.143, 'time_sum': 0.628, 'time_perc': 6.694, 'time_avg': 0.628, 'time_max': 0.628, 'time_med': 0.628}, {'url': '/api/v2/banner/25019354', 'count': 1, 'count_perc': 7.143, 'time_sum': 0.39, 'time_perc': 4.157, 'time_avg': 0.39, 'time_max': 0.39, 'time_med': 0.39}, {'url': '/api/v2/banner/16852664', 'count': 1, 'count_perc': 7.143, 'time_sum': 0.199, 'time_perc': 2.121, 'time_avg': 0.199, 'time_max': 0.199, 'time_med': 0.199}, {'url': '/api/v2/slot/4822/groups', 'count': 1, 'count_perc': 7.143, 'time_sum': 0.157, 'time_perc': 1.674, 'time_avg': 0.157, 'time_max': 0.157, 'time_med': 0.157}, {'url': '/api/v2/internal/banner/24294027/info', 'count': 1, 'count_perc': 7.143, 'time_sum': 0.146, 'time_perc': 1.556, 'time_avg': 0.146, 'time_max': 0.146, 'time_med': 0.146}, {'url': '/api/v2/banner/1717161', 'count': 1, 'count_perc': 7.143, 'time_sum': 0.138, 'time_perc': 1.471, 'time_avg': 0.138, 'time_max': 0.138, 'time_med': 0.138}, {'url': '/api/1/photogenic_banners/list/?server_name=WIN7RB4', 'count': 1, 'count_perc': 7.143, 'time_sum': 0.133, 'time_perc': 1.418, 'time_avg': 0.133, 'time_max': 0.133, 'time_med': 0.133}, {'url': '/api/v2/group/7786679/statistic/sites/?date_type=day&date_from=2017-06-28&date_to=2017-06-28', 'count': 1, 'count_perc': 7.143, 'time_sum': 0.067, 'time_perc': 0.714, 'time_avg': 0.067, 'time_max': 0.067, 'time_med': 0.067}, {'url': '/export/appinstall_raw/2017-06-29/', 'count': 1, 'count_perc': 7.143, 'time_sum': 0.003, 'time_perc': 0.032, 'time_avg': 0.003, 'time_max': 0.003, 'time_med': 0.003}],
        ),
        TestData(
            file_name="test_log_2",
            logs="""1.196.116.32 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/25019354 HTTP/1.1" 200 927 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-2190034393-4708-9752759" "dc7161be3" 0.390
                1.99.174.176 3b81f63526fa8  - [29/Jun/2017:03:50:22 +0300] "GET /api/1/photogenic_banners/list/?server_name=WIN7RB4 HTTP/1.1" 200 12 "-" "Python-urllib/2.7" "-" "1498697422-32900793-4708-9752770" "-" 0.133
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 0.704
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/16852664 HTTP/1.1" 200 19415 "-" "Slotovod" "-" "1498697422-2118016444-4708-9752769" "712e90144abee9" 1.199
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/16852664 HTTP/1.1" 200 19415 "-" "Slotovod" "-" "1498697422-2118016444-4708-9752769" "712e90144abee9" 0.199
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 0.704
                1.168.65.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/internal/banner/24294027/info HTTP/1.1" 200 407 "-" "-" "-" "1498697422-2539198130-4709-9928846" "89f7f1be37d" 0.146
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/16852664 HTTP/1.1" 200 19415 "-" "Slotovod" "-" "1498697422-2118016444-4708-9752769" "712e90144abee9" 1.199
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 1.704
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/group/1769230/banners HTTP/1.1" 200 1020 "-" "Configovod" "-" "1498697422-2118016444-4708-9752747" "712e90144abee9" 0.628
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 3.704
                1.194.135.240 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/group/7786679/statistic/sites/?date_type=day&date_from=2017-06-28&date_to=2017-06-28 HTTP/1.1" 200 22 "-" "python-requests/2.13.0" "-" "1498697422-3979856266-4708-9752772" "8a7741a54297568b" 0.067
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/16852664 HTTP/1.1" 200 19415 "-" "Slotovod" "-" "1498697422-2118016444-4708-9752769" "712e90144abee9" 0.899
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/1717161 HTTP/1.1" 200 2116 "-" "Slotovod" "-" "1498697422-2118016444-4708-9752771" "712e90144abee9" 0.138
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4705/groups HTTP/1.1" 200 2613 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752745" "2a828197ae235b0b3cb" 0.704
                1.166.85.48 -  - [29/Jun/2017:03:50:22 +0300] "GET /export/appinstall_raw/2017-06-29/ HTTP/1.0" 200 28358 "-" "Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)" "-" "-" "-" 0.003
                1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/16852664 HTTP/1.1" 200 19415 "-" "Slotovod" "-" "1498697422-2118016444-4708-9752769" "712e90144abee9" 0.199
                1.199.4.96 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/slot/4822/groups HTTP/1.1" 200 22 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-3800516057-4708-9752773" "2a828197ae235b0b3cb" 0.157""",
            expected_output=[{'url': '/api/v2/slot/4705/groups', 'count': 5, 'count_perc': 27.778, 'time_sum': 7.52, 'time_perc': 58.399, 'time_avg': 1.504, 'time_max': 3.704, 'time_med': 0.704}, {'url': '/api/v2/banner/16852664', 'count': 5, 'count_perc': 27.778, 'time_sum': 3.695, 'time_perc': 28.695, 'time_avg': 0.739, 'time_max': 1.199, 'time_med': 0.899}, {'url': '/api/v2/group/1769230/banners', 'count': 1, 'count_perc': 5.556, 'time_sum': 0.628, 'time_perc': 4.877, 'time_avg': 0.628, 'time_max': 0.628, 'time_med': 0.628}, {'url': '/api/v2/banner/25019354', 'count': 1, 'count_perc': 5.556, 'time_sum': 0.39, 'time_perc': 3.029, 'time_avg': 0.39, 'time_max': 0.39, 'time_med': 0.39}, {'url': '/api/v2/slot/4822/groups', 'count': 1, 'count_perc': 5.556, 'time_sum': 0.157, 'time_perc': 1.219, 'time_avg': 0.157, 'time_max': 0.157, 'time_med': 0.157}, {'url': '/api/v2/internal/banner/24294027/info', 'count': 1, 'count_perc': 5.556, 'time_sum': 0.146, 'time_perc': 1.134, 'time_avg': 0.146, 'time_max': 0.146, 'time_med': 0.146}, {'url': '/api/v2/banner/1717161', 'count': 1, 'count_perc': 5.556, 'time_sum': 0.138, 'time_perc': 1.072, 'time_avg': 0.138, 'time_max': 0.138, 'time_med': 0.138}, {'url': '/api/1/photogenic_banners/list/?server_name=WIN7RB4', 'count': 1, 'count_perc': 5.556, 'time_sum': 0.133, 'time_perc': 1.033, 'time_avg': 0.133, 'time_max': 0.133, 'time_med': 0.133}, {'url': '/api/v2/group/7786679/statistic/sites/?date_type=day&date_from=2017-06-28&date_to=2017-06-28', 'count': 1, 'count_perc': 5.556, 'time_sum': 0.067, 'time_perc': 0.52, 'time_avg': 0.067, 'time_max': 0.067, 'time_med': 0.067}, {'url': '/export/appinstall_raw/2017-06-29/', 'count': 1, 'count_perc': 5.556, 'time_sum': 0.003, 'time_perc': 0.023, 'time_avg': 0.003, 'time_max': 0.003, 'time_med': 0.003}],
        ),
    ]


def create_report_file_data() -> list:
    """Test data for test_create_report_file."""

    TestData = namedtuple("TestData", ["file_date", "reporting_data"])

    return [
        TestData(
            file_date="00000000",
            reporting_data=[{'url': '/api/v2/slot/4705/groups', 'count': 5, 'count_perc': 27.778, 'time_sum': 7.52,
                             'time_perc': 58.399, 'time_avg': 1.504, 'time_max': 3.704, 'time_med': 0.704}],
        ),
        TestData(
            file_date="11111111",
            reporting_data=[{'url': '/api/v2/banner/16852664', 'count': 5, 'count_perc': 27.778, 'time_sum': 3.695,
                             'time_perc': 28.695, 'time_avg': 0.739, 'time_max': 1.199, 'time_med': 0.899}],
        ),
    ]


def main_data() -> list:
    """Test data for test_main."""

    TestData = namedtuple("TestData", ["file_date", "logs", "expected_data", "expected_log"])

    return [
        TestData(
            file_date=99991231,
            logs="""1.200.76.128 f032b48fb33e1e692  - [29/Jun/2017:03:50:24 +0300] "GET /api/1/banners/?campaign=7789714 HTTP/1.1" 200 12 "-" "-" "-" "1498697424-4102637017-4708-9752804" "-" 0.151
                1.194.135.240 -  - [29/Jun/2017:03:50:24 +0300] "GET /api/v2/group/7820982/statistic/sites/?date_type=day&date_from=2017-06-28&date_to=2017-06-28 HTTP/1.1" 200 22 "-" "python-requests/2.13.0" "-" "1498697424-3979856266-4708-9752826" "8a7741a54297568b" 0.065
                1.196.116.32 -  - [29/Jun/2017:03:50:24 +0300] "GET /api/v2/banner/26613316 HTTP/1.1" 200 1283 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752818" "dc7161be3" 0.189
                1.196.116.32 -  - [29/Jun/2017:03:50:25 +0300] "GET /api/v2/banner/26604444 HTTP/1.1" 200 1379 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752817" "dc7161be3" 3.370
                1.196.116.32 -  - [29/Jun/2017:03:50:25 +0300] "GET /api/v2/banner/26629313 HTTP/1.1" 200 890 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752809" "dc7161be3" 0.407
                1.196.116.32 -  - [29/Jun/2017:03:50:24 +0300] "GET /api/v2/banner/797816 HTTP/1.1" 200 1192 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752815" "dc7161be3" 0.208
                1.200.76.128 f032b48fb33e1e692  - [29/Jun/2017:03:50:24 +0300] "GET /api/1/campaigns/?id=7789717 HTTP/1.1" 200 608 "-" "-" "-" "1498697424-4102637017-4708-9752827" "-" 0.145
                1.141.86.192 -  - [29/Jun/2017:03:50:24 +0300] "GET /export/appinstall_raw/2017-06-29/ HTTP/1.0" 200 28358 "-" "Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)" "-" "-" "-" 0.002
                1.196.116.32 -  - [29/Jun/2017:03:50:25 +0300] "GET /api/v2/banner/26629313 HTTP/1.1" 200 890 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752809" "dc7161be3" 1.407
                1.196.116.32 -  - [29/Jun/2017:03:50:25 +0300] "GET /api/v2/banner/26604444 HTTP/1.1" 200 1379 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752817" "dc7161be3"1.370
                1.141.86.192 -  - [29/Jun/2017:03:50:25 +0300] "GET /export/appinstall_raw/2017-06-30/ HTTP/1.0" 404 162 "-" "Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)" "-" "-" "-" 0.001
                1.196.116.32 -  - [29/Jun/2017:03:50:25 +0300] "GET /api/v2/banner/26740463 HTTP/1.1" 200 849 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752813" "dc7161be3" 0.273
                1.196.116.32 -  - [29/Jun/2017:03:50:25 +0300] "GET /api/v2/banner/25048498 HTTP/1.1" 200 1045 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752807" "dc7161be3" 0.360
                1.196.116.32 -  - [29/Jun/2017:03:50:25 +0300] "GET /api/v2/banner/26604444 HTTP/1.1" 200 1379 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752817" "dc7161be3" 0.370
                1.196.116.32 -  - [29/Jun/2017:03:50:25 +0300] "GET /api/v2/banner/26604444 HTTP/1.1" 200 1379 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752817" "dc7161be3" 2.370
                1.170.209.160 -  - [29/Jun/2017:03:50:25 +0300] "GET /export/appinstall_raw/2017-06-29/ HTTP/1.0" 200 28358 "-" "Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)" "-" "-" "-" 0.002
                1.170.209.160 -  - [29/Jun/2017:03:50:25 +0300] "GET /export/appinstall_raw/2017-06-30/ HTTP/1.0" 404 162 "-" "Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)" "-" "-" "-" 0.001
                1.200.76.128 f032b48fb33e1e692  - [29/Jun/2017:03:50:25 +0300] "GET /api/1/banners/?campaign=7789717 HTTP/1.1" 200 12 "-" "-" "-" "1498697424-4102637017-4708-9752828" "-" 0.151
                1.196.116.32 -  - [29/Jun/2017:03:50:25 +0300] "GET /api/v2/banner/26629313 HTTP/1.1" 200 890 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697424-2190034393-4708-9752809" "dc7161be3" 0.407""",
            expected_data='[{"url": "/api/v2/banner/26604444", "count": 3, "count_perc": 15.789, "time_sum": 6.11, "time_perc": 61.848, "time_avg": 2.037, "time_max": 3.37, "time_med": 2.37}, {"url": "/api/v2/banner/26629313", "count": 3, "count_perc": 15.789, "time_sum": 2.221, "time_perc": 22.482, "time_avg": 0.74, "time_max": 1.407, "time_med": 0.407}, {"url": "/api/v2/banner/25048498", "count": 1, "count_perc": 5.263, "time_sum": 0.36, "time_perc": 3.644, "time_avg": 0.36, "time_max": 0.36, "time_med": 0.36}, {"url": "/api/v2/banner/26740463", "count": 1, "count_perc": 5.263, "time_sum": 0.273, "time_perc": 2.763, "time_avg": 0.273, "time_max": 0.273, "time_med": 0.273}, {"url": "/api/v2/banner/797816", "count": 1, "count_perc": 5.263, "time_sum": 0.208, "time_perc": 2.105, "time_avg": 0.208, "time_max": 0.208, "time_med": 0.208}]',
            expected_log={"level": "info", "message": "The report has been generated"},
        ),
    ]
