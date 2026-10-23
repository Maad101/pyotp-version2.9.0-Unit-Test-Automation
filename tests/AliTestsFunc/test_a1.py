import pytest
import pyotp

def test_uristart():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    uri = hotp.provisioning_uri("alice")
    assert uri.startswith("otpauth://hotp/")

def test_urisecret():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    uri = hotp.provisioning_uri("alice")
    assert "secret=GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ" in uri

def test_uricounter0():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    uri = hotp.provisioning_uri("alice")
    assert "counter=0" in uri

def test_uriissuer():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    uri = hotp.provisioning_uri("alice", issuer_name="ACME")
    assert "ACME:alice" in uri

def test_urihttpimage():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    with pytest.raises(ValueError):
        hotp.provisioning_uri("alice", image="http://example.com/logo.png")

def test_urinegcounter():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", initial_count=-5)
    with pytest.raises(ValueError):
        hotp.provisioning_uri("alice")

def test_uridigitszero():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digits=0)
    with pytest.raises(ValueError):
        hotp.provisioning_uri("alice")
