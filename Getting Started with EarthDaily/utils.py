import requests

def get_new_token(session, token_url):
    """Obtain a new authentication token using client credentials."""
    try:
        token_response = session.post(
            token_url,
            data={"grant_type": "client_credentials"}
        )
        token_response.raise_for_status()
        tokens = token_response.json()
        return tokens["access_token"]
    except requests.exceptions.RequestException as e:
        print(f"Failed to obtain token: {e}")
        return