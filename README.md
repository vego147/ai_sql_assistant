# AI-Powered SQL Assistant

This project demonstrates the use of an AI-powered assistant that generates SQL queries based on user input. The system allows users to interact with a PostgreSQL database via a command-line interface, where the assistant generates raw SQL queries using the Gemini API to execute on the database.

## Features

- **AI-Powered SQL Generation**: Uses the Gemini API to dynamically generate SQL queries based on user input.
- **PostgreSQL Integration**: Connects to a PostgreSQL database to execute generated SQL queries.
- **Interactive Command Line**: Users can interact with the system to request data or perform actions on the database tables.
- **Database Table Check**: Ensures the requested tables exist in the database before execution.
- **Dynamic SQL Execution**: Executes the generated SQL queries and returns the results to the user.

## Project Structure

├── agent.py # Contains the logic for generating SQL queries via Gemini API
├── ai_sql_assistant.py # Main application file to interact with the database
├── database.py # Contains database connection logic and helper functions
├── .env # Environment variables (for API keys and database credentials)
├── README.md # Project documentation (this file)
├── requirements.txt # List of project dependencies
└── .gitignore # Git ignore file

markdown
Copy
Edit

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.x
- PostgreSQL database
- Gemini API key (from Google Cloud)
- psycopg2 (PostgreSQL client for Python)
- requests (for API calls)
- python-dotenv (for loading environment variables)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-sql-assistant.git
cd ai-sql-assistant
2. Create a virtual environment:
bash
Copy
Edit
python -m venv myenv
source myenv/bin/activate  # On Windows, use myenv\Scripts\activate
3. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
4. Set up the environment variables:
Create a .env file in the root directory of the project and add your database credentials and Gemini API key:

bash
Copy
Edit
DB_HOST=your-db-host
DB_PORT=your-db-port
DB_NAME=your-db-name
DB_USER=your-db-username
DB_PASSWORD=your-db-password
GEMINI_API=your-gemini-api-key
5. Run the application:
After setting up the environment, run the ai_sql_assistant.py file:

bash
Copy
Edit
python ai_sql_assistant.py
The program will prompt you for a table name and allow you to perform SQL operations by typing commands. You can interact with the database through this command-line interface.

Usage
Once the program is running, the system will ask for the table name you want to access and interact with. You can enter SQL-related queries, and the system will generate and execute the corresponding SQL for you.

Example:

bash
Copy
Edit
Please Enter name You want to access: employee
Please Enter What you want to do with employee: SELECT * FROM employee WHERE department = 'Sales';
You can also use the following commands:

quit: To exit the program.

commit: To commit any changes to the database.

The AI will respond by executing the SQL query and returning the result.

Database Schema
The application assumes you have a PostgreSQL database with one or more tables.

The employee table is used as an example. It should have the following columns (as an example, but can be modified as needed):

Column Name	Data Type
id	INTEGER
name	VARCHAR
department	VARCHAR
performance_score	INTEGER

Feel free to modify the database schema to fit your needs.

Contributing
Fork the repository.

Create a new branch (git checkout -b feature/your-feature).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature).

Create a new Pull Request.

License
This project is open-source and available under the MIT License.
