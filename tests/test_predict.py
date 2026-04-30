from ai_model.predict import classify_waste

def test_battery():
    assert classify_waste(1) == "battery"

def test_cable():
    assert classify_waste(2) == "cable"

def test_circuit():
    assert classify_waste(3) == "circuit"

def test_mobile():
    assert classify_waste(4) == "mobile"
