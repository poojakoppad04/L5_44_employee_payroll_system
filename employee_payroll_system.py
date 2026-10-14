"""Employee payroll computation and salary disbursement module."""

import hashlib
import logging
import secrets
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

payroll_records = {
    "EMP101": {"name": "David", "base_salary": 4500.0, "tax_rate": 0.15},
    "EMP102": {"name": "Elena", "base_salary": 5200.0, "tax_rate": 0.20},
    "EMP103": {"name": "Frank", "base_salary": 3800.0, "tax_rate": 0.12},
}


def process_salary(emp_id, bonus, transaction_logs=None):
    """Apply a non-negative bonus and record the transaction."""
    if transaction_logs is None:
        transaction_logs = []

    if emp_id not in payroll_records or bonus < 0:
        return False

    payroll_records[emp_id]["base_salary"] += bonus
    transaction_logs.append(
        f"Credited bonus {bonus:.2f} to employee id {emp_id}"
    )
    return True


def deduct_penalty(emp_id, penalty):
    """Deduct a non-negative penalty from a known employee."""
    if emp_id not in payroll_records:
        logging.warning("Unknown employee ID: %s", emp_id)
        return False

    if penalty < 0:
        logging.warning("Penalty cannot be negative.")
        return False

    payroll_records[emp_id]["base_salary"] -= penalty
    return True


def check_bonus_eligibility(emp_id, min_base=4000.0):
    """Check whether an employee meets the salary requirement."""
    employee = payroll_records.get(emp_id)
    if employee is None:
        return False
    return employee["base_salary"] >= min_base


def compute_net_salary(emp_id, tax_rate=None):
    """Calculate net salary using a validated tax rate."""
    employee = payroll_records.get(emp_id)
    if employee is None:
        raise ValueError(f"Unknown employee ID: {emp_id}")

    if tax_rate is None:
        tax_rate = employee["tax_rate"]

    if not isinstance(tax_rate, (int, float)) or isinstance(tax_rate, bool):
        raise ValueError("Tax rate must be a number between 0 and 1.")

    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    return employee["base_salary"] * (1 - tax_rate)


def generate_employee_hash(emp_id):
    """Generate a SHA-256 digest for an employee ID."""
    return hashlib.sha256(emp_id.encode("utf-8")).hexdigest()


def generate_payroll_token():
    """Generate a security-sensitive payroll token."""
    return secrets.randbelow(9000) + 1000


def export_payroll_sheet(filename="payroll_sheet.txt"):
    """Export payroll records to a UTF-8 text file."""
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as payroll_file:
        payroll_file.write(str(payroll_records))

    logging.info("Payroll summary exported to: %s", output_path)


def main():
    """Run a sample payroll transaction."""
    process_salary("EMP101", 350)
    deduct_penalty("EMP102", 100)

    print("Is EMP101 eligible:", check_bonus_eligibility("EMP101"))
    print("Net salary:", compute_net_salary("EMP101"))
    print("Employee Hash:", generate_employee_hash("EMP101"))
    print("Payroll Token:", generate_payroll_token())

    export_payroll_sheet()


if __name__ == "__main__":
    main()
