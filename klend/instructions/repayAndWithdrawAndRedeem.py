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
class RepayAndWithdrawAndRedeemArgs(typing.TypedDict):
    repayAmount:int
    withdrawCollateralAmount:int


layout = borsh.CStruct(
    "repayAmount" /borsh.U64,
    "withdrawCollateralAmount" /borsh.U64,
    )


class RepayAndWithdrawAndRedeemAccounts(typing.TypedDict):
    owner:SolPubkey
    obligation:SolPubkey
    lendingMarket:SolPubkey
    repayReserve:SolPubkey
    reserveLiquidityMint:SolPubkey
    reserveDestinationLiquidity:SolPubkey
    userSourceLiquidity:SolPubkey
    tokenProgram:SolPubkey
    instructionSysvarAccount:SolPubkey
    owner:SolPubkey
    obligation:SolPubkey
    lendingMarket:SolPubkey
    lendingMarketAuthority:SolPubkey
    withdrawReserve:SolPubkey
    reserveLiquidityMint:SolPubkey
    reserveSourceCollateral:SolPubkey
    reserveCollateralMint:SolPubkey
    reserveLiquiditySupply:SolPubkey
    userDestinationLiquidity:SolPubkey
    placeholderUserDestinationCollateral:SolPubkey
    collateralTokenProgram:SolPubkey
    liquidityTokenProgram:SolPubkey
    instructionSysvarAccount:SolPubkey
    obligationFarmUserState:SolPubkey
    reserveFarmState:SolPubkey
    obligationFarmUserState:SolPubkey
    reserveFarmState:SolPubkey
    farmsProgram:SolPubkey

def RepayAndWithdrawAndRedeem(
    args: RepayAndWithdrawAndRedeemArgs,
    accounts: RepayAndWithdrawAndRedeemAccounts,
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
    AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=True),
    AccountMeta(pubkey=accounts["obligation"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["lendingMarket"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["lendingMarketAuthority"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["withdrawReserve"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["reserveLiquidityMint"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["reserveSourceCollateral"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["reserveCollateralMint"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["reserveLiquiditySupply"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["userDestinationLiquidity"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["placeholderUserDestinationCollateral"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["collateralTokenProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["liquidityTokenProgram"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["instructionSysvarAccount"], is_signer=False, is_writable=False),
    AccountMeta(pubkey=accounts["obligationFarmUserState"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["reserveFarmState"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["obligationFarmUserState"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["reserveFarmState"], is_signer=False, is_writable=True),
    AccountMeta(pubkey=accounts["farmsProgram"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x02\x36\x98\x03\x94\x60\x6d\xda"
    encoded_args = layout.build({
        "repayAmount":args["repayAmount"],
        "withdrawCollateralAmount":args["withdrawCollateralAmount"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)








