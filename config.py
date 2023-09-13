# config.py

# This is a dictionary where keys are investor names and values are lists of example prompts for that investor.
investor_specific_prompts = {
    "InvestorA": [
        "Analyze stock market data",
        "Write a script to fetch real-time stock prices",
        "Visualize stock market trends"
    ],
    "InvestorB": [
        "Develop a real estate price prediction model",
        "Analyze property market trends",
        "Write a script to scrape real estate listings"
    ],
    # Add more investors and their specific tasks as needed
}

# Default investor - change this before sending to a specific investor.
DEFAULT_INVESTOR = "InvestorA"
