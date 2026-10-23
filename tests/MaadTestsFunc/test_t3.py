import pytest
import pyotp
pytestmark = [pytest.mark.utils, pytest.mark.functions, pytest.mark.order(3)]

def test_defaultlen():
    secret = pyotp.random_base32()
    assert len(secret) == 32

def test_len31():
    with pytest.raises(ValueError):
        pyotp.random_base32(length=31)

def test_len33():
    secret = pyotp.random_base32(length=33)
    assert len(secret) == 33

def test_base32chars():
    secret = pyotp.random_base32()
    for ch in secret:
        assert ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

def test_emptychars():
    with pytest.raises(ValueError):
        pyotp.random_base32(chars="")

def test_invalidchars():
    with pytest.raises(ValueError):
        pyotp.random_base32(chars="189")

def test_twosecretsdiff():
    secret1 = pyotp.random_base32()
    secret2 = pyotp.random_base32()
    assert secret1 != secret2
