from fastapi import FastAPI, Query, Depends, Request
import requests, os
from app.integrations.ssl_status import check_ssl_status
from app.config import SENDGRID_API_KEY, GITHUB_TOKEN, DEBANK_AIRDROP_API, COINGECKO_SWAP_API, CURRENCY_EXCHANGE_API
from app.auth import get_auth

app = FastAPI()

@app.get("/ssl-check")
def ssl_check(url: str = Query(...), request: Request = None, auth=Depends(get_auth)):
    return check_ssl_status(url)

@app.get("/github-stats")
def github_stats(repo: str = Query(...), request: Request = None, auth=Depends(get_auth)):
    stats_url = f"https://api.github.com/repos/{repo}"
    issues_url = f"https://api.github.com/repos/{repo}/issues"
    prs_url = f"https://api.github.com/repos/{repo}/pulls"
    repo_data = requests.get(stats_url).json()
    issues = requests.get(issues_url).json()
    prs = requests.get(prs_url).json()
    return {
        "stars": repo_data.get("stargazers_count"),
        "forks": repo_data.get("forks_count"),
        "open_issues": len([i for i in issues if 'pull_request' not in i]),
        "open_prs": len(prs),
    }

@app.get("/airdrop-status")
def airdrop_status(wallet: str = Query(...), request: Request = None, auth=Depends(get_auth)):
    url = DEBANK_AIRDROP_API.format(wallet=wallet)
    resp = requests.get(url)
    data = resp.json() if resp.status_code == 200 else {}
    eligibility = data.get("eligible", "Unknown")
    return {"wallet": wallet, "eligible": eligibility}

@app.post("/register-webhook")
def register_webhook(repo: str = Query(...), webhook_url: str = Query(...), request: Request = None, auth=Depends(get_auth)):
    api_url = f"https://api.github.com/repos/{repo}/hooks"
    payload = {"name": "web", "active": True, "events": ["push"], "config": {"url": webhook_url, "content_type": "json"}}
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.post(api_url, json=payload, headers=headers)
    return resp.json() if resp.status_code in [200, 201] else {"error": resp.text}

@app.post("/send-email")
def send_email(email: str = Query(...), request: Request = None, auth=Depends(get_auth)):
    SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"
    payload = {
        "personalizations": [{"to": [{"email": email}], "subject": "Test Notification"}],
        "from": {"email": "no-reply@your-app.com"},
        "content": [{"type": "text/plain", "value": "This is a test notification from your dashboard."}]
    }
    headers = {"Authorization": f"Bearer {SENDGRID_API_KEY}", "Content-Type": "application/json"}
    resp = requests.post(SENDGRID_URL, json=payload, headers=headers)
    return {"message": "Test email sent!"} if resp.status_code in [200, 202] else {"error": resp.text}

# --- Crypto Swap Coins ---
@app.get("/crypto-swap")
def crypto_swap(from_coin: str = Query(...), to_coin: str = Query(...), to_currency: str = Query("usd"), request: Request = None, auth=Depends(get_auth)):
    url = COINGECKO_SWAP_API.format(from_coin=from_coin, to_coin=to_coin, to_currency=to_currency)
    resp = requests.get(url)
    data = resp.json() if resp.status_code == 200 else {}
    swap_price = {
        f"{from_coin}_to_{to_currency}": data.get(from_coin, {}).get(to_currency),
        f"{to_coin}_to_{to_currency}": data.get(to_coin, {}).get(to_currency),
    }
    return swap_price

# --- Currency Exchange ---
@app.get("/currency-exchange")
def currency_exchange(base_currency: str = Query(...), target_currency: str = Query(...), request: Request = None, auth=Depends(get_auth)):
    url = CURRENCY_EXCHANGE_API.format(base_currency=base_currency)
    resp = requests.get(url)
    data = resp.json() if resp.status_code == 200 else {}
    rate = data.get("rates", {}).get(target_currency)
    return {"base_currency": base_currency, "target_currency": target_currency, "rate": rate}