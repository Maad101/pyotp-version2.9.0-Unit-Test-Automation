import pytest
import pyotp

def test_secretroundtrip():
    secret = pyotp.random_base32()
    uri = pyotp.utils.build_uri(secret, "alice")
    assert pyotp.parse_uri(uri).secret == secret

def test_comparecode():
    totp = pyotp.TOTP(pyotp.random_base32())
    code = totp.now()
    assert pyotp.utils.strings_equal(code, code) == True

def test_hexchars():
    secret = pyotp.random_hex()
    for ch in secret:
        assert ch in "ABCDEF0123456789"

def test_buildhotp():
    uri = pyotp.utils.build_uri("JBSWY3DPEHPK3PXP", "alice", initial_count=3)
    otp = pyotp.parse_uri(uri)
    assert otp.initial_count == 3

def test_buildissuer():
    uri = pyotp.utils.build_uri("JBSWY3DPEHPK3PXP", "alice", issuer="ACME")
    otp = pyotp.parse_uri(uri)
    assert otp.issuer == "ACME"

def test_periodneg():
    with pytest.raises(ValueError):
        pyotp.parse_uri("otpauth://totp/alice?secret=JBSWY3DPEHPK3PXP&period=-30")

def test_counterneg():
    with pytest.raises(ValueError):
        pyotp.parse_uri("otpauth://hotp/alice?secret=JBSWY3DPEHPK3PXP&counter=-1")
