import streamlit as st
from supabase import create_client, Client
import pickle

# Supabase Credentials
url = "https://qtpwefwbcncbdgrivzla.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF0cHdlZndiY25jYmRncml2emxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI4MjIzMDAsImV4cCI6MjA2ODM5ODMwMH0.GAv0sn3NFUZ7CFbF3j2BmGoU8P8FlQzdHUrX5iExlbo"

supabase: Client = create_client(url, key)

bucket_name = "niftyaskbid-data"
file_name = "live_data.pkl"

try:
    res = supabase.storage.from_(bucket_name).download(file_name)
    data = pickle.loads(res)
except Exception as e:
    st.error(f"Data load error: {e}")
    st.stop()

# UI
st.title("📊 NiftyAskBid - Live Bid/Ask Tracker")

for symbol in data.keys():
    st.header(f"🔹 {symbol}")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 20 Bids")
        st.table(data[symbol]['bid'])

    with col2:
        st.subheader("Top 20 Asks")
        st.table(data[symbol]['ask'])

    st.markdown(f"LTP: {data[symbol]['ltp']}")