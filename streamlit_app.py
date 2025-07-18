import streamlit as st
from supabase import create_client
import pickle

url = "https://qtpwefwbcncbdgrivzla.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

supabase = create_client(url, key)

try:
    response = supabase.storage.from_("niftyaskbid-data").download("live_data.pkl")
    data = pickle.loads(response)
except Exception as e:
    st.error(f"Data load error: {e}")
    st.stop()

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