import streamlit as st
from supabase import create_client
import pickle

# Supabase Config
url = "https://qtpwefwbcncbdgrivzla.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF0cHdlZndiY25jYmRncml2emxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI4MjIzMDAsImV4cCI6MjA2ODM5ODMwMH0.GAv0sn3NFUZ7CFbF3j2BmGoU8P8FlQzdHUrX5iExlbo"

supabase = create_client(url, key)

# Download from Supabase Storage
try:
    response = supabase.storage.from_("niftyaskbid-data").download("live_data.pkl")
    data_bytes = response.data
    data = pickle.loads(data_bytes)
except Exception as e:
    st.error(f"❌ Data load error: {e}")
    st.stop()

# Streamlit UI
st.set_page_config(layout="wide")
st.title("📊 NiftyAskBid - Live Bid/Ask Tracker")

if data:
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
else:
    st.warning("No data available in live_data.pkl")