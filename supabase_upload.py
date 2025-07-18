import os
import pickle
from supabase import create_client

# Load Supabase credentials from environment variables
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# Read local live_data.pkl
with open("live_data.pkl", "rb") as f:
    data = f.read()

# Upload file with upsert enabled
res = supabase.storage.from_("niftyaskbid-data").upload(
    "live_data.pkl",
    data,
    {"content-type": "application/octet-stream", "x-upsert": "true"}
)

print("Upload Response:", res)