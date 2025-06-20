'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import PROGRAM_ID
class UpdateReserveConfigArgs(typing.TypedDict):
    mode:int
    value:str
    skipValidation:bool


layout = borsh.CStruct(
    "mode" /borsh.U64,
    "value" /borsh.String,
    "skipValidation" /borsh.Bool,
    )


class UpdateReserveConfigAccounts(typing.TypedDict):
    lendingMarketOwner:SolPubkey
    lendingMarket:SolPubkey
    reserve:SolPubkey

def UpdateReserveConfig(
    args: UpdateReserveConfigArgs,
    accounts: UpdateReserveConfigAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["lendingMarketOwner"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["lendingMarket"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["reserve"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x3d\x94\x64\x46\x8f\x6b\x11\x0d"
    encoded_args = layout.build({
        "mode":args["mode"],
        "value":args["value"],
        "skipValidation":args["skipValidation"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



