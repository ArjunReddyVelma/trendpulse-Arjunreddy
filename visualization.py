import matplotlib.pyplot as plt
import pandas as pd

# Load the cleaned dataset containing the processed news articles
df = pd.read_csv("cleaned_news_data.csv")

# Convert publishedAt column to datetime format
df["publishedAt"] = pd.to_datetime(df["publishedAt"])

# Count the number of articles published by each news source
source_counts = df["source"].value_counts()

plt.figure(figsize=(10, 6))
source_counts.head(10).plot(kind="bar")

plt.title("Top 10 News Sources by Article Count")
plt.xlabel("News Source")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45)

plt.tight_layout()


# Count articles by author
author_counts = df["author"].dropna().value_counts()

plt.figure(figsize=(10, 6))
author_counts.head(10).plot(kind="bar")

plt.title("Top 10 Authors by Article Count")
plt.xlabel("Author")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45)

plt.tight_layout()


# Count number of articles per day
articles_per_day = df["publishedAt"].dt.date.value_counts().sort_index()

plt.figure(figsize=(12, 6))
articles_per_day.plot(kind="line")

plt.title("Number of Articles Published Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45)

plt.tight_layout()


# Analyze most common words in titles
words = df["title"].str.lower().str.split().explode()
keyword_counts = words.value_counts().head(10)

plt.figure(figsize=(10,6))
keyword_counts.plot(kind="bar")

plt.title("Most Common Words in News Headlines")
plt.xlabel("Keyword")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

plt.show()