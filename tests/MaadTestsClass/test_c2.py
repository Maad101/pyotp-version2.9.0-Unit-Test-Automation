import pytest
import pyotp
pytestmark = [pytest.mark.totp, pytest.mark.classes, pytest.mark.order(5)]

def test_genverify():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    code = totp.now()
    assert totp.verify(code) == True

def test_wrongcode():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert totp.verify("000000") == False

def test_eightdigits():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digits=8)
    code = totp.now()
    assert len(code) == 8

def test_samecode():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert totp.at(60) == totp.at(89)

def test_nextcode():
    totp = pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert totp.at(60) != totp.at(90)

def test_intervalzero():
    with pytest.raises(ValueError):
        pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", interval=0)

def test_intervalneg():
    with pytest.raises(ValueError):
        pyotp.TOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", interval=-30)
