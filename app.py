import streamlit as st
import requests
from datetime import datetime

# Function to fetch news articles
def fetch_news(api_key, query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return articles
    else:
        st.error(f'Failed to retrieve news: {response.status_code}')
        return []

# Set your News API key
api_key = '24e059157f3047aea5330b2aa4fae652'  # Replace with your News API key

# Title of the app
st.title('Life Insurance Industry News Curator')

# Display the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Current Date and Time: {current_time}")

# Define the topics to search for
topics = {
    "Annuities": "annuities",
    "Pension Risk Transfer": "pension risk transfer",
    "Bermuda Reinsurance": "Bermuda reinsurance",
    "Cyberattacks in Life Insurance": "cyberattacks life insurance",
    "Technology in Life Insurance": "technology life insurance"
}

# Create a dropdown to select a topic
selected_topic = st.selectbox('Select a topic to fetch news:', list(topics.keys()))

# Fetch and display news articles for the selected topic
if st.button('Fetch News'):
    query = topics[selected_topic]
    articles = fetch_news(api_key, query)

    if articles:
        # Sort articles by publication date (newest first)
        articles.sort(key=lambda x: x['publishedAt'], reverse=True)

        st.subheader(f'News Articles for: {selected_topic}')
        for article in articles:
            st.write(f"**Title:** [{article['title']}]({article['url']})")
            st.write(f"**Source:** {article['source']['name']} | **Published At:** {article['publishedAt']}")
            st.write("---")

