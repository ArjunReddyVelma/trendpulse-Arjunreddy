import pandas as pd
df = pd.read_csv("news_data.csv")
# check dataset
print(df.info())
# Fill missing values in 'author' column with 'Unknown'
df['author'] = df['author'].fillna('Unknown')
# Fill missing values in 'description' column with the corresponding 'title' value
df['description'] = df['description'].fillna(df['title'])
df['publishedAt'] = pd.to_datetime(df['publishedAt'], errors='coerce')
# Save the cleaned dataset to a new CSV file
df.to_csv("cleaned_news_data.csv", index=False)
print("Data cleaning completed")
