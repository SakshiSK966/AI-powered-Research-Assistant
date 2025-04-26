# AI-powered-Research-Assistant
Overview
This project is an AI-powered research assistant designed to help users gather relevant research results and generate informative answers based on their queries. It uses advanced AI technologies like LangChain, Tavily, and Hugging Face models to automate the research process and provide well-structured answers.

Users can input their research query, and the system will fetch relevant information from online sources, then generate a detailed and informative response using a language generation model.

Features
Research Query Input: Users can input their queries in the text box.
Research Results: The system fetches research results using the Tavily API.
Answer Generation: Based on the fetched results, a detailed answer is generated using the T5-small transformer model.

Why API Keys Are Hidden
API keys, such as the TAVILY_API_KEY and HUGGINGFACEHUB_API_TOKEN, are used to authenticate requests to external services (Tavily and Hugging Face). These keys are sensitive and should never be publicly exposed in code repositories, as they can be misused by unauthorized individuals, potentially leading to security risks, data breaches, or service limitations.
To ensure the safety of the API keys, I have stored them in a .env file, which is excluded from version control using .gitignore. This ensures the keys are never exposed to the public.

How to Run the Project
To run this project locally, follow these steps:
1. Clone the Repository
Clone the repository to your local machine using Git:
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant

2. Install Dependencies
Install the required Python libraries using pip:
pip install -r requirements.txt
Make sure you have python-dotenv, streamlit, langchain, transformers, and tavily installed.

3. Set Up Environment Variables
Create a .env file in the root directory of the project and add your API keys:
touch .env

Inside the .env file, add the following:
TAVILY_API_KEY=your_tavily_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
Replace your_tavily_api_key_here and your_huggingface_api_token_here with the actual API keys.

4. Run the Streamlit App
Start the Streamlit application:
streamlit run app.py
This will open the project in your browser, where you can interact with the AI-powered research assistant.

Notes
The .env file is excluded from version control to protect sensitive information like API keys.
The project uses Tavily for research results and Hugging Face's T5-small model for generating answers based on the results.
If you encounter any issues, make sure your API keys are correctly set in the .env file.

