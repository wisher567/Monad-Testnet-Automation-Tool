from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class NetworkConfig:
    rpc_url: str = "https://rpc.testnet.monad.xyz"  # Monad testnet RPC
    chain_id: int = 1337  # Monad testnet chain ID

@dataclass
class FaucetConfig:
    enabled: bool = True
    farm_faucet_enabled: bool = True
    disperse_farm_accounts_enabled: bool = True
    disperse_from_one_wallet_enabled: bool = True

@dataclass
class DEXConfig:
    enabled: bool = True
    collect_all_to_monad_enabled: bool = True
    swaps_enabled: bool = True
    bean_enabled: bool = True
    ambient_enabled: bool = True
    izumi_enabled: bool = True

@dataclass
class WalletConfig:
    keys_for_faucet_path: str = "data/keys_for_faucet.txt"
    private_keys_path: str = "data/private_keys.txt"

@dataclass
class DEXAddresses:
    bean: str = "0x..."  # Bean DEX contract address
    ambient: str = "0x..."  # Ambient DEX contract address
    izumi: str = "0x..."  # Izumi DEX contract address

@dataclass
class Config:
    network: NetworkConfig = NetworkConfig()
    faucet: FaucetConfig = FaucetConfig()
    dex: DEXConfig = DEXConfig()
    wallet: WalletConfig = WalletConfig()
    dex_addresses: DEXAddresses = DEXAddresses()

# Global configuration instance
config = Config() 