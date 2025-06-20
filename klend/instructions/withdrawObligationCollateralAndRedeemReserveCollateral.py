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
class WithdrawObligationCollateralAndRedeemReserveCollateralArgs(typing.TypedDict):
    collateralAmount:int


layout = borsh.CStruct(
    "collateralAmount" /borsh.U64,
    )


class WithdrawObligationCollateralAndRedeemReserveCollateralAccounts(typing.TypedDict):
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

def WithdrawObligationCollateralAndRedeemReserveCollateral(
    args: WithdrawObligationCollateralAndRedeemReserveCollateralArgs,
    accounts: WithdrawObligationCollateralAndRedeemReserveCollateralAccounts,
    program_id: SolPubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) ->Instruction:
    keys: list[AccountMeta] = [
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
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x4b\x5d\x5d\xdc\x22\x96\xda\xc4"
    encoded_args = layout.build({
        "collateralAmount":args["collateralAmount"],
       })
    data = identifier + encoded_args
    return Instruction(program_id,data,keys)




