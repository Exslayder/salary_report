import sys
import pytest
from subprocess import Popen, PIPE
from pathlib import Path

MAIN = Path(__file__).parent.parent / 'main.py'
CSV = 'name,department,hours_worked,hourly_rate\nTom,HR,5,10\n'

def run(args):
    p = Popen([sys.executable, str(MAIN)] + args, stdout=PIPE, stderr=PIPE, text=True)
    return p.wait(), *p.communicate()


def test_run_success(tmp_path):
    f = tmp_path / 'f.csv'
    f.write_text(CSV)
    code, out, err = run([str(f), '--report', 'payout'])
    assert code == 0
    assert 'HR\n' in out

def test_unknown_report(tmp_path):
    f = tmp_path / 'f.csv'
    f.write_text(CSV)
    code, out, err = run([str(f), '--report', 'unknown'])
    assert code != 0
    assert 'Unsupported report' in err

def test_file_not_found():
    code, out, err = run(['nofile.csv', '--report', 'payout'])
    assert code != 0
    assert 'File not found' in err
