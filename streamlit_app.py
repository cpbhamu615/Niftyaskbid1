import streamlit as st
from supabase import create_client
import pickle
import os

# Supabase URL and Key from Streamlit Secrets
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)

bucket_name = "niftyaskbid-data"
file_name = "live_data.pkl"

try:
    # Download file from Supabase storage
    res = supabase.storage.from_(bucket_name).download(file_name)
    data_bytes = res.read()
    data = pickle.loads(data_bytes)
except Exception as e:
    st.error(f"Data load error: {e}")
    st.stop()

# Streamlit UI
st.set_page_config(layout="wide")
st.title("📊 NiftyAskBid - Live Bid/Ask Tracker")

if not data:
    st.warning("No live data available.")
    st.stop()

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