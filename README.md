# Product Recommendation System with Sentiment Analysis

This repository contains a Python-based product recommendation system that generates recommendations and uses sentiment analysis on Amazon product reviews and statistical calculations. The goal is to provide users with an insightful analysis of products based on real-time data retrieved from Amazon.

## Features

- **Sentiment Analysis**: Analyzes product reviews using Sentiment Intensity Analysis (VADER) to evaluate the sentiment of user reviews.
- **Statistical Analysis**: Leverages advanced statistical methods, including beta distribution, to analyze and assess product ratings and reviews.
- **Web Scraping**: Extracts review data using Selenium and BeautifulSoup to gather and analyze reviews from Amazon product pages.
- **Real-time Recommendations**: The system generates dynamic product recommendations based on user review ratings, sentiment analysis, and statistical calculations.

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/actionproject-madhav/Amazon-Product-Recommender-Tool.git
    cd Amazon-Product-Recommender-Tool
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:

    You can modify `amazon.py` or `main.py` to enter the Amazon product URL you'd like to analyze. Run the script to gather data, analyze sentiment, and get product recommendations.

4. **Explore results**:

    Visualizations in PNG files provide a graphical representation of sentiment and ratings analysis.

## Requirements

- Python 3.x
- Libraries listed in `requirements.txt`

## Tools & Technologies

- **Python**: Primary language for the project
- **Selenium**: Web scraping and browser automation
- **BeautifulSoup**: Parsing HTML for extracting reviews
- **NLTK**: Sentiment analysis library (VADER)
- **SciPy**: Statistical analysis tools
- **Matplotlib & Seaborn**: Visualizations and graphs

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
