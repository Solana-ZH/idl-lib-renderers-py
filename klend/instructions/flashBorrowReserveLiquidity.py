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
class FlashBorrowReserveLiquidityArgs(typing.TypedDict):
    liquidityAmount:int


layout = borsh.CStruct(
    "liquidityAmount" /borsh.U64,
    )


class FlashBorrowReserveLiquidityAccounts(typing.TypedDict):
    userTransferAuthority:SolPubkey
    lendingMarketAuthority:SolPubkey
    lendingMarket:SolPubkey
    reserve:SolPubkey
    reserveLiquidityMint:SolPubkey
    reserveSourceLiquidity:SolPubkey
    userDestinationLiquidity:SolPubkey
    reserveLiquidityFeeReceiver:SolPubkey
    referrerTokenState:SolPubkey
    referrerAccount:SolPubkey
    sysvarInfo:SolPubkey
    tokenProgram:SolPubkey

def FlashBorrowReserveLiquidity(
    args: FlashBorrowReserveLiquidityArgs,
    accounts: FlashBorrowReserveLiquidityAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["userTransferAuthority"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["lendingMarketAuthority"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["lendingMarket"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["reserve"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["reserveLiquidityMint"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["reserveSourceLiquidity"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["userDestinationLiquidity"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["reserveLiquidityFeeReceiver"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["referrerTokenState"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["referrerAccount"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["sysvarInfo"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["tokenProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x87\xe7\x34\xa7\x07\x34\xd4\xc1"
    encoded_args = layout.build({
        "liquidityAmount":args["liquidityAmount"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




