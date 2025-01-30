import logging
from ollama import Client
from .mappings import map_deepseek_response_to_instructions

class DeepSeekInterface:
    def __init__(self, api_key):
        self._api_client = self._initialize_client(api_key)
        self._logger = self._setup_logger()

    def _initialize_client(self, api_key):
        return Client(
            host='https://api.deepseek.com/v1',
            headers={'Authorization': f'Bearer {api_key}'}
        )

    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.info("DeepSeekInterface initialized")
        return logger

    def extract_instructions(self, input_text, context_info):
        self._logger.debug(f"Extracting instructions from input: {input_text} with context: {context_info}")
        try:
            response = self._api_client.chat(
                model='deepseek-reasoner',
                messages=[
                    {'role': 'user', 'content': input_text},
                    {'role': 'system', 'content': f"Context: {context_info}"}
                ]
            )
            raw_instructions = response.get('choices', [{}])[0].get('message', {}).get('content', '')
            self._logger.debug(f"Raw instructions: {raw_instructions}")
            instructions = map_deepseek_response_to_instructions(raw_instructions)
            self._logger.debug(f"Mapped instructions: {instructions}")
            return instructions
        except Exception as error:
            self._logger.error(f"Error extracting instructions: {error}")
            return []

    def enhance_communication(self, message, context_details):
        self._logger.debug(f"Enhancing communication for message: {message} with context: {context_details}")
        try:
            response = self._api_client.chat(
                model='deepseek-reasoner',
                messages=[
                    {'role': 'user', 'content': message},
                    {'role': 'system', 'content': f"Context: {context_details}"}
                ]
            )
            enhanced_content = response.get('choices', [{}])[0].get('message', {}).get('content', '')
            self._logger.debug(f"Enhanced communication result: {enhanced_content}")
            return enhanced_content
        except Exception as error:
            self._logger.error(f"Error enhancing communication: {error}")
            return ""