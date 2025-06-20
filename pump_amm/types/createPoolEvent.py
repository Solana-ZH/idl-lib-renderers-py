'''
    This code was AUTOGENERATED using the codama library.
    Please DO NOT EDIT THIS FILE, instead use visitors
    to add features, then rerun codama to update it.
    @see https://github.com/codama-idl/codama
'''

import borsh_construct as borsh
import typing
from anchorpy.borsh_extension import BorshPubkey
from construct import Container
from dataclasses import dataclass
from solders.pubkey import Pubkey as SolPubkey

class CreatePoolEventJSON(typing.TypedDict):
    timestamp: int
    index: int
    creator: str
    baseMint: str
    quoteMint: str
    baseMintDecimals: int
    quoteMintDecimals: int
    baseAmountIn: int
    quoteAmountIn: int
    poolBaseAmount: int
    poolQuoteAmount: int
    minimumLiquidity: int
    initialLiquidity: int
    lpTokenAmountOut: int
    poolBump: int
    pool: str
    lpMint: str
    userBaseTokenAccount: str
    userQuoteTokenAccount: str

@dataclass
class CreatePoolEvent:
    layout: typing.ClassVar = borsh.CStruct(
        "timestamp" /borsh.I64,
        "index" /borsh.U16,
        "creator" /BorshPubkey,
        "baseMint" /BorshPubkey,
        "quoteMint" /BorshPubkey,
        "baseMintDecimals" /borsh.U8,
        "quoteMintDecimals" /borsh.U8,
        "baseAmountIn" /borsh.U64,
        "quoteAmountIn" /borsh.U64,
        "poolBaseAmount" /borsh.U64,
        "poolQuoteAmount" /borsh.U64,
        "minimumLiquidity" /borsh.U64,
        "initialLiquidity" /borsh.U64,
        "lpTokenAmountOut" /borsh.U64,
        "poolBump" /borsh.U8,
        "pool" /BorshPubkey,
        "lpMint" /BorshPubkey,
        "userBaseTokenAccount" /BorshPubkey,
        "userQuoteTokenAccount" /BorshPubkey,
        )
    #fields
    timestamp: int
    index: int
    creator: SolPubkey
    baseMint: SolPubkey
    quoteMint: SolPubkey
    baseMintDecimals: int
    quoteMintDecimals: int
    baseAmountIn: int
    quoteAmountIn: int
    poolBaseAmount: int
    poolQuoteAmount: int
    minimumLiquidity: int
    initialLiquidity: int
    lpTokenAmountOut: int
    poolBump: int
    pool: SolPubkey
    lpMint: SolPubkey
    userBaseTokenAccount: SolPubkey
    userQuoteTokenAccount: SolPubkey
    
    @classmethod
    def from_decoded(cls, obj: Container) -> "CreatePoolEvent":
        return cls(
        timestamp=obj["timestamp"],
        index=obj["index"],
        creator=obj["creator"],
        baseMint=obj["baseMint"],
        quoteMint=obj["quoteMint"],
        baseMintDecimals=obj["baseMintDecimals"],
        quoteMintDecimals=obj["quoteMintDecimals"],
        baseAmountIn=obj["baseAmountIn"],
        quoteAmountIn=obj["quoteAmountIn"],
        poolBaseAmount=obj["poolBaseAmount"],
        poolQuoteAmount=obj["poolQuoteAmount"],
        minimumLiquidity=obj["minimumLiquidity"],
        initialLiquidity=obj["initialLiquidity"],
        lpTokenAmountOut=obj["lpTokenAmountOut"],
        poolBump=obj["poolBump"],
        pool=obj["pool"],
        lpMint=obj["lpMint"],
        userBaseTokenAccount=obj["userBaseTokenAccount"],
        userQuoteTokenAccount=obj["userQuoteTokenAccount"],
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
                "timestamp": self.timestamp,
                "index": self.index,
                "creator": self.creator,
                "baseMint": self.baseMint,
                "quoteMint": self.quoteMint,
                "baseMintDecimals": self.baseMintDecimals,
                "quoteMintDecimals": self.quoteMintDecimals,
                "baseAmountIn": self.baseAmountIn,
                "quoteAmountIn": self.quoteAmountIn,
                "poolBaseAmount": self.poolBaseAmount,
                "poolQuoteAmount": self.poolQuoteAmount,
                "minimumLiquidity": self.minimumLiquidity,
                "initialLiquidity": self.initialLiquidity,
                "lpTokenAmountOut": self.lpTokenAmountOut,
                "poolBump": self.poolBump,
                "pool": self.pool,
                "lpMint": self.lpMint,
                "userBaseTokenAccount": self.userBaseTokenAccount,
                "userQuoteTokenAccount": self.userQuoteTokenAccount,
                }

    def to_json(self) -> CreatePoolEventJSON:
        return {
                "timestamp": self.timestamp,
                "index": self.index,
                "creator": str(self.creator),
                "baseMint": str(self.baseMint),
                "quoteMint": str(self.quoteMint),
                "baseMintDecimals": self.baseMintDecimals,
                "quoteMintDecimals": self.quoteMintDecimals,
                "baseAmountIn": self.baseAmountIn,
                "quoteAmountIn": self.quoteAmountIn,
                "poolBaseAmount": self.poolBaseAmount,
                "poolQuoteAmount": self.poolQuoteAmount,
                "minimumLiquidity": self.minimumLiquidity,
                "initialLiquidity": self.initialLiquidity,
                "lpTokenAmountOut": self.lpTokenAmountOut,
                "poolBump": self.poolBump,
                "pool": str(self.pool),
                "lpMint": str(self.lpMint),
                "userBaseTokenAccount": str(self.userBaseTokenAccount),
                "userQuoteTokenAccount": str(self.userQuoteTokenAccount),
                }

    @classmethod
    def from_json(cls, obj: CreatePoolEventJSON) -> "CreatePoolEvent":
        return cls(
                timestamp=obj["timestamp"],
                index=obj["index"],
                creator=SolPubkey.from_string(obj["creator"]),
                baseMint=SolPubkey.from_string(obj["baseMint"]),
                quoteMint=SolPubkey.from_string(obj["quoteMint"]),
                baseMintDecimals=obj["baseMintDecimals"],
                quoteMintDecimals=obj["quoteMintDecimals"],
                baseAmountIn=obj["baseAmountIn"],
                quoteAmountIn=obj["quoteAmountIn"],
                poolBaseAmount=obj["poolBaseAmount"],
                poolQuoteAmount=obj["poolQuoteAmount"],
                minimumLiquidity=obj["minimumLiquidity"],
                initialLiquidity=obj["initialLiquidity"],
                lpTokenAmountOut=obj["lpTokenAmountOut"],
                poolBump=obj["poolBump"],
                pool=SolPubkey.from_string(obj["pool"]),
                lpMint=SolPubkey.from_string(obj["lpMint"]),
                userBaseTokenAccount=SolPubkey.from_string(obj["userBaseTokenAccount"]),
                userQuoteTokenAccount=SolPubkey.from_string(obj["userQuoteTokenAccount"]),
        )






