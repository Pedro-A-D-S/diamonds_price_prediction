"""Data contract validation node for Kedro pipeline (Great Expectations / Pandera principles)."""

from typing import Dict, Any, List

class DataContractError(ValueError):
    pass

class DiamondDataContract:
    REQUIRED_COLUMNS = ["carat", "cut", "color", "clarity", "depth", "table", "price", "x", "y", "z"]
    VALID_CUTS = ["Fair", "Good", "Very Good", "Premium", "Ideal"]

    @classmethod
    def validate_record(cls, record: Dict[str, Any]) -> bool:
        # Check column presence
        for col in cls.REQUIRED_COLUMNS:
            if col not in record:
                raise DataContractError(f"Missing required column: {col}")

        # Bounds checks
        if record["carat"] <= 0:
            raise DataContractError("Carat must be positive.")
        if record["price"] <= 0:
            raise DataContractError("Price must be positive.")
        if record["x"] <= 0 or record["y"] <= 0 or record["z"] <= 0:
            raise DataContractError("Physical dimensions x, y, z must be strictly positive.")
        if record["cut"] not in cls.VALID_CUTS:
            raise DataContractError(f"Invalid diamond cut category: {record['cut']}")

        return True

    @classmethod
    def validate_batch(cls, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        valid_count = 0
        for r in records:
            if cls.validate_record(r):
                valid_count += 1
        return {"total_validated": valid_count, "contract_status": "PASSED"}
