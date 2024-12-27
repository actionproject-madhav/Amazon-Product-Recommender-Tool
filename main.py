import pandas as pd
import numpy as np
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import beta as beta_dist

# Download necessary NLTK resources
nltk.download('vader_lexicon')

# Load the dataset
df = pd.read_csv('review.csv')  # Ensure this file exists in your working directory
df = df.head(1000)  # For demo purposes, limit to the first 1000 reviews

# Set up the SentimentIntensityAnalyzer
so = SentimentIntensityAnalyzer()

# Calculate sentiment scores for each review
collector = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row['Text']
    id = row['Id']
    collector[id] = so.polarity_scores(text)

# Convert sentiment scores into DataFrame
pandas_data = pd.DataFrame(collector).T
pandas_data = pandas_data.reset_index().rename(columns={'index': 'Id'})  # Ensure the 'Id' column is correctly named

# Merge the sentiment data with the original data
merged_data = pandas_data.merge(df, how='left', on='Id')

# Function to categorize sentiment: Positive, Neutral, Negative
def get_sentiment_label(compound_score):
    if compound_score >= 0.1:  # Stronger threshold for Positive sentiment
        return 'Positive'
    elif compound_score <= -0.1:  # Stronger threshold for Negative sentiment
        return 'Negative'
    else:
        return 'Neutral'

merged_data['Sentiment'] = merged_data['compound'].apply(lambda x: get_sentiment_label(x))  # Fixed reference to 'compound'

# Calculate the overall sentiment distribution
positive_sentiment = len(merged_data[merged_data['Sentiment'] == 'Positive'])
negative_sentiment = len(merged_data[merged_data['Sentiment'] == 'Negative'])
neutral_sentiment = len(merged_data[merged_data['Sentiment'] == 'Neutral'])

# Plot Sentiment Distribution with distinct colors
sentiment_counts = [positive_sentiment, negative_sentiment, neutral_sentiment]
sentiment_labels = ['Positive Sentiment', 'Negative Sentiment', 'Neutral Sentiment']
colors = ['#2ca02c', '#d62728', '#c6c6c6']  # Green for Positive, Red for Negative, Grey for Neutral

plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_labels, y=sentiment_counts, palette=colors)

plt.title('Customer Satisfaction Based on Sentiments Expressed in Reviews')
plt.xlabel('Sentiment Based on Review Comments')
plt.ylabel('Number of Reviews')
plt.tight_layout()
plt.show()

# Customer Satisfaction probability using Beta distribution (with laplace smoothing)
initial_beta_parameters = [1, 1]  # uniform distribution at first
initial_beta_parameters[0] += positive_sentiment
initial_beta_parameters[1] += negative_sentiment
beta_success_sentiment = initial_beta_parameters[0] / (initial_beta_parameters[0] + initial_beta_parameters[1])
print(f'Customer Satisfaction based on Sentiment (Beta Success): {beta_success_sentiment:.2f}')

# Customer Satisfaction probability directly using the Score column with Beta distribution
positive_threshold = 4
negative_threshold = 2

positive_reviews = len(df[df['Score'] >= positive_threshold])
negative_reviews = len(df[df['Score'] <= negative_threshold])

# Apply Laplace's Succession for smoothing (Add 1 to the counts)
alpha = positive_reviews + 1
beta_param = negative_reviews + 1  # Renamed to avoid overwriting
beta_success_rating = alpha / (alpha + beta_param)

x = np.linspace(0, 1, 100)

# Generate y values based on the Beta distribution
y = beta_dist.pdf(x, alpha, beta_param)

# Plotting the Beta distribution
plt.figure(figsize=(8, 6))

# Plot the curve with a label for the Beta distribution
plt.plot(x, y, label=f'Beta Distribution\n(alpha={alpha}, beta={beta_param})', color='b', lw=2)

# Customize the plot with labels and title
plt.title('Beta Distribution of Customer Satisfaction', fontsize=16)
plt.xlabel('Probability of Customer Satisfaction', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.axvline(x=beta_success_rating, color='r', linestyle='--', label=f'Satisfaction Chance = {beta_success_rating:.2f}')
plt.legend(loc='upper left')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()

# Success rate using the Beta distribution formula
print(f'Customer Satisfaction based on Ratings (Beta Success): {beta_success_rating:.2f}')

# Plot ratings-based sentiment distribution with distinct colors
rating_counts = [positive_reviews, negative_reviews, len(df) - (positive_reviews + negative_reviews)]
rating_labels = ['Positive Reviews', 'Negative Reviews', 'Neutral Reviews']
rating_colors = ['#2ca02c', '#d62728', '#c6c6c6']  # Green for Positive, Red for Negative, Grey for Neutral

plt.figure(figsize=(8, 6))
sns.barplot(x=rating_labels, y=rating_counts, palette=rating_colors)

plt.title('Customer Satisfaction Based on Ratings Given')
plt.xlabel('Ratings ')
plt.ylabel('Number of Reviews')
plt.tight_layout()
plt.show()

final = (beta_success_sentiment + beta_success_rating) / 2 * 100
total = len(df)
print(f"Based on detailed word-by-word analysis of sentiment in each of the {total} reviews and ratings, there's a {final:.1f}% chance you will be satisfied.")
