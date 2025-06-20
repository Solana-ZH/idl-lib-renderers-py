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
class RepayObligationLiquidityV2Args(typing.TypedDict):
    liquidityAmount:int


layout = borsh.CStruct(
    "liquidityAmount" /borsh.U64,
    )


class RepayObligationLiquidityV2Accounts(typing.TypedDict):
    owner:SolPubkey
    obligation:SolPubkey
    lendingMarket:SolPubkey
    repayReserve:SolPubkey
    reserveLiquidityMint:SolPubkey
    reserveDestinationLiquidity:SolPubkey
    userSourceLiquidity:SolPubkey
    tokenProgram:SolPubkey
    instructionSysvarAccount:SolPubkey
    obligationFarmUserState:SolPubkey
    reserveFarmState:SolPubkey
    lendingMarketAuthority:SolPubkey
    farmsProgram:SolPubkey

def RepayObligationLiquidityV2(
    args: RepayObligationLiquidityV2Args,
    accounts: RepayObligationLiquidityV2Accounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
    AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=False),
    AccountMeta(pubkey=accounts["obligation"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["lendingMarket"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["repayReserve"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["reserveLiquidityMint"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["reserveDestinationLiquidity"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["userSourceLiquidity"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["tokenProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["instructionSysvarAccount"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["obligationFarmUserState"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["reserveFarmState"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["lendingMarketAuthority"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["farmsProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x74\xae\xd5\x4c\xb4\x35\xd2\x90"
    encoded_args = layout.build({
        "liquidityAmount":args["liquidityAmount"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)






