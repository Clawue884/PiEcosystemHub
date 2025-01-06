"""
Pi Coin Configuration Constants
This module contains constants and configurations related to the Pi Coin cryptocurrency.
Optimized for scalability, security, and advanced features.
"""

from datetime import timedelta

# General Constants
PI_COIN_SYMBOL = "Pi"  # Symbol for Pi Coin
PI_COIN_NAME = "Pi Network Coin"  # Full name of the cryptocurrency
PI_COIN_VERSION = "1.0.0"  # Current version of the coin protocol
PI_COIN_DECIMALS = 18  # Number of decimal places for Pi Coin
PI_COIN_GENESIS_BLOCK_TIMESTAMP = "2025-01-01T00:00:00Z"  # Genesis block creation date (ISO 8601)

# Monetary Policy
PI_COIN_VALUE = 314_159  # Fixed value of Pi Coin in USD
PI_COIN_SUPPLY = 100_000_000_000  # Total supply of Pi Coin (in units)
PI_COIN_TRANSACTION_FEE = 0.01  # Fixed transaction fee per transaction (in USD)

# Mining and Consensus
PI_COIN_NETWORK_PROTOCOL = "Proof-of-Stake"  # Consensus mechanism
PI_COIN_MINING_DIFFICULTY = 1000  # Mining difficulty for block production
PI_COIN_MINING_REWARD = 12.5  # Reward for mining a block (in Pi Coin)
PI_COIN_BLOCK_TIME = timedelta(seconds=10)  # Average block time
PI_COIN_STAKING_MIN_AMOUNT = 100.0  # Minimum staking amount (in Pi Coin)
PI_COIN_STAKING_REWARD_RATE = 0.05  # Annual reward rate for staking (5%)

# Security Features
PI_COIN_ENCRYPTION_ALGORITHM = "AES-256-GCM"  # Advanced encryption standard with Galois/Counter Mode
PI_COIN_HASHING_ALGORITHM = "SHA3-256"  # Advanced hashing algorithm (quantum-safe)
PI_COIN_SIGNATURE_SCHEME = "EdDSA"  # Advanced digital signature scheme for transaction signing
PI_COIN_MULTI_SIG_SUPPORT = True  # Enable multi-signature for transactions
PI_COIN_ANTI_SYBIL_PROTOCOL = "Proof-of-Humanity"  # Mechanism to prevent Sybil attacks

# Network Parameters
PI_COIN_MAX_PEERS = 500  # Maximum number of peers in the network
PI_COIN_NODE_TIMEOUT = timedelta(seconds=30)  # Timeout for node responses
PI_COIN_CONNECTION_RETRY_INTERVAL = timedelta(seconds=5)  # Retry interval for failed connections
PI_COIN_MAX_TRANSACTION_SIZE = 2_000_000  # Maximum transaction size (in bytes)
PI_COIN_MAX_BLOCK_SIZE = 10_000_000  # Maximum block size (in bytes)

# API Configuration
PI_COIN_API_RATE_LIMIT = 10_000  # Maximum API requests per hour
PI_COIN_API_KEY_EXPIRATION = timedelta(hours=24)  # API key expiration time
PI_COIN_GRAPHQL_SUPPORT = True  # Enable GraphQL API

# Governance
PI_COIN_GOVERNANCE_MODEL = "Decentralized DAO"  # Governance model
PI_COIN_VOTING_WEIGHT_MULTIPLIER = 1.5  # Multiplier for long-term staking weight in governance
PI_COIN_PROPOSAL_THRESHOLD = 10_000  # Minimum Pi Coin required to submit a governance proposal

# Interoperability
PI_COIN_CROSS_CHAIN_SUPPORT = True  # Enable cross-chain interoperability
PI_COIN_SUPPORTED_NETWORKS = ["Ethereum", "Stellar", "Polygon", "Binance Smart Chain"]  # Compatible networks

# Regulatory Compliance
PI_COIN_KYC_REQUIRED = True  # KYC requirement for transactions
PI_COIN_COMPLIANCE_REGIONS = ["US", "EU", "UK", "SG"]  # Regions requiring compliance
PI_COIN_TAXATION_SUPPORT = True  # Enable automatic taxation compliance

# Advanced Features
PI_COIN_SMART_CONTRACT_SUPPORT = True  # Enable smart contract functionality
PI_COIN_DEFI_SUPPORT = True  # Enable decentralized finance capabilities
PI_COIN_NFT_SUPPORT = True  # Enable Non-Fungible Token capabilities
PI_COIN_AI_INTEGRATION = True  # Integration with AI for advanced analytics and automation
PI_COIN_QUANTUM_RESISTANCE = True  # Quantum-resistance enabled

# Debugging and Development
PI_COIN_DEBUG_MODE = False  # Enable/disable debug mode
PI_COIN_TESTNET_ENDPOINT = "https://testnet.pi-network.com"  # Testnet API endpoint
PI_COIN_MAINNET_ENDPOINT = "https://mainnet.pi-network.com"  # Mainnet API endpoint
PI_COIN_LOGGING_LEVEL = "INFO"  # Logging level: DEBUG, INFO, WARNING, ERROR

# Utility Constants
PI_COIN_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"  # Standard time format for timestamps
PI_COIN_MAX_RETRY_ATTEMPTS = 3  # Maximum retry attempts for operations
PI_COIN_NOTIFICATION_RETRY_INTERVAL = timedelta(seconds=15)  # Interval for retrying failed notifications
PI_COIN_DAPP_LIMIT_PER_ACCOUNT = 50  # Maximum number of DApps a single account can deploy
PI_COIN_TRANSACTION_REVERT_TIME = timedelta(minutes=10)  # Time window for reverting a transaction

# Reserved for Future Expansion
PI_COIN_RESERVED_FEATURES = {
    "QuantumComputingModule": False,  # Placeholder for future quantum computing module
    "ZeroKnowledgeProofs": True,  # Enable zero-knowledge proof for enhanced privacy
    "DynamicSupplyAdjustment": False,  # Placeholder for dynamic supply adjustment
}
