import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        num = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        headers = {
            "Authorization": "Bearer 1950e5745492fddb1ff701d92083320776aec7c97c026ea6a247c9bf9fc8a7af"
        }

        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", headers = headers)
        response.raise_for_status()
        content = response.json()
        currentPrice = float(content["data"]["priceUsd"])
    except (requests.RequestException, requests.HTTPError, ValueError, KeyError):
        sys.exit(1)

    print(f"${(num * currentPrice):,.4f}")

main()
