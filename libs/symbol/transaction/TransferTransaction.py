from symbolchain.facade.SymbolFacade import SymbolFacade
from symbolchain.sc import TransferTransactionV1
from libs.symbol.transaction.base import BaseTransaction
from libs.symbol.transaction.common import FeeConfig


class TransferTransaction(BaseTransaction):
    def __init__(self, facade: SymbolFacade) -> None:
        super().__init__(facade)

    def fee(self, message: bytes, fee: FeeConfig = FeeConfig.normal) -> int:
        size = self.create(
            recipient_address="NASYMBOLLK6FSL7GSEMQEAWN7VW55ZSZU25TBOA",  # dummy
            signer_public_key="",
            deadline_by_hour=self.deadline_by_hours(2),  # dummy
            message=message,
            mosaics=[],  # dummy
            fee=0,  # dummy
        ).size
        return int(size * 1000 * fee.value)

    def create(
        self,
        recipient_address: str,
        signer_public_key: str,
        mosaics: list[dict[str, int]] = [],
        message: bytes = bytes([]),
        deadline_by_hour: int = 2,
        fee: int = 100000,
    ) -> TransferTransactionV1:
        return self.facade.transaction_factory.create(
            {
                "type": "transfer_transaction_v1",
                "signer_public_key": signer_public_key,
                "fee": fee,
                "deadline": self.deadline_by_hours(deadline_by_hour),
                "recipient_address": recipient_address,
                "mosaics": mosaics,
                "message": message,
            }
        )
