from fastapi import FastAPI, Query
from app.integrations.ssl_status import check_ssl_status

app = FastAPI()

@app.get("/ssl-check")
def ssl_check(url: str = Query(..., description="URL to check SSL status")):
    """
    Demo endpoint to check SSL status of a given URL.
    Usage: /ssl-check?url=https://your-app.onrender.com
    """
    result = check_ssl_status(url)
    return result
