import pyotp
def test_at_counter_0():
    hotp = pyotp.HOTP("GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ")
    assert hotp.at(0) == "755224"