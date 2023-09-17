from symbolchain.facade.SymbolFacade import SymbolFacade
from libs.config import NODE, PRIVATE_KEY, log
from libs.symbol.Account import Account
from libs.symbol.Mosaic import Mosaic
from libs.symbol.transaction.TransferTransaction import TransferTransaction
import asyncio


recipient_address = input("Enter recipient address: ")
amount = input("Enter amount: ")


async def main():
    facade: SymbolFacade = SymbolFacade("testnet")
    transaction_factory = TransferTransaction(facade)
    account = Account(facade, PRIVATE_KEY)

    transaction = transaction_factory.create(
        recipient_address=recipient_address,
        signer_public_key=account.public_key,
        mosaics=[Mosaic("72C0212E67A08BCE", 6).to_with_amount(float(amount))],
    )

    payload: str = account.sign(transaction)
    hash: str = transaction_factory.hash(transaction)

    await transaction_factory.announce_async(NODE, payload, account.address, hash)
    log.info(
        f"Announce Successfule. Transaction hash is {hash}. from {account.address} to {recipient_address}"
    )


asyncio.run(main())
