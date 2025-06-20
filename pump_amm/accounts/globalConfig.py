'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from dataclasses import dataclass
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import PROGRAM_ID


class GlobalConfigJSON(typing.TypedDict):
    admin: str
    lpFeeBasisPoints: int
    protocolFeeBasisPoints: int
    disableFlags: int
    protocolFeeRecipients: list[str]

@dataclass
class GlobalConfig:
    #fields
    admin: SolPubkey
    lpFeeBasisPoints: int
    protocolFeeBasisPoints: int
    disableFlags: int
    protocolFeeRecipients: list[SolPubkey]

    discriminator: typing.ClassVar = b"\x95\x08\x9c\xca\xa0\xfc\xb0\xd9"
    DISCRIMINATOR_SIZE: int = 8

    layout: typing.ClassVar = borsh.CStruct(
        "admin" /BorshPubkey,
        "lpFeeBasisPoints" /borsh.U64,
        "protocolFeeBasisPoints" /borsh.U64,
        "disableFlags" /borsh.U8,
        "protocolFeeRecipients" /BorshPubkey[8],
        )



    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: SolPubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = PROGRAM_ID,
    ) -> typing.Optional["GlobalConfig"]:
        resp = await conn.get_account_info(address, commitment=commitment)
        info = resp.value
        if info is None:
            return None
        if info.owner != program_id:
            raise ValueError("Account does not belong to this program")
        bytes_data = info.data
        return cls.decode(bytes_data)

    @classmethod
    async def fetch_multiple(
        cls,
        conn: AsyncClient,
        addresses: list[SolPubkey],
        commitment: typing.Optional[Commitment] = None,
        program_id: SolPubkey = PROGRAM_ID,
    ) -> typing.List[typing.Optional["GlobalConfig"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["GlobalConfig"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "GlobalConfig":
        if data[:cls.DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = GlobalConfig.layout.parse(data[cls.DISCRIMINATOR_SIZE:])
        return cls(
                admin=dec.admin,
                lpFeeBasisPoints=dec.lpFeeBasisPoints,
                protocolFeeBasisPoints=dec.protocolFeeBasisPoints,
                disableFlags=dec.disableFlags,
                protocolFeeRecipients=dec.protocolFeeRecipients,
                )

    def to_json(self) -> GlobalConfigJSON:
        return {
                "admin": str(self.admin),
                "lpFeeBasisPoints": self.lpFeeBasisPoints,
                "protocolFeeBasisPoints": self.protocolFeeBasisPoints,
                "disableFlags": self.disableFlags,
                "protocolFeeRecipients": list(map(lambda item:str(item),self.protocolFeeRecipients)),
                }

    @classmethod
    def from_json(cls, obj: GlobalConfigJSON) -> "GlobalConfig":
        return cls(
                admin=SolPubkey.from_string(obj["admin"]),
                lpFeeBasisPoints=obj["lpFeeBasisPoints"],
                protocolFeeBasisPoints=obj["protocolFeeBasisPoints"],
                disableFlags=obj["disableFlags"],
                protocolFeeRecipients=list(map(lambda item:SolPubkey.from_string(item),obj["protocolFeeRecipients"])),
                )




