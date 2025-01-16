# FastAPI + Gemini + Streamlit Project

This project is a REST API built using **FastAPI**, integrated with the **Gemini API** for AI-powered responses, and features a user-friendly interface created with **Streamlit**. Users can input prompts, and the application will generate responses using the Gemini API.

---

## Features
- **FastAPI Backend**: A robust and fast REST API to handle requests.
- **Gemini API Integration**: AI-powered responses using Google's Gemini API.
- **Streamlit Frontend**: A simple and interactive web interface for users to input prompts and view responses.

---
## How to Use

### Prerequisites
1. **Python 3.8+**: Ensure Python is installed on your system.
2. **Gemini API Key**: Obtain an API key from [Google AI Studio](https://ai.google.dev/).

### Installation
1. Clone this repository:
   ```bash
   
   git clone https://github.com/Ziixh/GeminiBasicChatBot
   git clone https://github.com/your-username/your-repo-name.git
Navigate to the project folder:
   cd fasttutorial

Install the required dependencies:
    pip install -r requirements.txt


Setting Up Environment Variables
    Create a .env file in the root of your project folder.

Add your Gemini API key to the .env file:
GEMINI_API_KEY=your_api_key_here

Running the FastAPI Server
    Start the FastAPI server:
    uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000.

Running the Streamlit App
    Start the Streamlit application:
    streamlit run streamlit_app.py
Open your browser and navigate to the provided local URL (e.g., http://localhost:8501).


All dependencies are listed in the requirements.txt file.


