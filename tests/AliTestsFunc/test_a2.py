import datetime
import pytest
import pyotp

def test_tcsame():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    start = datetime.datetime(2026, 10, 23, 12, 0, 0)
    end = datetime.datetime(2026, 10, 23, 12, 0, 29)
    assert totp.timecode(start) == totp.timecode(end)

def test_tcnext():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    start = datetime.datetime(2026, 10, 23, 12, 0, 0)
    nxt = datetime.datetime(2026, 10, 23, 12, 0, 30)
    assert totp.timecode(nxt) == totp.timecode(start) + 1

def test_tcprev():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    start = datetime.datetime(2026, 10, 23, 12, 0, 0)
    prev = datetime.datetime(2026, 10, 23, 11, 59, 59)
    assert totp.timecode(prev) == totp.timecode(start) - 1

def test_tcinterval60():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", interval=60)
    start = datetime.datetime(2026, 10, 23, 12, 0, 0)
    end = datetime.datetime(2026, 10, 23, 12, 0, 59)
    assert totp.timecode(start) == totp.timecode(end)

def test_tcutc():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    t = datetime.datetime(1970, 1, 1, 0, 0, 59, tzinfo=datetime.timezone.utc)
    assert totp.timecode(t) == 1

def test_tcinterval0():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", interval=0)
    with pytest.raises(ValueError):
        totp.timecode(datetime.datetime(2026, 10, 23, 12, 0, 0))

def test_tcintervalneg():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", interval=-30)
    with pytest.raises(ValueError):
        totp.timecode(datetime.datetime(2026, 10, 23, 12, 0, 0))
