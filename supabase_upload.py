from supabase import create_client, Client
import pickle

# Supabase credentials
url = "https://qtpwefwbcncbdgrivzla.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

supabase: Client = create_client(url, key)

# Upload live_data.pkl to Supabase Storage
with open("live_data.pkl", "rb") as f:
    data = f.read()

res = supabase.storage.from_("niftyaskbid-data").upload(
    "live_data.pkl",  # Path in bucket
    data,             # File content
    {"content-type": "application/octet-stream", "upsert": "true"}
)

print("✅ Upload Successful!")
print(res)