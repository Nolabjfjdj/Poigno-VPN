import ipaddress
import json
import urllib.error
import urllib.request


IP_CHECK_URL = "https://api.ipify.org?format=json"


def get_public_ip():
    request = urllib.request.Request(
        IP_CHECK_URL,
        headers={"User-Agent": "Poigno-VPN-IP-Check/0.1"},
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        payload = json.loads(response.read().decode("utf-8"))

    address = payload.get("ip")
    if not isinstance(address, str):
        raise ValueError("The IP check service returned an invalid response.")

    return str(ipaddress.ip_address(address))


def main():
    try:
        print(f"Public IP: {get_public_ip()}")
    except (urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(f"Could not determine public IP: {error}") from error


if __name__ == "__main__":
    main()
