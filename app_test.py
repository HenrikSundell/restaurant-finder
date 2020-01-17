from app import app, get_distance

def test_get_distance():
    d1 = get_distance((59.990967, 24.463767), (60.993223, 25.463767))
    d2 = get_distance((60.17045, 24.93147), (60.16898783926865, 24.939225018024445))
    d3 = get_distance((60.16923121347787, 24.944517016410828), (60.16898783926865, 24.939225018024445))
    d4 = get_distance((59.990967, 24.463767), (59.990967, 24.463767))
    assert round(d1) == 124
    assert round(d2,3) == 0.459
    assert round(d3,3) == 0.294
    assert d4 == 0.0