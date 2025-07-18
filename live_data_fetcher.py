from SmartApi import SmartConnect
import pyotp
import pickle

# Angel One API Credentials
API_KEY = "4TsVPFmc"
CLIENT_ID = "C38390"
PASSWORD = "9024"
TOTP_SECRET = "43ebe41b-1ca3-4c24-89e1-352879a0f67e"   # 🔑 Replace with your Angel One TOTP Secret

# Generate TOTP
totp = pyotp.TOTP(TOTP_SECRET).now()

# Angel One Login
obj = SmartConnect(api_key=API_KEY)
data = obj.generateSession(CLIENT_ID, PASSWORD, totp)

if data.get("status") is False:
    print("Login Failed:", data["message"])
    exit()

feedToken = data['feedToken']

# Dummy Nifty Data (Replace with real-time fetch if needed)
nifty_data = {
    "NIFTY": {
        "bid": [[22400, 50], [22300, 40], [22200, 30]],  # price, quantity
        "ask": [[22500, 60], [22600, 70], [22700, 80]],
        "ltp": 22450
    }
}

# Save locally as pickle
with open("live_data.pkl", "wb") as f:
    pickle.dump(nifty_data, f)

print("live_data.pkl saved successfully.")