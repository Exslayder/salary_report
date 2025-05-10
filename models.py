from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    department: str
    hours_worked: int
    hourly_rate: int

    @property
    def payout(self) -> int:
        return self.hours_worked * self.hourly_rate
