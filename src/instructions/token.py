import logging
from solana.transaction import Transaction
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.publickey import PublicKey
from spl.token.instructions import transfer_checked, TransferCheckedParams, initialize_account, InitializeAccountParams

class TokenInstructions:
    def __init__(self, solana_client_url):
        self._client = Client(solana_client_url)
        self._logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.info("TokenInstructions initialized")
        return logger
from solana.transaction import TransactionInstruction
from solana.publickey import PublicKey
from spl.token.instructions import (
    initialize_account,
    InitializeAccountParams,
    transfer_checked,
    TransferCheckedParams,
    mint_to_checked,
    MintToCheckedParams,
    approve_checked,
    ApproveCheckedParams
)
import logging

def create_initialize_token_account_instruction(account_pubkey, mint_pubkey, owner_pubkey):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating initialize token account instruction for account {account_pubkey}")

    try:
        instruction = initialize_account(
            InitializeAccountParams(
                account=PublicKey(account_pubkey),
                mint=PublicKey(mint_pubkey),
                owner=PublicKey(owner_pubkey)
            )
        )
        logger.debug(f"Initialize token account instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating initialize token account instruction: {error}")
        return None

def create_transfer_token_instruction(source_pubkey, dest_pubkey, owner_pubkey, amount, mint_pubkey, decimals):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating transfer token instruction from {source_pubkey} to {dest_pubkey} for {amount} tokens")

    try:
        instruction = transfer_checked(
            TransferCheckedParams(
                source=PublicKey(source_pubkey),
                dest=PublicKey(dest_pubkey),
                owner=PublicKey(owner_pubkey),
                amount=amount,
                mint=PublicKey(mint_pubkey),
                decimals=decimals
            )
        )
        logger.debug(f"Transfer token instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating transfer token instruction: {error}")
        return None

def create_mint_to_instruction(mint_pubkey, dest_pubkey, mint_authority_pubkey, amount, decimals):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating mint to instruction for mint {mint_pubkey} to destination {dest_pubkey} for {amount} tokens")

    try:
        instruction = mint_to_checked(
            MintToCheckedParams(
                mint=PublicKey(mint_pubkey),
                dest=PublicKey(dest_pubkey),
                mint_authority=PublicKey(mint_authority_pubkey),
                amount=amount,
                decimals=decimals
            )
        )
        logger.debug(f"Mint to instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating mint to instruction: {error}")
        return None

def create_approve_instruction(source_pubkey, delegate_pubkey, owner_pubkey, amount, mint_pubkey, decimals):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating approve instruction for source {source_pubkey} to delegate {delegate_pubkey} for {amount} tokens")

    try:
        instruction = approve_checked(
            ApproveCheckedParams(
                source=PublicKey(source_pubkey),
                delegate=PublicKey(delegate_pubkey),
                owner=PublicKey(owner_pubkey),
                amount=amount,
                mint=PublicKey(mint_pubkey),
                decimals=decimals
            )
        )
        logger.debug(f"Approve instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating approve instruction: {error}")
        return None
    def transfer_tokens(self, sender_private_key, recipient_address, amount, token_mint_address, decimals):
        self._logger.debug(f"Preparing to transfer {amount} tokens from {sender_private_key} to {recipient_address}")
        try:
            sender = PublicKey(sender_private_key)
            recipient = PublicKey(recipient_address)
            mint = PublicKey(token_mint_address)

            transaction = Transaction().add(
                transfer_checked(
                    TransferCheckedParams(
                        program_id=PublicKey("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"),  # SPL Token Program ID
                        source=sender,
                        mint=mint,
                        dest=recipient,
                        owner=sender,
                        amount=int(amount * (10 ** decimals)),
                        decimals=decimals
                    )
                )
            )

            self._logger.debug("Token transfer transaction created, sending transaction...")
            response = self._client.send_transaction(transaction, sender_private_key, opts=TxOpts(skip_confirmation=False))
            self._logger.debug(f"Token transfer transaction response: {response}")
            return response
        except Exception as error:
            self._logger.error(f"Error transferring tokens: {error}")
            return None

    def initialize_token_account(self, payer_private_key, new_account_address, token_mint_address):
        self._logger.debug(f"Initializing token account {new_account_address} for mint {token_mint_address}")
        try:
            payer = PublicKey(payer_private_key)
            new_account = PublicKey(new_account_address)
            mint = PublicKey(token_mint_address)

            transaction = Transaction().add(
                initialize_account(
                    InitializeAccountParams(
                        program_id=PublicKey("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"),  # SPL Token Program ID
                        account=new_account,
                        mint=mint,
                        owner=payer
                    )
                )
            )

            self._logger.debug("Token account initialization transaction created, sending transaction...")
            response = self._client.send_transaction(transaction, payer_private_key, opts=TxOpts(skip_confirmation=False))
            self._logger.debug(f"Token account initialization transaction response: {response}")
            return response
        except Exception as error:
            self._logger.error(f"Error initializing token account: {error}")
            return None