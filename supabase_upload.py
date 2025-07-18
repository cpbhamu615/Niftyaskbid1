from supabase import create_client, Client

url = "https://qtpwefwbcncbdgrivzla.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."  # Your Anon key

supabase: Client = create_client(url, key)

with open("live_data.pkl", "rb") as f:
    data = f.read()

# ✅ Use update() for overwrite
res = supabase.storage.from_("niftyaskbid-data").update(
    "live_data.pkl", 
    data, 
    {"content-type": "application/octet-stream"}
)

print("✅ Upload/Update Success")
print(res)