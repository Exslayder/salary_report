from typing import Callable, List
from models import Employee
from .payout import generate_payout_report

REPORTS: dict[str, Callable[[List[Employee]], str]] = {
    'payout': generate_payout_report,
}
