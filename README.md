# AI SQL Assistant

This project provides an AI-powered SQL assistant that allows users to interact with their PostgreSQL database using natural language. The assistant leverages the Gemini API to convert user prompts into executable SQL queries.

---

## Features

* **Natural Language to SQL:** Translate everyday language into PostgreSQL queries.
* **Conversation History:** The AI considers previous interactions to generate more accurate and contextually relevant SQL.
* **Table and Column Awareness:** The assistant understands the structure of your selected table, including its columns, to generate precise queries.
* **Basic Database Operations:** Supports `SELECT`, `INSERT`, `UPDATE`, and `DELETE` operations based on user input.
* **Database Commit:** Allows users to commit changes made to the database.

---

## Setup

### Prerequisites

* Python 3.7+
* PostgreSQL database
* A Gemini API Key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/ai-sql-assistant.git](https://github.com/your-username/ai-sql-assistant.git)
    cd ai-sql-assistant
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file containing `psycopg2-binary`, `python-dotenv`, and `requests`.)*

4.  **Create a `.env` file:**
    Create a file named `.env` in the root directory of the project and add your database credentials and Gemini API key:

    ```
    DB_HOST=your_db_host
    DB_PORT=your_db_port
    DB_USER=your_db_user
    DB_NAME=your_db_name
    DB_PASSWORD=your_db_password
    GEMINI_API=your_gemini_api_key
    ```
    Replace the placeholder values with your actual database and Gemini API credentials.

---

## Usage

1.  **Run the main application:**
    ```bash
    python ai_sql_assistant.py
    ```

2.  **Enter Table Name:**
    The assistant will first prompt you to enter the name of the table you want to access.
    ```
    Please Enter name You want to access: users
    ```
    If the table doesn't exist, you'll be prompted again.

3.  **Interact with the AI:**
    Once a valid table is selected, you can start interacting with the AI by typing your requests in natural language.

    ```
    Please Enter What you want to do with users: show me all users
    (1, 'Alice', 'alice@example.com')
    (2, 'Bob', 'bob@example.com')

    Please Enter What you want to do with users: add a new user named 'Charlie' with email 'charlie@example.com'
    Success

    Please Enter What you want to do with users: commit
    Database Updated

    Please Enter What you want to do with users: quit
    ```

### Commands

* `quit` or `q`: Exits the current table interaction or the application entirely.
* `commit`: Saves any changes made to the database.

---

## Project Structure

* **`ai_sql_assistant.py`**: The main application file that handles user input, connects to the database, and interacts with the AI agent.
* **`database.py`**: Contains functions for connecting to the PostgreSQL database, checking table existence, and retrieving column names.
* **`agent.py`**: Contains the `sql_agent` function responsible for making API calls to the Gemini model to convert natural language into SQL queries.
* **`.env`**: Stores environment variables for database credentials and API keys (not included in the repository for security reasons).

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
