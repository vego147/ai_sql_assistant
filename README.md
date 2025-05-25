AI SQL Assistant
The AI SQL Assistant project is designed to simplify database interaction through natural language queries. It leverages AI (specifically Google's Gemini API) to generate SQL queries based on user input and the structure of the database. This allows users to interact with their PostgreSQL database in an intuitive way.

Features
Database Connection: Connects to a PostgreSQL database using environment variables for credentials.

Dynamic SQL Generation: Uses Gemini API to generate raw SQL queries based on user input.

Conversation History: Keeps track of the conversation history to generate context-aware SQL queries.

Table & Column Checking: Ensures the specified table exists in the database and fetches column names.

Commit Changes: Supports committing database changes to the server.

Prerequisites
Python 3.8+

PostgreSQL (Make sure the database is set up and accessible)

Gemini API Key: Required to interact with the Google Gemini API for SQL generation.

Installation
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/ai_sql_assistant.git
cd ai_sql_assistant
Step 2: Install Dependencies
Install the required Python libraries using pip:

bash
Copy
Edit
pip install -r requirements.txt
Step 3: Set Up Environment Variables
Create a .env file in the root directory of the project and add the following environment variables:

dotenv
Copy
Edit
DB_HOST=<your_database_host>
DB_PORT=<your_database_port>
DB_USER=<your_database_user>
DB_NAME=<your_database_name>
DB_PASSWORD=<your_database_password>
GEMINI_API=<your_gemini_api_key>
Replace <your_database_* values with your actual PostgreSQL database credentials.

Replace <your_gemini_api_key> with your Gemini API key.

Step 4: Run the Program
To start the AI SQL Assistant, run the following command:

bash
Copy
Edit
python ai_sql_assistant.py
Step 5: Interact with the Assistant
Accessing a table: Enter the name of the table you want to interact with.

SQL operations: You can input various natural language SQL queries like:

"Show me all rows"

"What is the average salary in the employees table?"

Commit changes: Type commit to save any changes to the database.

Exit: Type quit to exit the application.

Example Usage
bash
Copy
Edit
Please Enter name You want to access: employees
Please Enter What you want to do with employees: Show me all rows
(1, 'John', 25, 'Software Engineer', 55000)
(2, 'Jane', 30, 'Data Scientist', 60000)

Please Enter What you want to do with employees: commit
Database Updated

Please Enter name You want to access: quit
Project Structure
ai_sql_assistant.py: Main script that interacts with the user and processes input to generate SQL queries.

database.py: Contains functions for connecting to the PostgreSQL database and interacting with it.

agent.py: Manages communication with the Gemini API to generate SQL queries based on user input.

.env: Stores environment variables for database credentials and API keys.

requirements.txt: Lists the dependencies for the project.

Dependencies
requests: Used to interact with the Gemini API.

psycopg2: PostgreSQL adapter for Python.

python-dotenv: Loads environment variables from the .env file.

License
This project is licensed under the MIT License - see the LICENSE file for details.

