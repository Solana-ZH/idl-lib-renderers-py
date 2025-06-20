'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import EnumForCodegen
from dataclasses import dataclass


class ActiveJSON(typing.TypedDict):
    kind: typing.Literal["Active"]


@dataclass
class Active:
    discriminator: typing.ClassVar = 0
    def to_json(self) -> ActiveJSON:
        return ActiveJSON(
            kind="Active",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Active": {},
        }




class ObsoleteJSON(typing.TypedDict):
    kind: typing.Literal["Obsolete"]


@dataclass
class Obsolete:
    discriminator: typing.ClassVar = 1
    def to_json(self) -> ObsoleteJSON:
        return ObsoleteJSON(
            kind="Obsolete",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Obsolete": {},
        }




class HiddenJSON(typing.TypedDict):
    kind: typing.Literal["Hidden"]


@dataclass
class Hidden:
    discriminator: typing.ClassVar = 2
    def to_json(self) -> HiddenJSON:
        return HiddenJSON(
            kind="Hidden",
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "Hidden": {},
        }





ReserveStatusKind = typing.Union[
    Active,
    Obsolete,
    Hidden,
]
ReserveStatusJSON = typing.Union[
    ActiveJSON,
    ObsoleteJSON,
    HiddenJSON,
]

def from_decoded(obj: dict) -> ReserveStatusKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "Active" in obj:
      return Active()
    if "Obsolete" in obj:
      return Obsolete()
    if "Hidden" in obj:
      return Hidden()
    raise ValueError("Invalid enum object")

def from_json(obj: ReserveStatusJSON) -> ReserveStatusKind:
    if obj["kind"] == "Active":
        return Active()

    if obj["kind"] == "Obsolete":
        return Obsolete()

    if obj["kind"] == "Hidden":
        return Hidden()

    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
"Active" / borsh.CStruct(),
"Obsolete" / borsh.CStruct(),
"Hidden" / borsh.CStruct(),
)
