import streamlit as st
import requests
from collections import defaultdict

# Set your News API key and topics
api_key = '24e059157f3047aea5330b2aa4fae652'  # Replace with your actual API key
topics = [
    "annuities",
    "pension risk transfer",
    "Bermuda reinsurance",
    "cyberattacks in life insurance",
    "technology in life insurance"
]

# Create a function to fetch news articles
def fetch_news():
    articles_by_topic = defaultdict(list)
    topic_counts = {topic: 0 for topic in topics}

    for topic in topics:
        url = f'https://newsapi.org/v2/everything?q={topic}&language=en&sortBy=publishedAt&apiKey={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            articles = response.json().get('articles', [])
            for article in articles:
                title = article['title']
                link = article['url']
                articles_by_topic[topic].append((title, link))
                topic_counts[topic] += 1

    return articles_by_topic, topic_counts

# Streamlit app layout
st.title("Life Insurance News Curator")

# Fetch news articles when the button is clicked
if st.button('Fetch News'):
    articles_by_topic, topic_counts = fetch_news()
    st.write("### Number of Articles by Topic")
    for topic, count in topic_counts.items():
        st.write(f"{topic}: {count}")

    # Display articles by topic
    for topic, articles in articles_by_topic.items():
        st.write(f"### Articles for '{topic}'")
        for title, link in articles:
            st.write(f"- **{title}** - [Read more]({link})")



