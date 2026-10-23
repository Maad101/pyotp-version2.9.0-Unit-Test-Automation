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
@pytest.mark.parametrize("row", read_csv("tests/CSVTests/test_data/uri_digits_data.csv"))
def test_uridigitscsv(row):
    otp = pyotp.parse_uri("otpauth://totp/alice?secret=JBSWY3DPEHPK3PXP&digits=" + row["digits"])
    assert otp.digits == int(row["digits"])

@pytest.mark.parametrize("row", read_csv("tests/CSVTests/test_data/secret_length_data.csv"))
def test_secretlencsv(row):
    secret = pyotp.random_base32(length=int(row["length"]))
    assert len(secret) == int(row["length"])
