import logging
from solana.rpc.api import Client
from solana.transaction import Transaction
from src.parser.parser import parse_input
from src.parser.deepseek import analyze_with_deepseek
from src.parser.mappings import map_to_instructions
from src.instructions.system import create_transfer_sol_instruction
from src.instructions.token import create_transfer_token_instruction
from src.instructions.staking import create_stake_account_instruction
from src.instructions.nft import create_mint_nft_instruction
from src.instructions.raydium import create_swap_instruction
from src.instructions.pumpfun import create_pumpfun_composite_instruction
from src.utils.helper import send_transaction
from src.utils.security import load_private_key_from_env, sign_transaction, send_signed_transaction

class PersephAI:
    def __init__(self, deepseek_api_key, solana_private_key_env_var):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Initializing PersephAI instance")
        self.deepseek_api_key = deepseek_api_key
        self.keypair = load_private_key_from_env(solana_private_key_env_var)
        self.client = Client("https://api.mainnet-beta.solana.com")

    def process_input(self, input_string):
        self.logger.debug(f"Processing input: {input_string}")
        parsed_data = parse_input(input_string)
        deepseek_response = analyze_with_deepseek(parsed_data, self.deepseek_api_key)
        instructions_data = map_to_instructions(deepseek_response)
        return instructions_data

    def construct_transaction(self, instructions_data):
        self.logger.debug("Constructing transaction")
        transaction = Transaction()
        for instruction_data in instructions_data:
            if instruction_data['type'] == 'transfer_sol':
                instruction = create_transfer_sol_instruction(
                    instruction_data['sender'], 
                    instruction_data['recipient'], 
                    instruction_data['lamports']
                )
            elif instruction_data['type'] == 'transfer_token':
                instruction = create_transfer_token_instruction(
                    instruction_data['source'], 
                    instruction_data['destination'], 
                    self.keypair.public_key, 
                    instruction_data['amount'], 
                    instruction_data['mint'], 
                    instruction_data['decimals']
                )
            elif instruction_data['type'] == 'stake':
                instruction = create_stake_account_instruction(
                    instruction_data['stake_account'], 
                    self.keypair.public_key, 
                    instruction_data['lamports']
                )
            elif instruction_data['type'] == 'mint_nft':
                instruction = create_mint_nft_instruction(
                    instruction_data['mint'], 
                    instruction_data['destination'], 
                    self.keypair.public_key, 
                    instruction_data['metadata'], 
                    instruction_data['master_edition']
                )
            elif instruction_data['type'] == 'swap':
                instruction = create_swap_instruction(
                    self.keypair.public_key, 
                    instruction_data['pool'], 
                    instruction_data['from_token'], 
                    instruction_data['to_token'], 
                    instruction_data['amount_in'], 
                    instruction_data['min_amount_out']
                )
            elif instruction_data['type'] == 'pumpfun':
                instruction = create_pumpfun_composite_instruction(
                    self.keypair.public_key, 
                    instruction_data['pump_program'], 
                    instruction_data['fun_program'], 
                    instruction_data['pump_data'], 
                    instruction_data['fun_data']
                )
            else:
                self.logger.error(f"Unknown instruction type: {instruction_data['type']}")
                continue

            if instruction:
                transaction.add(instruction)

        return transaction

    def execute_transaction(self, transaction):
        self.logger.debug("Executing transaction")
        signed_transaction = sign_transaction(transaction, self.keypair)
        if signed_transaction:
            result = send_signed_transaction(self.client, signed_transaction)
            self.logger.debug(f"Transaction result: {result}")
            return result
        else:
            self.logger.error("Failed to sign transaction")
            return None

    def run(self, input_string):
        instructions_data = self.process_input(input_string)
        transaction = self.construct_transaction(instructions_data)
        return self.execute_transaction(transaction)