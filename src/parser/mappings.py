import logging
import re

def map_deepseek_response_to_instructions(raw_instructions):
    logger = logging.getLogger(__name__)
    logger.debug(f"Mapping raw instructions: {raw_instructions}")

    instructions = []

    try:
        # Extract transfer SOL instructions
        transfer_matches = re.findall(r'transfer (\d+\.?\d*) SOL to (\w+)', raw_instructions)
        for amount, recipient in transfer_matches:
            instructions.append({
                'type': 'transfer',
                'asset': 'SOL',
                'amount': float(amount),
                'recipient': recipient
            })

        # Extract stake tokens instructions
        stake_matches = re.findall(r'stake (\d+\.?\d*) tokens with (\w+)', raw_instructions)
        for amount, validator in stake_matches:
            instructions.append({
                'type': 'stake',
                'asset': 'tokens',
                'amount': float(amount),
                'validator': validator
            })

        # Extract NFT-related instructions
        nft_transfer_matches = re.findall(r'transfer NFT (\w+) to (\w+)', raw_instructions)
        for nft_id, recipient in nft_transfer_matches:
            instructions.append({
                'type': 'nft_transfer',
                'nft_id': nft_id,
                'recipient': recipient
            })

        # Extract governance instructions
        governance_vote_matches = re.findall(r'vote (\w+) on proposal (\w+)', raw_instructions)
        for vote, proposal_id in governance_vote_matches:
            instructions.append({
                'type': 'governance_vote',
                'vote': vote,
                'proposal_id': proposal_id
            })

        # Extract lending instructions
        lending_borrow_matches = re.findall(r'borrow (\d+\.?\d*) (\w+) from (\w+)', raw_instructions)
        for amount, asset, platform in lending_borrow_matches:
            instructions.append({
                'type': 'borrow',
                'asset': asset,
                'amount': float(amount),
                'platform': platform
            })

        # Extract Raydium-specific transactions
        raydium_swap_matches = re.findall(r'swap (\d+\.?\d*) (\w+) for (\w+) on Raydium', raw_instructions)
        for amount, from_asset, to_asset in raydium_swap_matches:
            instructions.append({
                'type': 'raydium_swap',
                'from_asset': from_asset,
                'to_asset': to_asset,
                'amount': float(amount)
            })

        # Extract Pumpfun-specific transactions
        pumpfun_action_matches = re.findall(r'perform (\w+) action on Pumpfun', raw_instructions)
        for action in pumpfun_action_matches:
            instructions.append({
                'type': 'pumpfun_action',
                'action': action
            })

        logger.debug(f"Mapped instructions: {instructions}")

    except Exception as error:
        logger.error(f"Error mapping instructions: {error}")

    return instructions