import os

# Change these to customize API details
API_KEY = os.getenv("API_KEY", "YOUR_SUPER_SECRET_KEY")
AUTH_TYPE = os.getenv("AUTH_TYPE", "api_key")  # 'api_key', 'jwt', 'oauth2'
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

# External APIs (customize as needed)
DEBANK_AIRDROP_API = "https://openapi.debank.com/v1/user/airdrop?user_addr={wallet}"
COINGECKO_SWAP_API = "https://api.coingecko.com/api/v3/simple/price?ids={from_coin},{to_coin}&vs_currencies={to_currency}"
CURRENCY_EXCHANGE_API = "https://api.exchangerate-api.com/v4/latest/{base_currency}"