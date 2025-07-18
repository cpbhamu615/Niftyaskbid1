from supabase import create_client
import os

# Load env from local machine (Not for cloud)
url = "https://qtpwefwbcncbdgrivzla.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

supabase = create_client(url, key)

# Upload data to storage
with open("live_data.pkl", "rb") as f:
    data = f.read()

# Upload (create or overwrite)
res = supabase.storage.from_("niftyaskbid-data").upload(
    "live_data.pkl",
    data,
    {"content-type": "application/octet-stream", "x-upsert": "true"}
)

print(res)