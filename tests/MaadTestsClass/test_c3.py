import pytest
import pyotp
pytestmark = [pytest.mark.utils, pytest.mark.classes, pytest.mark.order(6)]

def test_secretworks():
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    assert len(totp.now()) == 6

def test_hexlen():
    secret = pyotp.random_hex()
    assert len(secret) == 40

def test_hexshort():
    with pytest.raises(ValueError):
        pyotp.random_hex(length=39)

def test_samestrings():
    assert pyotp.utils.strings_equal("123456", "123456") == True

def test_diffstrings():
    assert pyotp.utils.strings_equal("123456", "654321") == False

def test_uriback():
    uri = pyotp.utils.build_uri("JBSWY3DPEHPK3PXP", "alice")
    otp = pyotp.parse_uri(uri)
    assert otp.secret == "JBSWY3DPEHPK3PXP"

def test_hexemptychars():
    with pytest.raises(ValueError):
        pyotp.random_hex(chars="")

def test_uriperiodzero():
    with pytest.raises(ValueError):
        pyotp.parse_uri("otpauth://totp/alice?secret=JBSWY3DPEHPK3PXP&period=0")
