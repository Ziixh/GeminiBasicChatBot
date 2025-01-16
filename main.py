from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

# Configure the Gemini API with the key
genai.configure(api_key=API_KEY)

app = FastAPI()

# Pydantic model for user query
class UserQuery(BaseModel):
    prompt: str

# Pydantic model for API response
class GeminiResponse(BaseModel):
    response: str

# Route to interact with Gemini API
@app.post("/ask-gemini", response_model=GeminiResponse)
def ask_gemini(query: UserQuery):
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel('gemini-pro')

        # Generate a response
        response = model.generate_content(query.prompt)

        # Return the response
        return GeminiResponse(response=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))