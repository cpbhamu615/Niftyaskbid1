from supabase import create_client, Client

url = "https://qtpwefwbcncbdgrivzla.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

supabase: Client = create_client(url, key)

# Read pickle file as bytes
with open("live_data.pkl", "rb") as f:
    data = f.read()

# Upload to Supabase Storage
res = supabase.storage.from_("niftyaskbid-data").upload(
    "live_data.pkl",
    data,
    {"content-type": "application/octet-stream", "upsert": "true"}
)

print(res)