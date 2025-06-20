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
class InitLendingMarketArgs(typing.TypedDict):
    quoteCurrency:list[int]


layout = borsh.CStruct(
    "quoteCurrency" /borsh.U8[32],
    )


class InitLendingMarketAccounts(typing.TypedDict):
    lendingMarketOwner:SolPubkey
    lendingMarket:SolPubkey
    lendingMarketAuthority:SolPubkey
    systemProgram:SolPubkey
    rent:SolPubkey

def InitLendingMarket(
    args: InitLendingMarketArgs,
    accounts: InitLendingMarketAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["lendingMarketOwner"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["lendingMarket"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["lendingMarketAuthority"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x22\xa2\x74\x0e\x65\x89\x5e\xef"
    encoded_args = layout.build({
        "quoteCurrency":args["quoteCurrency"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)






