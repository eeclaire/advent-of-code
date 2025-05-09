import csv
from typing import Generator


def read_reports(input_path) -> Generator[list[int], None, None]:
    with open(input_path, 'r') as f:
        reader = csv.reader(f, delimiter=" ")
        for report in reader:
            yield [int(level) for level in report]


def check_increase(left: int, right: int) -> bool:
    if right <= left or right - left > 3:
        return False

    return True


def check_safe_levels(report: list[int]) -> bool:
    if report[0] < report[1]:
        for i in range(1, len(report)):
            if not check_increase(report[i - 1], report[i]):
                return False
    elif report[0] > report[1]:
        for i in range(1, len(report)):
            if not check_increase(report[i], report[i - 1]):
                return False
    else:
        return False

    return True


def count_safe_reports(reports: list[list[int]]) -> int:
    safe_reports = 0
    for report in reports:
        if check_safe_levels(report):
            safe_reports += 1

    return safe_rep
def day_two():
    reports = list(read_reports('./inputs/2024-12-02.csv'))
    safe_reports = count_safe_reports(reports)
    print(f"safe reports: {safe_reports}")


if __name__ == "__main__":
    day_two()
