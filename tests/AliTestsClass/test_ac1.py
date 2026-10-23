import hashlib
import pyotp

def test_sequence():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert hotp.verify(hotp.at(0), 0) == True
    assert hotp.verify(hotp.at(1), 1) == True
    assert hotp.at(0) != hotp.at(1)

def test_sha512():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digest=hashlib.sha512)
    code = hotp.at(0)
    assert hotp.verify(code, 0) == True

def test_initialcount():
    hotp1 = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", initial_count=10)
    hotp2 = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert hotp1.at(0) == hotp2.at(10)

def test_twosecrets():
    hotp1 = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    hotp2 = pyotp.HOTP("JBSWY3DPEHPK3PXP")
    assert hotp1.at(0) != hotp2.at(0)

def test_uriname():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", name="bob", issuer="Bank")
    copy = pyotp.parse_uri(hotp.provisioning_uri())
    assert copy.name == "bob"
    assert copy.issuer == "Bank"

def test_roundtrip10():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", digits=10)
    copy = pyotp.parse_uri(hotp.provisioning_uri("alice"))
    assert copy.at(0) == hotp.at(0)

def test_issuercolon():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ", name="bob", issuer="Ac:me")
    copy = pyotp.parse_uri(hotp.provisioning_uri())
    assert copy.issuer == "Ac:me"
