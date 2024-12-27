# Product Recommendation System with Sentiment Analysis and Beta Distribution

This repository contains a Python-based product recommendation system that uses natural language processing to analyze sentiments in comments and beta distribution to analyze rating scores. 

## Features

- **Sentiment Analysis**: Analyzes product reviews using Sentiment Intensity Analysis (VADER)
- **Statistical Analysis**: Used Beta Distribution to analyze rating scores
- **Web Scraping**: Extracts review data using Selenium and BeautifulSoup to gather and analyze reviews from Amazon product pages in real-time.
- **Real-time Recommendations**: Gives a final probability that you'll be satisfied buying the product

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
