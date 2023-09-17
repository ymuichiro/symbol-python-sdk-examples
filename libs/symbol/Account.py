from symbolchain.CryptoTypes import PrivateKey
from symbolchain.facade.SymbolFacade import SymbolFacade
from symbolchain.symbol.Network import Network
from typing import Any


class Account:
    def __init__(self, facade: SymbolFacade, private_key: str):
        self.__facade: SymbolFacade = facade
        self.__network: Network = facade.network
        self.__private_key: PrivateKey = PrivateKey(private_key)
        self.__key_pair = self.__facade.KeyPair(self.__private_key)
        self.public_key: str = str(self.__key_pair.public_key)
        self.address: str = str(
            self.__network.public_key_to_address(self.__key_pair.public_key)
        )

    @staticmethod
    def generate_new_account(facade: SymbolFacade) -> "Account":
        return Account(facade, str(PrivateKey.random()))

    def sign(self, transaction: Any) -> str:
        key_pair = self.__facade.KeyPair(self.__private_key)
        signature = self.__facade.sign_transaction(key_pair, transaction)
        return self.__facade.transaction_factory.attach_signature(
            transaction, signature
        )
