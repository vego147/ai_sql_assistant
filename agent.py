import requests
import os 
from dotenv import load_dotenv


load_dotenv()

api_key= os.getenv('GEMINI_API')

url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}'
header ={
    'Content-Type': 'application/json'
}

def sql_agent(table_name, column_names, convo_history, user_input):
    prompt = f"""
    You are an expert postgreSQL generator. Below is a conversation history with the user. 
    Generate only the raw SQL for the last user request, no quotes or markdown.
    DB structures:
    table_name = {table_name}
    column: {column_names}
    Conversation:
    {convo_history}

    Respond with only the raw SQL for the {user_input}
    """

    dummy_prompt = "hi how are you whats the basic sql code to view everything"
    data = {
      "contents": [
          {
            "parts": [
              {
               "text": prompt
              }
            ]
          }
        ]
      }
    
    response = requests.post(url,headers=header,json=data)
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text'].strip().replace("```sql", "").replace("```", "").strip()

    else:
        raise Exception(f"Gemini API Error: {response.status_code} {response.text}")
