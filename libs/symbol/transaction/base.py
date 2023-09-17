from symbolchain.facade.SymbolFacade import SymbolFacade
from symbolchain.symbol.Network import Network, NetworkTimestamp
from libs.config import log
from typing import Any
from websockets import client as ws
from datetime import datetime, timezone, timedelta
import json
import requests


class BaseTransaction:
    def __init__(self, facade: SymbolFacade) -> None:
        self.facade: SymbolFacade = facade
        self.network: Network = facade.network

    def deadline_by_hours(self, hours: int) -> int:
        deadline: NetworkTimestamp = self.network.from_datetime(
            datetime.now(tz=timezone.utc) + timedelta(hours=hours)
        )
        return int(deadline.timestamp)

    def hash(self, transaction: Any) -> str:
        """
        Note: Always sign the transaction before executing it.
        """
        return str(self.facade.hash_transaction(transaction))

    def announce(self, node: str, payload: str) -> Any:
        node = f"https://{node}:3001/transactions"
        res = requests.put(node, payload, headers={"Content-Type": "application/json"})

        if res.status_code == 202:
            return res.json()
        else:
            raise Exception(res.json())

    async def announce_async(
        self, node: str, payload: str, address: str, hash: str
    ) -> Any:
        ws_node = f"wss://{node}:3001/ws"
        async with ws.connect(ws_node) as w:
            while True:
                msg = json.loads(await w.recv())
                if "uid" in msg:
                    body1: dict[str, str] = {
                        "uid": msg["uid"],
                        "subscribe": f"status/{address}",
                    }
                    body2: dict[str, str] = {
                        "uid": msg["uid"],
                        "subscribe": f"confirmedAdded/{address}",
                    }
                    await w.send(json.dumps(body1))
                    await w.send(json.dumps(body2))
                    announced = self.announce(node, payload)
                    log.info(msg=f'Announced transaction: {announced["message"]}')
                else:
                    # cache status error
                    if msg["topic"] == f"status/{address}":
                        if msg["data"]["hash"] == hash and "code" in msg["data"]:
                            raise Exception(msg["data"]["code"])

                    # cache confirmed transaction status
                    if msg["topic"] != f"confirmedAdded/{address}":
                        continue

                    if msg["data"]["meta"]["hash"] == hash:
                        return msg["data"]
