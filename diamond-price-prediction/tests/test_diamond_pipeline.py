import pytest
from diamond_price_prediction.data_contract import DiamondDataContract, DataContractError
from diamond_price_prediction.serving.engine import DiamondValuationEngine

def test_data_contract_valid_record():
    valid_diamond = {
        "carat": 1.25,
        "cut": "Ideal",
        "color": "G",
        "clarity": "VS1",
        "depth": 61.8,
        "table": 56.0,
        "price": 8200.0,
        "x": 6.85,
        "y": 6.89,
        "z": 4.24
    }
    assert DiamondDataContract.validate_record(valid_diamond) is True

def test_data_contract_invalid_zero_dimension():
    invalid_diamond = {
        "carat": 1.0,
        "cut": "Ideal",
        "color": "D",
        "clarity": "IF",
        "depth": 60.0,
        "table": 55.0,
        "price": 5000.0,
        "x": 0.0, # Impossible zero length
        "y": 6.0,
        "z": 4.0
    }
    with pytest.raises(DataContractError, match="strictly positive"):
        DiamondDataContract.validate_record(invalid_diamond)

def test_diamond_serving_engine_prediction():
    engine = DiamondValuationEngine()
    req = {"carat": 2.0, "depth": 62.0}
    res = engine.estimate_price(req)
    assert res["estimated_price_usd"] > 10000.0
    assert res["currency"] == "USD"
    assert res["latency_ms"] >= 0.0
