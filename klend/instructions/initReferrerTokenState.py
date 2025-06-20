'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import typing
from solders.instruction import AccountMeta, Instruction
from solders.pubkey import Pubkey as SolPubkey
from ..program_id import PROGRAM_ID

class InitReferrerTokenStateAccounts(typing.TypedDict):
    payer:SolPubkey
    lendingMarket:SolPubkey
    reserve:SolPubkey
    referrer:SolPubkey
    referrerTokenState:SolPubkey
    rent:SolPubkey
    systemProgram:SolPubkey

def InitReferrerTokenState(
    accounts: InitReferrerTokenStateAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["lendingMarket"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["reserve"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["referrer"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["referrerTokenState"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["rent"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["systemProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x74\x2d\x42\x94\x3a\x0d\xda\x73"
    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)








