from collections import defaultdict
from models import Employee

def generate_payout_report(employees: list[Employee]) -> str:
    grouped = defaultdict(list)
    for emp in employees:
        grouped[emp.department].append(emp)

    report_lines = []

    header = f"{'':<15}{'name':<20}{'hours':>9}{'rate':>6}{'payout':>8}"

    for dept, emps in sorted(grouped.items()):
        report_lines.append(header)
        report_lines.append(f"{dept}")
        total_payout = 0
        total_hours = 0
        for emp in emps:
            payout = emp.hours_worked * emp.hourly_rate
            total_payout += payout
            total_hours += emp.hours_worked
            report_lines.append(
                f"{'-'*15}{emp.name:<21}{emp.hours_worked:>6}{emp.hourly_rate:>6}{'$':>5}{payout:>2}"
            )
        report_lines.append(
            f"{'':<30}{total_hours:>12}{'$':>11}{total_payout:>2}"
        )
        report_lines.append("") 

    return "\n".join(report_lines)
