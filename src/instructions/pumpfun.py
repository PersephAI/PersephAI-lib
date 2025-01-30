from solana.transaction import TransactionInstruction
from solana.publickey import PublicKey
import logging

def create_pump_action_instruction(user_pubkey, pump_program_pubkey, action_data):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating pump action instruction for user {user_pubkey}")

    try:
        instruction = TransactionInstruction(
            program_id=PublicKey(pump_program_pubkey),
            keys=[
                {"pubkey": PublicKey(user_pubkey), "is_signer": True, "is_writable": True}
            ],
            data=action_data
        )
        logger.debug(f"Pump action instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating pump action instruction: {error}")
        return None

def create_fun_action_instruction(user_pubkey, fun_program_pubkey, action_data):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating fun action instruction for user {user_pubkey}")

    try:
        instruction = TransactionInstruction(
            program_id=PublicKey(fun_program_pubkey),
            keys=[
                {"pubkey": PublicKey(user_pubkey), "is_signer": True, "is_writable": True}
            ],
            data=action_data
        )
        logger.debug(f"Fun action instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating fun action instruction: {error}")
        return None

def create_pumpfun_composite_instruction(user_pubkey, pump_program_pubkey, fun_program_pubkey, pump_data, fun_data):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating pumpfun composite instruction for user {user_pubkey}")

    try:
        pump_instruction = create_pump_action_instruction(user_pubkey, pump_program_pubkey, pump_data)
        fun_instruction = create_fun_action_instruction(user_pubkey, fun_program_pubkey, fun_data)
        logger.debug(f"Pumpfun composite instructions created: {[pump_instruction, fun_instruction]}")
        return [pump_instruction, fun_instruction]
    except Exception as error:
        logger.error(f"Error creating pumpfun composite instruction: {error}")
        return []