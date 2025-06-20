'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from construct import Container
from dataclasses import dataclass
from . import borrowRateCurve, reserveFees, tokenInfo, withdrawalCaps

class ReserveConfigJSON(typing.TypedDict):
    status: int
    assetTier: int
    hostFixedInterestRateBps: int
    reserved2: list[int]
    protocolOrderExecutionFeePct: int
    protocolTakeRatePct: int
    protocolLiquidationFeePct: int
    loanToValuePct: int
    liquidationThresholdPct: int
    minLiquidationBonusBps: int
    maxLiquidationBonusBps: int
    badDebtLiquidationBonusBps: int
    deleveragingMarginCallPeriodSecs: int
    deleveragingThresholdDecreaseBpsPerDay: int
    fees: reserveFees.ReserveFeesJSON
    borrowRateCurve: borrowRateCurve.BorrowRateCurveJSON
    borrowFactorPct: int
    depositLimit: int
    borrowLimit: int
    tokenInfo: tokenInfo.TokenInfoJSON
    depositWithdrawalCap: withdrawalCaps.WithdrawalCapsJSON
    debtWithdrawalCap: withdrawalCaps.WithdrawalCapsJSON
    elevationGroups: list[int]
    disableUsageAsCollOutsideEmode: int
    utilizationLimitBlockBorrowingAbovePct: int
    autodeleverageEnabled: int
    reserved1: list[int]
    borrowLimitOutsideElevationGroup: int
    borrowLimitAgainstThisCollateralInElevationGroup: list[int]
    deleveragingBonusIncreaseBpsPerDay: int

@dataclass
class ReserveConfig:
    layout: typing.ClassVar = borsh.CStruct(
        "status" /borsh.U8,
        "assetTier" /borsh.U8,
        "hostFixedInterestRateBps" /borsh.U16,
        "reserved2" /borsh.U8[9],
        "protocolOrderExecutionFeePct" /borsh.U8,
        "protocolTakeRatePct" /borsh.U8,
        "protocolLiquidationFeePct" /borsh.U8,
        "loanToValuePct" /borsh.U8,
        "liquidationThresholdPct" /borsh.U8,
        "minLiquidationBonusBps" /borsh.U16,
        "maxLiquidationBonusBps" /borsh.U16,
        "badDebtLiquidationBonusBps" /borsh.U16,
        "deleveragingMarginCallPeriodSecs" /borsh.U64,
        "deleveragingThresholdDecreaseBpsPerDay" /borsh.U64,
        "fees" /reserveFees.ReserveFees.layout,
        "borrowRateCurve" /borrowRateCurve.BorrowRateCurve.layout,
        "borrowFactorPct" /borsh.U64,
        "depositLimit" /borsh.U64,
        "borrowLimit" /borsh.U64,
        "tokenInfo" /tokenInfo.TokenInfo.layout,
        "depositWithdrawalCap" /withdrawalCaps.WithdrawalCaps.layout,
        "debtWithdrawalCap" /withdrawalCaps.WithdrawalCaps.layout,
        "elevationGroups" /borsh.U8[20],
        "disableUsageAsCollOutsideEmode" /borsh.U8,
        "utilizationLimitBlockBorrowingAbovePct" /borsh.U8,
        "autodeleverageEnabled" /borsh.U8,
        "reserved1" /borsh.U8[1],
        "borrowLimitOutsideElevationGroup" /borsh.U64,
        "borrowLimitAgainstThisCollateralInElevationGroup" /borsh.U64[32],
        "deleveragingBonusIncreaseBpsPerDay" /borsh.U64,
        )
    #fields
    status: int
    assetTier: int
    hostFixedInterestRateBps: int
    reserved2: list[int]
    protocolOrderExecutionFeePct: int
    protocolTakeRatePct: int
    protocolLiquidationFeePct: int
    loanToValuePct: int
    liquidationThresholdPct: int
    minLiquidationBonusBps: int
    maxLiquidationBonusBps: int
    badDebtLiquidationBonusBps: int
    deleveragingMarginCallPeriodSecs: int
    deleveragingThresholdDecreaseBpsPerDay: int
    fees: reserveFees.ReserveFees
    borrowRateCurve: borrowRateCurve.BorrowRateCurve
    borrowFactorPct: int
    depositLimit: int
    borrowLimit: int
    tokenInfo: tokenInfo.TokenInfo
    depositWithdrawalCap: withdrawalCaps.WithdrawalCaps
    debtWithdrawalCap: withdrawalCaps.WithdrawalCaps
    elevationGroups: list[int]
    disableUsageAsCollOutsideEmode: int
    utilizationLimitBlockBorrowingAbovePct: int
    autodeleverageEnabled: int
    reserved1: list[int]
    borrowLimitOutsideElevationGroup: int
    borrowLimitAgainstThisCollateralInElevationGroup: list[int]
    deleveragingBonusIncreaseBpsPerDay: int
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "ReserveConfig":
        return cls(
        status=obj["status"],
        assetTier=obj["assetTier"],
        hostFixedInterestRateBps=obj["hostFixedInterestRateBps"],
        reserved2=obj["reserved2"],
        protocolOrderExecutionFeePct=obj["protocolOrderExecutionFeePct"],
        protocolTakeRatePct=obj["protocolTakeRatePct"],
        protocolLiquidationFeePct=obj["protocolLiquidationFeePct"],
        loanToValuePct=obj["loanToValuePct"],
        liquidationThresholdPct=obj["liquidationThresholdPct"],
        minLiquidationBonusBps=obj["minLiquidationBonusBps"],
        maxLiquidationBonusBps=obj["maxLiquidationBonusBps"],
        badDebtLiquidationBonusBps=obj["badDebtLiquidationBonusBps"],
        deleveragingMarginCallPeriodSecs=obj["deleveragingMarginCallPeriodSecs"],
        deleveragingThresholdDecreaseBpsPerDay=obj["deleveragingThresholdDecreaseBpsPerDay"],
        fees=reserveFees.ReserveFees.from_decoded(obj["fees"]),
        borrowRateCurve=borrowRateCurve.BorrowRateCurve.from_decoded(obj["borrowRateCurve"]),
        borrowFactorPct=obj["borrowFactorPct"],
        depositLimit=obj["depositLimit"],
        borrowLimit=obj["borrowLimit"],
        tokenInfo=tokenInfo.TokenInfo.from_decoded(obj["tokenInfo"]),
        depositWithdrawalCap=withdrawalCaps.WithdrawalCaps.from_decoded(obj["depositWithdrawalCap"]),
        debtWithdrawalCap=withdrawalCaps.WithdrawalCaps.from_decoded(obj["debtWithdrawalCap"]),
        elevationGroups=obj["elevationGroups"],
        disableUsageAsCollOutsideEmode=obj["disableUsageAsCollOutsideEmode"],
        utilizationLimitBlockBorrowingAbovePct=obj["utilizationLimitBlockBorrowingAbovePct"],
        autodeleverageEnabled=obj["autodeleverageEnabled"],
        reserved1=obj["reserved1"],
        borrowLimitOutsideElevationGroup=obj["borrowLimitOutsideElevationGroup"],
        borrowLimitAgainstThisCollateralInElevationGroup=obj["borrowLimitAgainstThisCollateralInElevationGroup"],
        deleveragingBonusIncreaseBpsPerDay=obj["deleveragingBonusIncreaseBpsPerDay"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "status": self.status,
                "assetTier": self.assetTier,
                "hostFixedInterestRateBps": self.hostFixedInterestRateBps,
                "reserved2": self.reserved2,
                "protocolOrderExecutionFeePct": self.protocolOrderExecutionFeePct,
                "protocolTakeRatePct": self.protocolTakeRatePct,
                "protocolLiquidationFeePct": self.protocolLiquidationFeePct,
                "loanToValuePct": self.loanToValuePct,
                "liquidationThresholdPct": self.liquidationThresholdPct,
                "minLiquidationBonusBps": self.minLiquidationBonusBps,
                "maxLiquidationBonusBps": self.maxLiquidationBonusBps,
                "badDebtLiquidationBonusBps": self.badDebtLiquidationBonusBps,
                "deleveragingMarginCallPeriodSecs": self.deleveragingMarginCallPeriodSecs,
                "deleveragingThresholdDecreaseBpsPerDay": self.deleveragingThresholdDecreaseBpsPerDay,
                "fees": self.fees.to_encodable(),
                "borrowRateCurve": self.borrowRateCurve.to_encodable(),
                "borrowFactorPct": self.borrowFactorPct,
                "depositLimit": self.depositLimit,
                "borrowLimit": self.borrowLimit,
                "tokenInfo": self.tokenInfo.to_encodable(),
                "depositWithdrawalCap": self.depositWithdrawalCap.to_encodable(),
                "debtWithdrawalCap": self.debtWithdrawalCap.to_encodable(),
                "elevationGroups": self.elevationGroups,
                "disableUsageAsCollOutsideEmode": self.disableUsageAsCollOutsideEmode,
                "utilizationLimitBlockBorrowingAbovePct": self.utilizationLimitBlockBorrowingAbovePct,
                "autodeleverageEnabled": self.autodeleverageEnabled,
                "reserved1": self.reserved1,
                "borrowLimitOutsideElevationGroup": self.borrowLimitOutsideElevationGroup,
                "borrowLimitAgainstThisCollateralInElevationGroup": self.borrowLimitAgainstThisCollateralInElevationGroup,
                "deleveragingBonusIncreaseBpsPerDay": self.deleveragingBonusIncreaseBpsPerDay,
                }

    def to_json(self) -> ReserveConfigJSON:
        return {
                "status": self.status,
                "assetTier": self.assetTier,
                "hostFixedInterestRateBps": self.hostFixedInterestRateBps,
                "reserved2": self.reserved2,
                "protocolOrderExecutionFeePct": self.protocolOrderExecutionFeePct,
                "protocolTakeRatePct": self.protocolTakeRatePct,
                "protocolLiquidationFeePct": self.protocolLiquidationFeePct,
                "loanToValuePct": self.loanToValuePct,
                "liquidationThresholdPct": self.liquidationThresholdPct,
                "minLiquidationBonusBps": self.minLiquidationBonusBps,
                "maxLiquidationBonusBps": self.maxLiquidationBonusBps,
                "badDebtLiquidationBonusBps": self.badDebtLiquidationBonusBps,
                "deleveragingMarginCallPeriodSecs": self.deleveragingMarginCallPeriodSecs,
                "deleveragingThresholdDecreaseBpsPerDay": self.deleveragingThresholdDecreaseBpsPerDay,
                "fees": self.fees.to_json(),
                "borrowRateCurve": self.borrowRateCurve.to_json(),
                "borrowFactorPct": self.borrowFactorPct,
                "depositLimit": self.depositLimit,
                "borrowLimit": self.borrowLimit,
                "tokenInfo": self.tokenInfo.to_json(),
                "depositWithdrawalCap": self.depositWithdrawalCap.to_json(),
                "debtWithdrawalCap": self.debtWithdrawalCap.to_json(),
                "elevationGroups": self.elevationGroups,
                "disableUsageAsCollOutsideEmode": self.disableUsageAsCollOutsideEmode,
                "utilizationLimitBlockBorrowingAbovePct": self.utilizationLimitBlockBorrowingAbovePct,
                "autodeleverageEnabled": self.autodeleverageEnabled,
                "reserved1": self.reserved1,
                "borrowLimitOutsideElevationGroup": self.borrowLimitOutsideElevationGroup,
                "borrowLimitAgainstThisCollateralInElevationGroup": self.borrowLimitAgainstThisCollateralInElevationGroup,
                "deleveragingBonusIncreaseBpsPerDay": self.deleveragingBonusIncreaseBpsPerDay,
                }

    @classmethod
    def from_json(cls, obj: ReserveConfigJSON) -> "ReserveConfig":
        return cls(
                status=obj["status"],
                assetTier=obj["assetTier"],
                hostFixedInterestRateBps=obj["hostFixedInterestRateBps"],
                reserved2=obj["reserved2"],
                protocolOrderExecutionFeePct=obj["protocolOrderExecutionFeePct"],
                protocolTakeRatePct=obj["protocolTakeRatePct"],
                protocolLiquidationFeePct=obj["protocolLiquidationFeePct"],
                loanToValuePct=obj["loanToValuePct"],
                liquidationThresholdPct=obj["liquidationThresholdPct"],
                minLiquidationBonusBps=obj["minLiquidationBonusBps"],
                maxLiquidationBonusBps=obj["maxLiquidationBonusBps"],
                badDebtLiquidationBonusBps=obj["badDebtLiquidationBonusBps"],
                deleveragingMarginCallPeriodSecs=obj["deleveragingMarginCallPeriodSecs"],
                deleveragingThresholdDecreaseBpsPerDay=obj["deleveragingThresholdDecreaseBpsPerDay"],
                fees=reserveFees.ReserveFees.from_json(obj["fees"]),
                borrowRateCurve=borrowRateCurve.BorrowRateCurve.from_json(obj["borrowRateCurve"]),
                borrowFactorPct=obj["borrowFactorPct"],
                depositLimit=obj["depositLimit"],
                borrowLimit=obj["borrowLimit"],
                tokenInfo=tokenInfo.TokenInfo.from_json(obj["tokenInfo"]),
                depositWithdrawalCap=withdrawalCaps.WithdrawalCaps.from_json(obj["depositWithdrawalCap"]),
                debtWithdrawalCap=withdrawalCaps.WithdrawalCaps.from_json(obj["debtWithdrawalCap"]),
                elevationGroups=obj["elevationGroups"],
                disableUsageAsCollOutsideEmode=obj["disableUsageAsCollOutsideEmode"],
                utilizationLimitBlockBorrowingAbovePct=obj["utilizationLimitBlockBorrowingAbovePct"],
                autodeleverageEnabled=obj["autodeleverageEnabled"],
                reserved1=obj["reserved1"],
                borrowLimitOutsideElevationGroup=obj["borrowLimitOutsideElevationGroup"],
                borrowLimitAgainstThisCollateralInElevationGroup=obj["borrowLimitAgainstThisCollateralInElevationGroup"],
                deleveragingBonusIncreaseBpsPerDay=obj["deleveragingBonusIncreaseBpsPerDay"],
        )






