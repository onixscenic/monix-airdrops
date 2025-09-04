# Monix Airdrops Backend

A modular FastAPI backend for SSL checks, GitHub stats, crypto airdrop status, webhook registration, email notifications, crypto swaps, currency exchange, and customizable authentication.

## Quick Start

1. **Clone/download** this folder.
2. **Install dependencies:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Set environment variables** in `.env` or your shell:
   - `API_KEY`, `SENDGRID_API_KEY`, `GITHUB_TOKEN`, etc.
   - `AUTH_TYPE=api_key` (or `jwt`, `oauth2`)
4. **Run the server:**
   ```sh
   uvicorn main:app --reload
   ```
5. **Call endpoints** (see API_SAMPLE_REQUESTS.md for examples).

## Future Modification

- Add new endpoints to `app/api.py` or modules in `app/integrations/`.
- Change authentication type in `app/config.py`.

## Example Endpoints

- `/ssl-check`
- `/github-stats`
- `/airdrop-status`
- `/register-webhook`
- `/send-email`
- `/crypto-swap`
- `/currency-exchange`
