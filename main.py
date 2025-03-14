import os
from typing import List
from config import config
import utils

def setup_data_directory():
    """Create the data directory if it doesn't exist."""
    os.makedirs("data", exist_ok=True)

def faucet_operations():
    """Handle all faucet-related operations."""
    if not config.faucet.enabled:
        print("Faucet operations are disabled")
        return

    try:
        private_keys = utils.load_private_keys(config.wallet.private_keys_path)
        
        # Regular faucet claims
        for private_key in private_keys:
            if utils.get_faucet_tokens(private_key):
                print(f"Successfully claimed faucet tokens for {utils.get_account_from_private_key(private_key).address}")
            else:
                print(f"Failed to claim faucet tokens for {utils.get_account_from_private_key(private_key).address}")

        # Farm faucet operations
        if config.faucet.farm_faucet_enabled:
            farm_keys = utils.load_private_keys(config.wallet.keys_for_faucet_path)
            for private_key in farm_keys:
                if utils.get_faucet_tokens(private_key):
                    print(f"Successfully claimed farm faucet tokens for {utils.get_account_from_private_key(private_key).address}")
                else:
                    print(f"Failed to claim farm faucet tokens for {utils.get_account_from_private_key(private_key).address}")

        # Disperse operations
        if config.faucet.disperse_farm_accounts_enabled:
            # TODO: Implement disperse between farm accounts
            pass

        if config.faucet.disperse_from_one_wallet_enabled:
            # TODO: Implement disperse from one wallet
            pass

    except Exception as e:
        print(f"Error in faucet operations: {e}")

def dex_operations():
    """Handle all DEX-related operations."""
    if not config.dex.enabled:
        print("DEX operations are disabled")
        return

    try:
        private_keys = utils.load_private_keys(config.wallet.private_keys_path)
        
        # Collect all to MON
        if config.dex.collect_all_to_monad_enabled:
            for private_key in private_keys:
                if utils.collect_all_to_monad(private_key):
                    print(f"Successfully collected all tokens to MON for {utils.get_account_from_private_key(private_key).address}")
                else:
                    print(f"Failed to collect tokens to MON for {utils.get_account_from_private_key(private_key).address}")

        # DEX-specific operations
        if config.dex.bean_enabled:
            # TODO: Implement Bean DEX operations
            pass

        if config.dex.ambient_enabled:
            # TODO: Implement Ambient DEX operations
            pass

        if config.dex.izumi_enabled:
            # TODO: Implement Izumi DEX operations
            pass

    except Exception as e:
        print(f"Error in DEX operations: {e}")

def main():
    """Main entry point for the Monad Testnet Automation Tool."""
    print("Starting Monad Testnet Automation Tool...")
    
    # Setup
    setup_data_directory()
    
    # Get Monad testnet data
    testnet_data = utils.get_monad_testnet_page_data()
    if testnet_data:
        print("Successfully fetched Monad testnet data")
    else:
        print("Failed to fetch Monad testnet data")

    # Run operations
    print("\nStarting faucet operations...")
    faucet_operations()
    
    print("\nStarting DEX operations...")
    dex_operations()
    
    print("\nMonad Testnet Automation Tool completed!")

if __name__ == "__main__":
    main() 