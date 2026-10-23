import pytest
import pyotp
pytestmark = [pytest.mark.hotp, pytest.mark.classes, pytest.mark.order(4)]

def test_gennver():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    code = hotp.at(5)
    assert hotp.verify(code, 5) == True

def test_wrngcount():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    code = hotp.at(5)
    assert hotp.verify(code, 6) == False

def test_eightdigits():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digits=8)
    code = hotp.at(0)
    assert len(code) == 8
    assert hotp.verify(code, 0) == True

def test_uricircletrip():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", name="alice", issuer="ACME")
    uri = hotp.provisioning_uri()
    copy = pyotp.parse_uri(uri)
    assert copy.at(3) == hotp.at(3)

def test_negicount():
    with pytest.raises(ValueError):
        pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", initial_count=-5)

def test_invalidsecrets():
    with pytest.raises(ValueError):
        pyotp.HOTP("not base32!!")

def test_digitzero():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digits=0)
    code = hotp.at(0)
    assert len(code) == hotp.digits
