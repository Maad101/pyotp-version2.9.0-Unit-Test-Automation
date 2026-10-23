import csv
import pytest
import pyotp
pytestmark = [pytest.mark.csvdata, pytest.mark.order(7)]

def read_csv(path):
    with open(path) as file:
        return list(csv.DictReader(file))

@pytest.mark.parametrize("row", read_csv("tests/CSVTests/test_data/hotp_data.csv"))
def test_hotpcsv(row):
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert hotp.at(int(row["counter"])) == row["expected"]

@pytest.mark.parametrize("row", read_csv("tests/CSVTests/test_data/digits_data.csv"))
def test_digitscsv(row):
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digits=int(row["digits"]))
    assert len(hotp.at(0)) == int(row["length"])
