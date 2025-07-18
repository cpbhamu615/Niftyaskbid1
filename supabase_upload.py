from supabase import create_client
import os

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

bucket_name = "niftyaskbid-data"
file_name = "live_data.pkl"

# Read local pickle file
with open(file_name, "rb") as f:
    data = f.read()

# Upload to Supabase
res = supabase.storage.from_(bucket_name).upload(
    file_name,
    data,
    {"content-type": "application/octet-stream", "x-upsert": "true"}
)

print("Upload response:", res)