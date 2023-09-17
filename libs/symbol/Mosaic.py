import json


class Mosaic:
    def __init__(self, mosaic_id: str, divisibility: int) -> None:
        self.mosaic_id: str = mosaic_id
        self.divisibility: int = divisibility

    def to_with_amount(self, amount: float) -> dict[str, int]:
        return {
            "mosaic_id": int(f"0x{self.mosaic_id}", 16),
            "amount": int(amount * (10**self.divisibility)),
        }

    def __str__(self) -> str:
        return json.dumps(
            {
                "mosaic_id": self.mosaic_id,
                "divisibility": self.divisibility,
            }
        )
