import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to extract i10 index and H-index from a Google Scholar profile URL
def extract_indices(url):
    # Send a request to the Google Scholar profile page
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return None, "Error fetching the profile. Please check the URL."

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the H-index and i10 index
    try:
        stats = soup.find_all('td', class_='gsc_rsb_std')
        h_index = stats[0].text  # H-index
        i10_index = stats[2].text  # i10 index
        return h_index, i10_index
    except IndexError:
        return None, "Could not find H-index and i10 index. Check the profile format."

# Streamlit application
st.title("Google Scholar Index Extractor")
st.write("Enter the Google Scholar profile URL to extract H-index and i10 index.")

# User input
url = st.text_input("Google Scholar Profile URL:")

if st.button("Extract Indices"):
    if url:
        h_index, i10_index = extract_indices(url)
        if h_index is not None:
            st.success(f"H-index: {h_index}")
            st.success(f"i10 Index: {i10_index}")
        else:
            st.error(i10_index)  # Show error message
    else:
        st.error("Please enter a valid URL.")