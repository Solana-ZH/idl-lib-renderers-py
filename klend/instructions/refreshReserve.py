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

class RefreshReserveAccounts(typing.TypedDict):
    reserve:SolPubkey
    lendingMarket:SolPubkey
    pythOracle:SolPubkey
    switchboardPriceOracle:SolPubkey
    switchboardTwapOracle:SolPubkey
    scopePrices:SolPubkey

def RefreshReserve(
    accounts: RefreshReserveAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["reserve"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["lendingMarket"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["pythOracle"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["switchboardPriceOracle"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["switchboardTwapOracle"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["scopePrices"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x02\xda\x8a\xeb\x4f\xc9\x19\x66"
    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)



