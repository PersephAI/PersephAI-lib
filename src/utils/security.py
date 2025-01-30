from solana.keypair import Keypair
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from cryptography.fernet import Fernet
import logging
import base64
import os

def load_private_key_from_env(env_var_name):
    logger = logging.getLogger(__name__)
    logger.debug(f"Loading private key from environment variable: {env_var_name}")

    try:
        private_key_base64 = os.getenv(env_var_name)
        if not private_key_base64:
            raise ValueError(f"Environment variable {env_var_name} not set")
        private_key_bytes = base64.b64decode(private_key_base64)
        keypair = Keypair.from_secret_key(private_key_bytes)
        logger.debug(f"Loaded private key for public key: {keypair.public_key}")
        return keypair
    except Exception as error:
        logger.error(f"Error loading private key from environment: {error}")
        return None

def sign_transaction(transaction, keypair):
    logger = logging.getLogger(__name__)
    logger.debug(f"Signing transaction with keypair: {keypair.public_key}")

    try:
        transaction.sign(keypair)
        logger.debug("Transaction signed successfully")
        return transaction
    except Exception as error:
        logger.error(f"Error signing transaction: {error}")
        return None

def send_signed_transaction(client, transaction, opts=TxOpts(skip_confirmation=False)):
    logger = logging.getLogger(__name__)
    logger.debug("Sending signed transaction")

    try:
        transaction_result = client.send_transaction(transaction, opts=opts)
        logger.debug(f"Signed transaction sent: {transaction_result}")
        return transaction_result
    except Exception as error:
        logger.error(f"Error sending signed transaction: {error}")
        return None

def encrypt_data(data, key):
    logger = logging.getLogger(__name__)
    logger.debug("Encrypting data")

    try:
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode('utf-8'))
        logger.debug(f"Data encrypted: {encrypted_data}")
        return encrypted_data
    except Exception as error:
        logger.error(f"Error encrypting data: {error}")
        return None

def decrypt_data(encrypted_data, key):
    logger = logging.getLogger(__name__)
    logger.debug("Decrypting data")

    try:
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data).decode('utf-8')
        logger.debug(f"Data decrypted: {decrypted_data}")
        return decrypted_data
    except Exception as error:
        logger.error(f"Error decrypting data: {error}")
        return None