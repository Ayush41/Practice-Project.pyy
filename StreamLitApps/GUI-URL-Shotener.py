import streamlit as st
import pyshorteners as pysh

def shorten_url(long_url):
    shortener = pysh.Shortener()
    try:
        short_url = shortener.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("URL Shortener")

    # Input for long URL
    long_url = st.text_input("Enter the long URL:")

    if st.button("Shorten URL"):
        if long_url:
            short_url = shorten_url(long_url)
            st.text_input("Output shortened link:", value=short_url, key="shortened_url")
        else:
            st.error("Please enter a valid URL.")

if __name__ == "__main__":
    main()
