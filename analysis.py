import pandas as pd

# Load the cleaned dataset containing the processed news articles
df = pd.read_csv("cleaned_news_data.csv")
print(df.info())
# Display dataset information such as number of rows, columns,
# data types, and whether any missing values exist.
# Conclusion: This helps verify that the dataset is properly cleaned and that each column has the expected data type.

df.head()
# Display the first few rows of the dataset.
# Conclusion: Allows us to visually inspect the structure and confirm that the data looks correct.

df["source"].unique()
# Display all unique news sources present in the dataset.
# Conclusion: This shows the variety of publishers that contributed articles in the dataset.
df["source"].value_counts().head(10)
# Count how many articles were published by each news source
# and display the top 10 most frequent sources.
# Conclusion: This helps identify which news publishers produce the most articles in the dataset.

df["publishedAt"] = pd.to_datetime(df["publishedAt"])
# Convert the publishedAt column from string format to datetime so that time-based analysis can be performed.

df["publishedAt"].dt.date.value_counts()
# Count how many articles were published on each date.
# Conclusion: This reveals the distribution of articles over time and helps identify days with higher news activity.