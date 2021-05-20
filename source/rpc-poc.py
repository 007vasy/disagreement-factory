import requests
import json


def main():
    url = "http://127.0.0.1:8549/jsonrpc"

    # Example echo method
    payload = {
        "method": "eth_accounts",
        # "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, json=payload).json()
    print(response)
    # assert response["result"] == "echome!"
    # assert response["jsonrpc"]
    # assert response["id"] == 0

if __name__ == "__main__":
    main()