# Monad Testnet Automation Tool

A Python-based automation tool for interacting with the Monad testnet, including faucet claims and DEX operations.

## ⚠️ Security Warning

This tool involves handling private keys. **NEVER** store private keys in plain text files in a production environment.

## Features

- Faucet Operations:
  - Claim tokens from the Monad testnet faucet
  - Farm faucet claims across multiple accounts
  - Disperse tokens between farm accounts
  - Disperse tokens from a single wallet to multiple addresses

- DEX Operations:
  - Collect all tokens to MON
  - Perform token swaps
  - Interact with multiple DEXes:
    - Bean DEX
    - Ambient DEX
    - Izumi DEX

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for version control)

## Installation

1. Clone the repository (optional):
```bash
git clone <repository-url>
cd monad-testnet-automation
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit the `.env` file with your settings:
```env
# Network Configuration
RPC_URL=https://rpc.testnet.monad.xyz
CHAIN_ID=1337

# Contract Addresses
FAUCET_CONTRACT=0x...  # Add actual faucet contract address
MON_TOKEN_CONTRACT=0x...  # Add actual MON token contract address
BEAN_DEX_CONTRACT=0x...  # Add actual Bean DEX contract address
AMBIENT_DEX_CONTRACT=0x...  # Add actual Ambient DEX contract address
IZUMI_DEX_CONTRACT=0x...  # Add actual Izumi DEX contract address

# Private Keys (DO NOT COMMIT ACTUAL KEYS)
PRIVATE_KEY=your_private_key_here
FARM_PRIVATE_KEY=your_farm_private_key_here

# Transaction Settings
MAX_SLIPPAGE=0.01
GAS_LIMIT=300000
MIN_AMOUNT=1000000000000000

# Security Settings
MAX_TRANSACTION_AMOUNT=1000000000000000000
```

3. Create the data directory:
```bash
mkdir data
```

## Running the Tool

1. Basic usage:
```bash
python main.py
```

2. The tool will:
   - Validate your private keys
   - Check network connectivity
   - Perform faucet operations
   - Execute DEX operations
   - Log all activities

3. Monitor the logs:
   - Console output shows real-time progress
   - Detailed logs are saved to `monad_automation.log`

## Project Structure

```
monad_automation_tool/
├── main.py           # Main script
├── config.py         # Configuration file
├── utils.py          # Helper functions
├── .env              # Environment variables (create from .env.example)
├── .env.example      # Example environment file
├── data/             # Data directory
│   ├── keys_for_faucet.txt  # Farm account private keys
│   └── private_keys.txt     # Main account private keys
├── requirements.txt  # Python dependencies
└── monad_automation.log  # Log file (created on run)
```

## Security Considerations

- Private keys are stored in environment variables
- Never commit your `.env` file or private keys
- Use virtual environments to isolate dependencies
- Monitor transaction limits and gas prices
- Keep your Python packages updated

## Troubleshooting

1. If you get "Invalid private key" errors:
   - Check your private key format in `.env`
   - Ensure there are no extra spaces or newlines
   - Verify the key is correct

2. If transactions fail:
   - Check your network connection
   - Verify you have enough gas
   - Check the logs for detailed error messages

3. If faucet claims fail:
   - Verify the faucet contract address
   - Check if you've already claimed
   - Wait for the cooldown period

## Disclaimer

This tool is for testing purposes only. Use at your own risk. Never use this tool with real funds or on mainnet.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
