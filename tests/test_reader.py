import pytest
from reader import read_csv, CSVParseError
from models import Employee

RATE_CSV = """\
name,department,hours_worked,rate
Dave,Ops,20,15
"""

SALARY_CSV = """\
salary,department,name,hours_worked
25,Sales,Eve,10
"""

MALFORMED_CSV = """\
name,department,hours_worked,hourly_rate
Frank,Dev,5,10
BadLine,MissingColumns
Grace,QA,8,some_text
Heidi,QA,12,20
"""

EMPTY_CSV = """"""

def write_tmp(content, tmp_path, name="test.csv"):
    p = tmp_path / name
    p.write_text(content)
    return str(p)

def test_rate_column(tmp_path):
    path = write_tmp(RATE_CSV, tmp_path)
    emps = read_csv(path)
    assert emps == [Employee("Dave", "Ops", 20, 15)]

def test_salary_column(tmp_path):
    path = write_tmp(SALARY_CSV, tmp_path)
    emps = read_csv(path)
    # hours_worked=10, salary=25
    assert emps == [Employee("Eve", "Sales", 10, 25)]

def test_empty_file_raises(tmp_path):
    path = write_tmp(EMPTY_CSV, tmp_path, name="empty.csv")
    with pytest.raises(CSVParseError):
        read_csv(path)

def test_skip_malformed_and_nonint(tmp_path, caplog):
    path = write_tmp(MALFORMED_CSV, tmp_path, name="malformed.csv")
    caplog.set_level("WARNING")
    emps = read_csv(path)
    # Ожидаем, что успешные строки: Frank и Heidi
    assert Employee("Frank", "Dev", 5, 10) in emps
    assert Employee("Heidi", "QA", 12, 20) in emps
    # BadLine пропускается из-за wrong column count
    # Grace пропускается из-за non-int rate
    # Проверяем наличие предупреждений
    assert any("Skipping line" in rec.message for rec in caplog.records)
