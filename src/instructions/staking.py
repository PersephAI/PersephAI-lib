from solana.transaction import TransactionInstruction
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from spl.stake_pool.instructions import (
    deposit_stake,
    DepositStakeParams,
    withdraw_stake,
    WithdrawStakeParams,
    create_stake_account,
    CreateStakeAccountParams
)
import logging

def create_stake_account_instruction(stake_account_pubkey, owner_pubkey, lamports):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating stake account instruction for stake account {stake_account_pubkey}")

    try:
        instruction = create_stake_account(
            CreateStakeAccountParams(
                stake_account=PublicKey(stake_account_pubkey),
                owner=PublicKey(owner_pubkey),
                lamports=lamports
            )
        )
        logger.debug(f"Stake account creation instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating stake account instruction: {error}")
        return None

def create_deposit_stake_instruction(stake_pool_pubkey, stake_account_pubkey, validator_pubkey, owner_pubkey, lamports):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating deposit stake instruction to pool {stake_pool_pubkey} from stake account {stake_account_pubkey}")

    try:
        instruction = deposit_stake(
            DepositStakeParams(
                stake_pool=PublicKey(stake_pool_pubkey),
                stake_account=PublicKey(stake_account_pubkey),
                validator=PublicKey(validator_pubkey),
                owner=PublicKey(owner_pubkey),
                lamports=lamports
            )
        )
        logger.debug(f"Deposit stake instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating deposit stake instruction: {error}")
        return None

def create_withdraw_stake_instruction(stake_pool_pubkey, stake_account_pubkey, owner_pubkey, lamports):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating withdraw stake instruction from pool {stake_pool_pubkey} to stake account {stake_account_pubkey}")

    try:
        instruction = withdraw_stake(
            WithdrawStakeParams(
                stake_pool=PublicKey(stake_pool_pubkey),
                stake_account=PublicKey(stake_account_pubkey),
                owner=PublicKey(owner_pubkey),
                lamports=lamports
            )
        )
        logger.debug(f"Withdraw stake instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating withdraw stake instruction: {error}")
        return None

def create_delegate_stake_instruction(stake_account_pubkey, validator_pubkey, owner_pubkey):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating delegate stake instruction for stake account {stake_account_pubkey} to validator {validator_pubkey}")

    try:
        instruction = TransactionInstruction(
            program_id=SYS_PROGRAM_ID,
            keys=[
                {"pubkey": PublicKey(stake_account_pubkey), "is_signer": True, "is_writable": True},
                {"pubkey": PublicKey(validator_pubkey), "is_signer": False, "is_writable": False},
                {"pubkey": PublicKey(owner_pubkey), "is_signer": True, "is_writable": False},
            ],
            data=b''
        )
        logger.debug(f"Delegate stake instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating delegate stake instruction: {error}")
        return None