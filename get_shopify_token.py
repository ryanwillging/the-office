#!/usr/bin/env python3
"""
Shopify OAuth Token Generator
Gets an Admin API access token using your client credentials
"""

import os
import webbrowser
import requests
from urllib.parse import urlencode

from dotenv import load_dotenv

load_dotenv()

# Credentials come from .env (never hardcode them; this repo is public)
CLIENT_ID = os.environ["SHOPIFY_API_KEY"]
CLIENT_SECRET = os.environ["SHOPIFY_CLIENT_SECRET"]
SHOP = os.environ["SHOPIFY_STORE"]

# Scopes needed for product management
SCOPES = "write_products,read_products"

# Redirect URI - using a placeholder since we'll manually copy the code
REDIRECT_URI = "https://localhost/callback"

def get_authorization_url():
    """Generate the OAuth authorization URL"""
    params = {
        "client_id": CLIENT_ID,
        "scope": SCOPES,
        "redirect_uri": REDIRECT_URI,
    }
    return f"https://{SHOP}/admin/oauth/authorize?{urlencode(params)}"

def exchange_code_for_token(code):
    """Exchange authorization code for access token"""
    url = f"https://{SHOP}/admin/oauth/access_token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data.get("access_token")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def main():
    print("=" * 60)
    print("Shopify OAuth Token Generator")
    print("=" * 60)

    # Step 1: Generate and open authorization URL
    auth_url = get_authorization_url()
    print("\n[Step 1] Opening authorization URL in your browser...")
    print(f"\nURL: {auth_url}\n")

    try:
        webbrowser.open(auth_url)
        print("Browser opened! Please approve the app.")
    except:
        print("Could not open browser. Please copy and paste the URL above.")

    # Step 2: Get the authorization code from user
    print("\n[Step 2] After approving, you'll be redirected to a URL like:")
    print("  https://localhost/callback?code=XXXXXX&...")
    print("\nCopy the 'code' value from that URL.")

    code = input("\nPaste the authorization code here: ").strip()

    if not code:
        print("No code provided. Exiting.")
        return

    # Step 3: Exchange code for token
    print("\n[Step 3] Exchanging code for access token...")

    token = exchange_code_for_token(code)

    if token:
        print("\n" + "=" * 60)
        print("SUCCESS! Here's your Admin API access token:")
        print("=" * 60)
        print(f"\n{token}\n")
        print("Add this to your .env file as:")
        print(f"SHOPIFY_API_SECRET={token}")
        print("=" * 60)
    else:
        print("\nFailed to get access token.")

if __name__ == "__main__":
    main()
