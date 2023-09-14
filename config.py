# config.py
# This is a dictionary where keys are investor names and values are lists of example prompts for that investor.
investor_specific_prompts = {
    "Tilman Fertitta": {
        "objectives": ["Revolutionize the restaurant industry by creating a chain of AI-powered, fully automated dining experiences, aiming for a nationwide rollout within 2 years", "Expand your restaurant chain by opening 5 new locations in emerging markets within the next year.", "Create a Marketing Strategy for my new restaurant in a new city"],
        "tasks": ["Research the feasibility of AI-powered kitchen automation systems. Schedule meetings with at least 3 vendors who specialize in this technology", "Analyze market trends and identify the top 3 emerging markets with a growing middle-class population. Conduct a feasibility study for each.", "Research and study most effective restaurant location grand openings"]
    },
    "InvestorB": {
        "objectives": ["Objective 1 for InvestorB", "Objective 2 for InvestorB", "Objective 3 for InvestorB"],
        "tasks": ["Task 1 for InvestorB", "Task 2 for InvestorB", "Task 3 for InvestorB"]
    },
    # Add more investors and their specific tasks as needed
}
# Default investor - change this before sending to a specific investor.
DEFAULT_INVESTOR = "Tilman Fertitta"