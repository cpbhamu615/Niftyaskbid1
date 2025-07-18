import streamlit as st
from supabase import create_client
import pickle
import os

# 🔑 Load Supabase URL and KEY from Streamlit Secrets
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Supabase Client
supabase = create_client(url, key)

# Download and Load Pickle Data
try:
    response = supabase.storage.from_("niftyaskbid-data").download("live_data.pkl")
    data = pickle.loads(response)
except Exception as e:
    st.error(f"Data load error: {e}")
    st.stop()

# Streamlit App UI
st.set_page_config(layout="wide")
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