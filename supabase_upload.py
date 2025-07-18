from supabase import create_client, Client

# Supabase Credentials
url = "https://qtpwefwbcncbdgrivzla.supabase.co"    # Your Supabase URL
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF0cHdlZndiY25jYmRncml2emxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI4MjIzMDAsImV4cCI6MjA2ODM5ODMwMH0.GAv0sn3NFUZ7CFbF3j2BmGoU8P8FlQzdHUrX5iExlbo"     # Your Supabase Anon Key

supabase: Client = create_client(url, key)

# Upload live_data.pkl to Supabase Storage bucket
bucket_name = "niftyaskbid-data"
file_path = "live_data.pkl"

with open(file_path, "rb") as f:
    data = f.read()

# Try to upload first (if not exists), else update
try:
    res = supabase.storage.from_(bucket_name).upload(
        "live_data.pkl",  # Path in bucket
        data,
        {"content-type": "application/octet-stream"}
    )
    print("✅ Uploaded successfully")
except Exception as e:
    print("🔄 File exists, trying to update...")
    res = supabase.storage.from_(bucket_name).update(
        "live_data.pkl",
        data,
        {"content-type": "application/octet-stream"}
    )
    print("✅ Updated successfully")