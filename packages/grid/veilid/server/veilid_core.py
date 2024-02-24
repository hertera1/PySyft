# stdlib
from typing import Callable
from typing import Optional

# third party
import veilid
from veilid import KeyPair
from veilid import VeilidUpdate
from veilid.json_api import _JsonVeilidAPI

# relative
from .constants import HOST
from .constants import PORT
from .veilid_db import load_dht_key
from .veilid_db import store_dht_key
from .veilid_db import store_dht_key_creds


async def main_callback(update: VeilidUpdate) -> None:
    print(update)


async def noop_callback(update: VeilidUpdate) -> None:
    pass


async def get_veilid_conn(
    host: str = HOST, port: int = PORT, update_callback: Callable = noop_callback
) -> _JsonVeilidAPI:
    return await veilid.json_api_connect(
        host=HOST, port=PORT, update_callback=noop_callback
    )


class VeilidConnectionSingleton:
    _instance = None

    def __new__(cls) -> "VeilidConnectionSingleton":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def __init__(self) -> None:
        self._connection: Optional[_JsonVeilidAPI] = None

    @property
    def connection(self) -> Optional[_JsonVeilidAPI]:
        return self._connection

    async def initialize_connection(self) -> None:
        if self._connection is None:
            self._connection = await get_veilid_conn(update_callback=main_callback)
            # TODO: Shift to Logging Module
            print("Connected to Veilid")

    async def release_connection(self) -> None:
        if self._connection is not None:
            await self._connection.release()
            # TODO: Shift to Logging Module
            print("Disconnected from Veilid")
            self._connection = None


async def generate_dht_key() -> dict[str, str]:
    conn = await get_veilid_conn()

    if await load_dht_key(conn):
        return {"message": "DHT Key already exists"}

    router = await (await conn.new_routing_context()).with_default_safety()

    dht_record = await router.create_dht_record(veilid.DHTSchema.dflt(1))
    keypair = KeyPair.from_parts(key=dht_record.owner, secret=dht_record.owner_secret)

    await store_dht_key(conn, dht_record.key)
    await store_dht_key_creds(conn, keypair)

    return {"message": "DHT Key generated successfully"}


async def retrieve_dht_key() -> dict[str, str]:
    conn = await get_veilid_conn()

    dht_key = await load_dht_key(conn)

    if dht_key is None:
        return {"message": "DHT Key does not exist"}
    return {"message": str(dht_key)}
