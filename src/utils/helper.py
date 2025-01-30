import base64
import json
import logging
from solana.rpc.api import Client
from solana.rpc.types import TxOpts

def base64_encode(data):
    logger = logging.getLogger(__name__)
    logger.debug(f"Encoding data to base64: {data}")

    try:
        encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        logger.debug(f"Encoded data: {encoded_data}")
        return encoded_data
    except Exception as error:
        logger.error(f"Error encoding data to base64: {error}")
        return None

def base64_decode(encoded_data):
    logger = logging.getLogger(__name__)
    logger.debug(f"Decoding data from base64: {encoded_data}")

    try:
        decoded_data = base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')
        logger.debug(f"Decoded data: {decoded_data}")
        return decoded_data
    except Exception as error:
        logger.error(f"Error decoding data from base64: {error}")
        return None

def send_transaction(client, transaction, signers, opts=TxOpts(skip_confirmation=False)):
    logger = logging.getLogger(__name__)
    logger.debug(f"Sending transaction with signers: {signers}")

    try:
        transaction_result = client.send_transaction(transaction, *signers, opts=opts)
        logger.debug(f"Transaction sent: {transaction_result}")
        return transaction_result
    except Exception as error:
        logger.error(f"Error sending transaction: {error}")
        return None

def load_json_from_file(file_path):
    logger = logging.getLogger(__name__)
    logger.debug(f"Loading JSON from file: {file_path}")

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logger.debug(f"Loaded JSON data: {data}")
            return data
    except Exception as error:
        logger.error(f"Error loading JSON from file: {error}")
        return None

def save_json_to_file(data, file_path):
    logger = logging.getLogger(__name__)
    logger.debug(f"Saving JSON to file: {file_path}")

    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logger.debug(f"JSON data saved: {data}")
    except Exception as error:
        logger.error(f"Error saving JSON to file: {error}")