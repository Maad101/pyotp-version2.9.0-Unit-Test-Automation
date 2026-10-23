import pytest
import pyotp

def test_nowverify():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert totp.verify(totp.now()) == True

def test_samewindow():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    code = totp.at(1700000010)
    assert totp.verify(code, for_time=1700000039) == True

def test_nextwindow():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    code = totp.at(1700000010)
    assert totp.verify(code, for_time=1700000040) == False

def test_validwindow1():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    code = totp.at(1700000010)
    assert totp.verify(code, for_time=1700000040, valid_window=1) == True

def test_uriroundtrip():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", name="alice", issuer="ACME")
    copy = pyotp.parse_uri(totp.provisioning_uri())
    assert copy.at(1700000010) == totp.at(1700000010)

def test_roundtrip9():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digits=9)
    copy = pyotp.parse_uri(totp.provisioning_uri("alice"))
    assert copy.at(1700000010) == totp.at(1700000010)

def test_period0uri():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", interval=0)
    with pytest.raises(ValueError):
        totp.provisioning_uri("alice")
