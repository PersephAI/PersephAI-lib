from solana.transaction import TransactionInstruction
from solana.publickey import PublicKey
from raydium.instructions import (
    swap,
    SwapParams,
    add_liquidity,
    AddLiquidityParams,
    remove_liquidity,
    RemoveLiquidityParams
)
import logging

def create_swap_instruction(user_pubkey, pool_pubkey, from_token_pubkey, to_token_pubkey, amount_in, min_amount_out):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating swap instruction on Raydium from {from_token_pubkey} to {to_token_pubkey} for amount {amount_in}")

    try:
        instruction = swap(
            SwapParams(
                user=PublicKey(user_pubkey),
                pool=PublicKey(pool_pubkey),
                from_token=PublicKey(from_token_pubkey),
                to_token=PublicKey(to_token_pubkey),
                amount_in=amount_in,
                min_amount_out=min_amount_out
            )
        )
        logger.debug(f"Swap instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating swap instruction: {error}")
        return None

def create_add_liquidity_instruction(user_pubkey, pool_pubkey, token_a_pubkey, token_b_pubkey, amount_a, amount_b):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating add liquidity instruction on Raydium for tokens {token_a_pubkey} and {token_b_pubkey}")

    try:
        instruction = add_liquidity(
            AddLiquidityParams(
                user=PublicKey(user_pubkey),
                pool=PublicKey(pool_pubkey),
                token_a=PublicKey(token_a_pubkey),
                token_b=PublicKey(token_b_pubkey),
                amount_a=amount_a,
                amount_b=amount_b
            )
        )
        logger.debug(f"Add liquidity instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating add liquidity instruction: {error}")
        return None

def create_remove_liquidity_instruction(user_pubkey, pool_pubkey, lp_token_pubkey, amount):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating remove liquidity instruction on Raydium for LP token {lp_token_pubkey}")

    try:
        instruction = remove_liquidity(
            RemoveLiquidityParams(
                user=PublicKey(user_pubkey),
                pool=PublicKey(pool_pubkey),
                lp_token=PublicKey(lp_token_pubkey),
                amount=amount
            )
        )
        logger.debug(f"Remove liquidity instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating remove liquidity instruction: {error}")
        return None

def create_stake_liquidity_instruction(user_pubkey, pool_pubkey, lp_token_pubkey, amount):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating stake liquidity instruction on Raydium for LP token {lp_token_pubkey}")

    try:
        instruction = TransactionInstruction(
            program_id=pool_pubkey,
            keys=[
                {"pubkey": PublicKey(user_pubkey), "is_signer": True, "is_writable": True},
                {"pubkey": PublicKey(lp_token_pubkey), "is_signer": False, "is_writable": True},
            ],
            data=b''
        )
        logger.debug(f"Stake liquidity instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating stake liquidity instruction: {error}")
        return None