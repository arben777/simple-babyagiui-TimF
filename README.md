
# Baby-AGI Investor Showcase

Welcome to the Baby-AGI Investor Showcase! This application is designed to demonstrate the capabilities of a Baby-AGI system to potential investors. It provides an interactive interface where investors can input objectives and observe the AI in action, handling tasks, and completing objectives.

## Features:

1. **Objective Input**: Investors can specify their own objective or choose from pre-defined prompts tailored to them.
2. **Task Management**: The application employs an AI-driven task management system that creates, prioritizes, and executes tasks based on user input.
3. **LangChain Framework**: The application uses the LangChain framework, which aids in the intelligent generation and execution of tasks.
4. **OpenAI Integration**: Leveraging the power of OpenAI, the application uses embeddings to assist in task-related operations.
5. **Customized Experience**: The application can be easily customized with investor-specific example prompts, providing a personalized experience.
6. **Intuitive Interface**: Powered by Streamlit, the interface is user-friendly and straightforward.

## Investor-specific Example Prompts:

To make the demo process smoother and more relatable, we've implemented a feature where each investor can have a set of example prompts tailored to their interests or industry. By selecting one of these prompts, they can quickly see the AI's capabilities relevant to their domain.

## Getting Started:

### Customizing for a Specific Investor:

1. **Configuration File**: The `config.py` file is where you can specify investor-specific example prompts. It provides a simple dictionary format for adding new investors and their associated prompts.
    ```python
    investor_specific_prompts = {
        "InvestorA": ["Prompt 1 for InvestorA", "Prompt 2 for InvestorA"],
        "InvestorB": ["Prompt 1 for InvestorB", "Prompt 2 for InvestorB"],
    }
    ```

2. **Setting the Default Investor**: In the same `config.py` file, set the `DEFAULT_INVESTOR` variable to the name of the investor for whom you are preparing the application.
    ```python
    DEFAULT_INVESTOR = "InvestorA"
    ```

### Deployment:

#### Online Deployment:

For making the app shareable and accessible to investors, deploy the application on a cloud platform:

1. **Heroku**:
    - Ensure you have a `requirements.txt` file with all necessary dependencies.
    - Create a `Procfile` with the content: `web: streamlit run main.py`.
    - Commit your changes and push to a Heroku app instance.
    - Set necessary environment variables (like the OpenAI API key) in the Heroku dashboard.

2. **Google Cloud Platform**:
    - Create a new VM instance.
    - Clone your application repository.
    - Install necessary dependencies.
    - Set environment variables and start the Streamlit app.

3. **AWS EC2**:
    - Launch an EC2 instance.
    - SSH into the instance, clone your app, and install requirements.
    - Set environment variables and start the Streamlit app.

#### Streamlit Deployment:

To deploy using Streamlit:

    - Ensure the `streamlit` library is included in your `requirements.txt`.
    - Use any of the platforms above or Streamlit sharing to deploy your app. Refer to the Streamlit documentation for more specific guidance.

#### Multiple Deployments:

For deploying multiple versions (one for each investor):

    - Adjust the `DEFAULT_INVESTOR` in the `config.py` file.
    - Deploy the application to a new instance or URL on your chosen cloud platform.
    - Share the URL with the specific investor.

## Conclusion:

The Baby-AGI Investor Showcase is designed to provide a seamless demonstration experience for potential investors. By showcasing relevant prompts and an interactive AI, we hope to engage and impress our audience. If you have any questions or need further customizations, please refer to the documentation or reach out to our team.
