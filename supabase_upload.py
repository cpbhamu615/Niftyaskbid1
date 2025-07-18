from supabase import create_client, Client

url = "https://qtpwefwbcncbdgrivzla.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."  # Your Supabase anon key

supabase: Client = create_client(url, key)

with open("live_data.pkl", "rb") as f:
    data = f.read()

# Upload with correct 'x-upsert' header
res = supabase.storage.from_("niftyaskbid-data").upload(
    "live_data.pkl", 
    data, 
    {
        "content-type": "application/octet-stream",
        "x-upsert": "true"   # ✅ Correct header for overwrite
    }
)

print("✅ Upload Success")
print(res)