# Sample API Requests for monix-airdrops

## Authentication
- If using **API Key**: Add header `X-API-Key: YOUR_SUPER_SECRET_KEY`
- If using **JWT**: Add header `Authorization: Bearer <your_jwt_token>`
- If using **OAuth2**: Add header `Authorization: Bearer <your_oauth2_token>`

---

## 1. SSL Status Check

**curl**
```sh
curl -X GET "https://your-domain.com/ssl-check?url=https://example.com" \
  -H "X-API-Key: YOUR_SUPER_SECRET_KEY"
```

## 2. GitHub Repo Stats

**curl**
```sh
curl -X GET "https://your-domain.com/github-stats?repo=onixscenic/monix-airdrops" \
  -H "X-API-Key: YOUR_SUPER_SECRET_KEY"
```

## 3. Crypto Airdrop Monitor

**curl**
```sh
curl -X GET "https://your-domain.com/airdrop-status?wallet=0xYourWalletAddress" \
  -H "X-API-Key: YOUR_SUPER_SECRET_KEY"
```

## 4. Register Webhook

**curl**
```sh
curl -X POST "https://your-domain.com/register-webhook?repo=onixscenic/monix-airdrops&webhook_url=https://your-webhook-endpoint.com" \
  -H "X-API-Key: YOUR_SUPER_SECRET_KEY"
```

## 5. Send Email Notification

**curl**
```sh
curl -X POST "https://your-domain.com/send-email?email=you@example.com" \
  -H "X-API-Key: YOUR_SUPER_SECRET_KEY"
```

## 6. Crypto Swap

**curl**
```sh
curl -X GET "https://your-domain.com/crypto-swap?from_coin=bitcoin&to_coin=ethereum&to_currency=usd" \
  -H "X-API-Key: YOUR_SUPER_SECRET_KEY"
```

## 7. Currency Exchange

**curl**
```sh
curl -X GET "https://your-domain.com/currency-exchange?base_currency=USD&target_currency=EUR" \
  -H "X-API-Key: YOUR_SUPER_SECRET_KEY"
```

---

## Python Example (using requests)

```python
import requests

headers = {"X-API-Key": "YOUR_SUPER_SECRET_KEY"}

r = requests.get("https://your-domain.com/github-stats?repo=onixscenic/monix-airdrops", headers=headers)
print(r.json())
```
