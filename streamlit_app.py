import streamlit as st
from supabase import create_client
import pickle
import os

# Supabase Config
url = os.getenv("SUPABASE_URL", "https://qtpwefwbcncbdgrivzla.supabase.co")
key = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF0cHdlZndiY25jYmRncml2emxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI4MjIzMDAsImV4cCI6MjA2ODM5ODMwMH0.GAv0sn3NFUZ7CFbF3j2BmGoU8P8FlQzdHUrX5iExlbo")  # 🔑 Replace with your anon key

supabase = create_client(url, key)

# Fetch pickle
try:
    response = supabase.storage.from_("niftyaskbid-data").download("live_data.pkl")
    data = pickle.loads(response.read())
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

# UI
st.set_page_config(layout="wide")
st.title("📊 NiftyAskBid - Live Bid/Ask Tracker")

for symbol in data.keys():
    st.header(f"🔹 {symbol}")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top Bids")
        st.table(data[symbol]["bid"])

    with col2:
        st.subheader("Top Asks")
        st.table(data[symbol]["ask"])

    st.markdown(f"LTP: {data[symbol]['ltp']}")