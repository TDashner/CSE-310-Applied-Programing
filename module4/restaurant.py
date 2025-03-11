import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load dataset 
df = pd.read_csv('C:/Users/tessa/OneDrive/Desktop/restaurant_reviews.csv')

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Display basic info about dataset
print('Dataset Information:')
print(df.info())
print('\nFirst few rows of the dataset:')
print(df.head())

df = df.dropna(subset=['country', 'restaurant_name', 'sentiment', 'review_title', 'review_date', 'review'])

df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')

# Question 1: What are the most popular restaurants based on review count?
restaurant_counts = df['restaurant_name'].value_counts()
print('\nMost popular restaurants:')
print(restaurant_counts.head(10))

# Question 2: What is the average sentiment for different restaurants?
restaurant_avg_sentiment = df.groupby('restaurant_name')['sentiment'].mean().sort_values(ascending=False)
print('\nAverage sentiment per restaurant:')
print(restaurant_avg_sentiment.head(10))

# Normalize sentiments to a scale of 0-5
df['normalized_sentiment'] = (df['sentiment'] - df['sentiment'].min()) / (df['sentiment'].max() - df['sentiment'].min()) * 5

# Function to compute sentiment score
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['review'] = df['review'].fillna("").astype(str)  # This ensures text data is valid
df['sentiment_score'] = df['review'].apply(get_sentiment)

# Question 3: Which restaurants have the highest positive sentiment?
restaurant_sentiment = df.groupby('restaurant_name')['sentiment_score'].mean().sort_values(ascending=False)
print('\nRestaurants with highest sentiment:')
print(restaurant_sentiment.head(10))

# Stretch Challenge: Visualization
plt.figure(figsize=(10,5))
restaurant_counts.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Popular Restaurants')
plt.xlabel('Restaurant')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
restaurant_avg_sentiment.head(10).plot(kind='bar', color='lightcoral')
plt.title('Top 10 Highest Rated Restaurants')
plt.xlabel('Restaurant')
plt.ylabel('Average Sentiment')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
restaurant_sentiment.head(10).plot(kind='bar', color='lightgreen')
plt.title('Top 10 Restaurants by Sentiment Score')
plt.xlabel('Restaurant')
plt.ylabel('Average Sentiment Score')
plt.xticks(rotation=45)
plt.show()

print('\nDescriptive statistics for numerical columns:')
print(df.describe())
