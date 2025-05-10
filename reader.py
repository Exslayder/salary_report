import logging
from typing import List, Dict
from models import Employee

class CSVParseError(Exception):
    pass

def read_lines(filepath: str) -> List[str]:
    """Чтение строк из CSV-файла, без пустых строк"""
    with open(filepath, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def parse_headers(header_line: str) -> Dict[str, int]:
    """Парсинг заголовков"""
    headers = [h.strip() for h in header_line.split(',')]
    return {name: idx for idx, name in enumerate(headers)}

def read_csv(filepath: str) -> List[Employee]:
    """Парсинг CSV-файла в список объектов Employee"""
    lines = read_lines(filepath)
    if not lines:
        raise CSVParseError(f"No data in '{filepath}'")

    header_map = parse_headers(lines[0])
    required = ['name', 'department', 'hours_worked']
    for col in required:
        if col not in header_map:
            raise CSVParseError(f"Missing required column '{col}' in '{filepath}'")

    rate_keys = ['hourly_rate', 'rate', 'salary']
    rate_col = next((k for k in rate_keys if k in header_map), None)
    if not rate_col:
        raise CSVParseError(f"Missing any of {rate_keys} in '{filepath}'")

    employees: List[Employee] = []
    for lineno, line in enumerate(lines[1:], start=2):
        parts = [p.strip() for p in line.split(',')]
        if len(parts) != len(header_map):
            logging.warning("Skipping line %d in '%s': wrong column count", lineno, filepath)
            continue
        try:
            emp = Employee(
                name=parts[header_map['name']],
                department=parts[header_map['department']],
                hours_worked=int(parts[header_map['hours_worked']]),
                hourly_rate=int(parts[header_map[rate_col]]),
            )
            employees.append(emp)
        except ValueError as e:
            logging.warning("Skipping line %d in '%s': %s", lineno, filepath, e)
    return employees
