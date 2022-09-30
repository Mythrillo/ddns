import os

from requests import get


def get_ip() -> str:
    try:
        ip = get('https://api.ipify.org').text
        print(f"Current ip: {ip}")
    except Exception as e:
        print(f"Couldn't get the ip for some reason: {e}")


def update_duck_dns_ip(domain: str):
    token = os.getenv("DUCK_TOKEN")
    ip = get_ip()
    url = f"https://www.duckdns.org/update?domains={domain}&token={token}[&ip={ip}][&verbose=true][&clear=true]"
    response = get(url)
    print(response.reason)


if __name__ == "__main__":
    domain = os.getenv("DUCK_DOMAIN")
    update_duck_dns_ip(domain)
