'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from construct import Container
from dataclasses import dataclass
from solders.pubkey import Pubkey as SolPubkey

class PythConfigurationJSON(typing.TypedDict):
    price: str

@dataclass
class PythConfiguration:
    layout: typing.ClassVar = borsh.CStruct(
        "price" /BorshPubkey,
        )
    #fields
    price: SolPubkey
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "PythConfiguration":
        return cls(
        price=obj["price"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "price": self.price,
                }

    def to_json(self) -> PythConfigurationJSON:
        return {
                "price": str(self.price),
                }

    @classmethod
    def from_json(cls, obj: PythConfigurationJSON) -> "PythConfiguration":
        return cls(
                price=SolPubkey.from_string(obj["price"]),
        )






