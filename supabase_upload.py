from supabase import create_client, Client
import os

# Supabase Credentials (from Streamlit Cloud Secrets or hardcoded for local)
url = os.getenv("SUPABASE_URL", "https://qtpwefwbcncbdgrivzla.supabase.co")
key = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF0cHdlZndiY25jYmRncml2emxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI4MjIzMDAsImV4cCI6MjA2ODM5ODMwMH0.GAv0sn3NFUZ7CFbF3j2BmGoU8P8FlQzdHUrX5iExlbo")  # 🔑 Replace with your full anon key

supabase: Client = create_client(url, key)

# Upload pickle
with open("live_data.pkl", "rb") as f:
    data = f.read()

res = supabase.storage.from_("niftyaskbid-data").upload(
    "live_data.pkl",
    data,
    {"content-type": "application/octet-stream", "x-upsert": "true"}
)

print("Upload Response:", res)