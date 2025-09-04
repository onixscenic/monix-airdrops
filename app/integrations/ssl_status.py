import requests

def check_ssl_status(url: str) -> dict:
    try:
        response = requests.get(url, timeout=5)
        ssl_enabled = url.startswith("https://") and response.status_code == 200
        return {
            "url": url,
            "ssl_enabled": ssl_enabled,
            "status_code": response.status_code,
            "message": "SSL is enabled and reachable!" if ssl_enabled else "SSL check failed."
        }
    except Exception as e:
        return {
            "url": url,
            "ssl_enabled": False,
            "status_code": None,
            "message": f"SSL check error: {str(e)}"
        }