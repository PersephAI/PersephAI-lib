![PersephAI-lib](persephai_ban.png)

# README.md

# PersephAI Library

## Overview

The PersephAI library is a sophisticated software interface designed to seamlessly convert natural language instructions into executable transactions on the Solana blockchain. It acts as a bridge between human users, AI agents, and the decentralized ecosystem, leveraging the DeepSeek API to intelligently interpret, process, and map user inputs to precise blockchain operations.

By abstracting the complexities of blockchain transactions, PersephAI enables effortless execution of essential tasks, such as SOL transfers, token management, smart contract interactions, and other on-chain operations, through intuitive commands. This eliminates the need for in-depth knowledge of Solana’s architecture, making decentralized finance (DeFi) and blockchain applications more accessible to a wider audience.

Built with a modular and scalable Python-based architecture, the library ensures high flexibility and adaptability across various use cases. Developers can easily integrate PersephAI into their applications, whether for automated trading, AI-driven blockchain interactions, or user-friendly financial services. By simplifying transaction execution while maintaining security and efficiency, PersephAI stands as a powerful tool for bridging AI-driven automation and the decentralized economy.

## Features

- **Natural Language Processing**: Converts human-readable instructions into blockchain transactions.
- **DeepSeek API Integration**: Leverages the DeepSeek API for parsing and understanding input commands.
- **Comprehensive Instruction Set**: Supports a wide range of Solana blockchain operations, including token transfers, staking, NFT management, and more.
- **Security**: Implements robust security measures for handling private keys and executing transactions.
- **Modular Design**: Easily extendable with additional transaction types and functionalities.
- **AI Compatibility**: Designed to work seamlessly with AI agents for automated transaction processing.

## Installation

To install the PersephAI library, ensure you have Python 3.7 or later installed on your system. You can then clone the repository and install the required dependencies.

```bash
git clone https://github.com/persephai-lib/persephai-lib.git
cd persephai-lib
pip install -r requirements.txt
```

## Getting Started

To start using the PersephAI library, initialize a PersephAI instance with your DeepSeek API key and Solana private key. This setup prepares the instance for string parsing and transaction execution.

```python
from persephai import PersephAI

api_key = "your_deepseek_api_key"
private_key = "your_solana_private_key"

persephai = PersephAI(api_key, private_key)
```

## Modules

### PersephAI Module

- **persephai.py**: The main entry point for the PersephAI class, responsible for initializing and managing the transaction process.

### Parser Module

- **deepseek.py**: Handles interaction with the DeepSeek API to analyze input strings.
- **mappings.py**: Maps parsed data to specific instructions.
- **parser.py**: Contains the main parser logic for processing input strings.

### Instructions Module

- **system.py**: Contains system account instructions, such as sending SOL.
- **token.py**: Manages token-related instructions.
- **staking.py**: Handles staking-related instructions.
- **nft.py**: Manages NFT-related instructions.
- **governance.py**: Contains governance-related instructions.
- **lending.py**: Handles lending and borrowing instructions.
- **raydium.py**: Manages Raydium-specific transactions.
- **pumpfun.py**: Handles Pumpfun-specific transactions.

### Utils Module

- **security.py**: Provides utilities for handling private keys and ensuring transaction security.
- **helper.py**: Contains general utility functions used throughout the library.

## Usage

Once the PersephAI instance is initialized, you can use it to process natural language commands and execute transactions on the Solana blockchain. The library will handle parsing, mapping, and constructing the necessary transaction instructions.

```python
command = "Transfer 10 SOL to address XYZ"
transaction_function = persephai.generate(command)

# Execute the transaction
transaction_function()
```

## Security

The PersephAI library prioritizes security, especially when handling private keys and executing transactions. The `security.py` module includes utilities to ensure that private keys are managed securely, preventing unauthorized access and ensuring safe transaction execution.

## Contributing

Contributions to the PersephAI library are welcome. If you have ideas for new features or improvements, please submit a pull request or open an issue on the GitHub repository.

## License

The PersephAI library is open-source software licensed under the MIT License. See the LICENSE file for more details.

## Contact

For questions, feedback, or support, please contact the project maintainer at [contact@persephai.ai].

## Acknowledgments

We would like to thank the developers and contributors of the Solana blockchain and the DeepSeek API for their invaluable tools and resources that made this project possible.
