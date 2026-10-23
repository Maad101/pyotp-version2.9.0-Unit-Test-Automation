import datetime
import pytest
import pyotp

def test_vcrrt():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    now = datetime.datetime(2026, 10, 23, 12, 0, 0)
    code = totp.at(now)
    assert totp.verify(code, for_time=now) == True

def test_vwrg():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    now = datetime.datetime(2026, 10, 23, 12, 0, 0)
    assert totp.verify("000000", for_time=now) == False

def test_vOldWindow0():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    now = datetime.datetime(2026, 10, 23, 12, 0, 0)
    old = totp.at(now - datetime.timedelta(seconds=30))
    assert totp.verify(old, for_time=now, valid_window=0) == False



def test_vNegWindow():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    now = datetime.datetime(2026, 10, 23, 12, 0, 0)
    code = totp.at(now)
    with pytest.raises(ValueError):
        totp.verify(code, for_time=now, valid_window=-1)

def test_vIntrvlzero():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", interval=0)
    with pytest.raises(ValueError):
        totp.verify("123456")