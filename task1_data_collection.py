# Import required libraries
import requests       
import os               
import pandas as pd     
from dotenv import load_dotenv 

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the .env file
API_KEY = os.getenv('API_KEY')

# Create the API URL to fetch news related to "bitcoin"
url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}"

# Send a request to the News API
response = requests.get(url)

# Convert the response from JSON format into a Python dictionary
data = response.json()

# Check if the API returned an error
if data["status"] != "ok":
    print("API Error:", data["message"])

# Extract the list of articles from the API response
articles = data.get("articles", [])

# Print the number of articles received from the API
print("Number of articles:", len(articles))

# Create an empty list to store extracted news data
news_list = []

# Loop through each article and extract useful fields
for article in articles:
    news_list.append({
        "title": article["title"],                 
        "source": article["source"]["name"],        
        "author": article["author"],               
        "description": article["description"],     
        "content": article["content"],              
        "publishedAt": article["publishedAt"]       
    })

# Convert the collected news data into a pandas DataFrame
df = pd.DataFrame(news_list)

# Save dataset
df.to_csv("news_data.csv", index=False)

print("Data collection completed")
