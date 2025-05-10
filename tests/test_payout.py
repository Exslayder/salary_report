import re
from reports.payout import generate_payout_report
from models import Employee

def test_payout_report_format_strict():
    emps = [Employee('Alice', 'HR', 10, 50), Employee('Bob', 'HR', 20, 30)]
    rpt = generate_payout_report(emps)

    assert "name" in rpt
    assert "hours" in rpt
    assert "rate" in rpt
    assert "payout" in rpt

    pattern = r"^-{15}[A-Za-z ]{1,21}\s+\d+\s+\d+\s+\$\d+"
    lines = rpt.splitlines()
    data_lines = [line for line in lines if re.match(pattern, line)]
    assert len(data_lines) == 2

    assert re.search(r"\d+\s+\$\d+", rpt)

    assert "$500" in rpt
    assert "$600" in rpt

