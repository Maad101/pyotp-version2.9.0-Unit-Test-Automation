import pytest
import pyotp

def test_putotp():
    otp = pyotp.parse_uri("otpauth://totp/alice?secret=JBSWY3DPEHPK3PXP")
    assert isinstance(otp, pyotp.TOTP)

def test_puhotp():
    otp = pyotp.parse_uri("otpauth://hotp/alice?secret=JBSWY3DPEHPK3PXP&counter=5")
    assert isinstance(otp, pyotp.HOTP)
    assert otp.initial_count == 5

def test_punosecret():
    with pytest.raises(ValueError):
        pyotp.parse_uri("otpauth://totp/alice?digits=6")

def test_pubadscheme():
    with pytest.raises(ValueError):
        pyotp.parse_uri("http://totp/alice?secret=JBSWY3DPEHPK3PXP")

def test_pudigits8():
    otp = pyotp.parse_uri("otpauth://totp/alice?secret=JBSWY3DPEHPK3PXP&digits=8")
    assert otp.digits == 8

def test_pucolon():
    otp = pyotp.parse_uri("otpauth://totp/Ac%3Ame:bob?secret=JBSWY3DPEHPK3PXP")
    assert otp.issuer == "Ac:me"

def test_pudigits10():
    otp = pyotp.parse_uri("otpauth://totp/alice?secret=JBSWY3DPEHPK3PXP&digits=10")
    assert otp.digits == 10
