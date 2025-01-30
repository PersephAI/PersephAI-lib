from solana.transaction import TransactionInstruction
from solana.publickey import PublicKey
from metaplex.instructions import (
    create_metadata_account,
    CreateMetadataAccountParams,
    update_metadata_account,
    UpdateMetadataAccountParams,
    mint_nft,
    MintNFTParams,
    transfer_nft,
    TransferNFTParams
)
import logging

def create_metadata_instruction(metadata_pubkey, mint_pubkey, mint_authority_pubkey, update_authority_pubkey, metadata_data):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating metadata instruction for NFT with mint {mint_pubkey}")

    try:
        instruction = create_metadata_account(
            CreateMetadataAccountParams(
                metadata=PublicKey(metadata_pubkey),
                mint=PublicKey(mint_pubkey),
                mint_authority=PublicKey(mint_authority_pubkey),
                update_authority=PublicKey(update_authority_pubkey),
                data=metadata_data
            )
        )
        logger.debug(f"Metadata instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating metadata instruction: {error}")
        return None

def create_update_metadata_instruction(metadata_pubkey, update_authority_pubkey, new_metadata_data):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating update metadata instruction for metadata {metadata_pubkey}")

    try:
        instruction = update_metadata_account(
            UpdateMetadataAccountParams(
                metadata=PublicKey(metadata_pubkey),
                update_authority=PublicKey(update_authority_pubkey),
                data=new_metadata_data
            )
        )
        logger.debug(f"Update metadata instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating update metadata instruction: {error}")
        return None

def create_mint_nft_instruction(mint_pubkey, destination_pubkey, mint_authority_pubkey, metadata_pubkey, master_edition_pubkey):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating mint NFT instruction for mint {mint_pubkey}")

    try:
        instruction = mint_nft(
            MintNFTParams(
                mint=PublicKey(mint_pubkey),
                destination=PublicKey(destination_pubkey),
                mint_authority=PublicKey(mint_authority_pubkey),
                metadata=PublicKey(metadata_pubkey),
                master_edition=PublicKey(master_edition_pubkey)
            )
        )
        logger.debug(f"Mint NFT instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating mint NFT instruction: {error}")
        return None

def create_transfer_nft_instruction(nft_pubkey, source_pubkey, destination_pubkey, owner_pubkey):
    logger = logging.getLogger(__name__)
    logger.debug(f"Creating transfer NFT instruction for NFT {nft_pubkey}")

    try:
        instruction = transfer_nft(
            TransferNFTParams(
                nft=PublicKey(nft_pubkey),
                source=PublicKey(source_pubkey),
                destination=PublicKey(destination_pubkey),
                owner=PublicKey(owner_pubkey)
            )
        )
        logger.debug(f"Transfer NFT instruction created: {instruction}")
        return instruction
    except Exception as error:
        logger.error(f"Error creating transfer NFT instruction: {error}")
        return None