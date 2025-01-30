import logging
from .deepseek import DeepSeekInterface
from .mappings import map_deepseek_response_to_instructions

class InstructionParser:
    def __init__(self, api_key):
        self._deepseek_interface = DeepSeekInterface(api_key)
        self._logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.info("InstructionParser initialized")
        return logger

    def parse_input(self, input_text, context_info):
        self._logger.debug(f"Parsing input: {input_text} with context: {context_info}")
        try:
            raw_instructions = self._deepseek_interface.extract_instructions(input_text, context_info)
            self._logger.debug(f"Raw instructions received: {raw_instructions}")
            instructions = map_deepseek_response_to_instructions(raw_instructions)
            self._logger.debug(f"Parsed instructions: {instructions}")
            return instructions
        except Exception as error:
            self._logger.error(f"Error parsing input: {error}")
            return []

    def process_and_map(self, input_text, context_info):
        self._logger.debug(f"Processing and mapping input: {input_text} with context: {context_info}")
        instructions = self.parse_input(input_text, context_info)
        self._logger.debug(f"Processed and mapped instructions: {instructions}")
        return instructions