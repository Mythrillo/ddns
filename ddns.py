import logging
import os

from requests import get

logger = logging.getLogger("ddns")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("ddns.log")
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)



def get_ip() -> str:
    try:
        ip = get('https://api.ipify.org').text
        logger.info(f"Current ip: {ip}")
    except Exception as e:
        logger.error(f"Couldn't get the ip for some reason: {e}")


def update_duck_dns_ip(domain: str):
    token = os.getenv("DUCK_TOKEN")
    ip = get_ip()
    url = f"https://www.duckdns.org/update?domains={domain}&token={token}[&ip={ip}][&verbose=true][&clear=true]"
    response = get(url)
    logger.info(response.reason)


if __name__ == "__main__":
    domain = os.getenv("DUCK_DOMAIN")
    update_duck_dns_ip(domain)
