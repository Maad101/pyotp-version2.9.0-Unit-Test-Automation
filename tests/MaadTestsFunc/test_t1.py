import hashlib
import pytest
import pyotp
pytestmark = [pytest.mark.hotp, pytest.mark.functions, pytest.mark.order(1)]

def test_count():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert hotp.at(0) == "755224"

def test_count1():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert hotp.at(1) == "287082"

def test_count2():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert hotp.at(2) == "359152"

def test_negcount():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    with pytest.raises(ValueError):
        hotp.at(-1)

def test_digitneg():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digits=-1)
    code = hotp.at(0)
    assert code.isdigit()

def test_md5digest():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digest=hashlib.md5)
    with pytest.raises(ValueError):
        hotp.at(0)
