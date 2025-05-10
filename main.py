import sys
import argparse
import logging
from reader import read_csv, CSVParseError
from reports import REPORTS

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Payroll Report Generator")
    parser.add_argument("files", nargs="+", help="Paths to CSV employee data files")
    parser.add_argument("--report", required=True, help="Type of report to generate")
    args = parser.parse_args()

    if args.report not in REPORTS:
        logging.error("Unsupported report '%s'. Available: %s", args.report, ', '.join(REPORTS))
        sys.exit(1)

    all_employees = []
    for filepath in args.files:
        try:
            logging.info("Reading file %s", filepath)
            all_employees.extend(read_csv(filepath))
        except CSVParseError as e:
            logging.error("Failed to parse %s: %s", filepath, e)
            sys.exit(1)
        except FileNotFoundError:
            logging.error("File not found: %s", filepath)
            sys.exit(1)

    report_func = REPORTS[args.report]
    output = report_func(all_employees)
    print(output)

if __name__ == "__main__":
    main()
