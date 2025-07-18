import streamlit as st
from supabase import create_client
import pickle

# Supabase Config from Streamlit Secrets
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)

# Download from Supabase Storage
try:
    response = supabase.storage.from_("niftyaskbid-data").download("live_data.pkl")
    data_bytes = response.read()
    data = pickle.loads(data_bytes)
except Exception as e:
    st.error(f"Data load error: {e}")
    st.stop()

# Streamlit UI
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