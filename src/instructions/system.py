from solana.transaction import TransactionInstruction
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID, TransferParams, transfer
import logging

def create_transfer_sol_instruction(sender_pubkey, recipient_pubkey, lamports):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating transfer SOL instruction from {sender_pubkey} to {recipient_pubkey} for {lamports} lamports")

    try:
        instruction = transfer(
            TransferParams(
                from_pubkey=PublicKey(sender_pubkey),
                to_pubkey=PublicKey(recipient_pubkey),
                lamports=lamports
            )
        )
        logger.debug(f"Transfer SOL instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating transfer SOL instruction: {error}")
        return None

def create_account_instruction(new_account_pubkey, owner_pubkey, lamports, space):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating account instruction for new account {new_account_pubkey} with owner {owner_pubkey}")

    try:
        instruction = TransactionInstruction(
            program_id=SYS_PROGRAM_ID,
            keys=[
                {"pubkey": PublicKey(new_account_pubkey), "is_signer": True, "is_writable": True},
                {"pubkey": PublicKey(owner_pubkey), "is_signer": False, "is_writable": False},
            ],
            data=b''
        )
        logger.debug(f"Account creation instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating account instruction: {error}")
        return None