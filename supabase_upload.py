import streamlit as st
from supabase import create_client
import pickle

# Supabase Config
url = "https://qtpwefwbcncbdgrivzla.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF0cHdlZndiY25jYmRncml2emxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI4MjIzMDAsImV4cCI6MjA2ODM5ODMwMH0.GAv0sn3NFUZ7CFbF3j2BmGoU8P8FlQzdHUrX5iExlbo"

supabase = create_client(url, key)

# Download file from Supabase Storage
res = supabase.storage.from_("niftyaskbid-data").download("live_data.pkl")

# Pickle Load (res is StorageResponse, so use .data)
data = pickle.loads(res.data)

# Streamlit display
st.title("📊 NiftyAskBid - Live Data View")
st.write("Live Data:", data)