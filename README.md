# SQL Query Retrieval Using Gemini LLM

The **SQL Query Retrieval Using Gemini LLM** project is a natural language processing application that translates user queries into SQL commands and retrieves data from an SQLite database. It uses Google's Gemini LLM to interpret plain English inputs, allowing seamless interaction with databases through a user-friendly Streamlit interface.

---

![image alt](https://github.com/Ktrimalrao/Gemini-pro-sql-llm/blob/b6b4ab865a5fabdf02d082bf2698dcaa06c5172f/Screenshot%202024-12-28%20211436.png)

---

## Table of Contents
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Steps](#steps)
- [Future Enhancements](#future-enhancements)

---

## Usage
1. Launch the application using Streamlit.
2. Input your query in natural language, such as:
   - "Tell me student name."
   - "Tell me student name and class where marks less than 85."
   - "Tell me student name from class Data Science and Data Engineering."
3. View the results of the query, displayed in the app interface.

---

## Features
- **Natural Language to SQL Conversion**: Converts plain English queries into SQL commands using Google Gemini LLM.
- **Data Retrieval**: Executes the generated SQL commands to fetch results from an SQLite database.
- **Interactive Interface**: User-friendly Streamlit interface for seamless querying.
- **Preloaded Database**: Comes with a prebuilt SQLite database (`student.db`) containing sample student data.

---

## Technologies Used
- **Python**: Core programming language for application development.
- **Streamlit**: Framework for building the interactive web application.
- **SQLite**: Database system for storing and retrieving student data.
- **Google Gemini LLM**: Large language model for translating natural language queries into SQL.
- **dotenv**: For managing environment variables.

---

## Dataset
The application uses an SQLite database (`student.db`) preloaded with the following columns:
- **Name**: Student name.
- **Class**: Student's class (e.g., Data Science).
- **Section**: Section identifier.
- **Marks**: Student's marks in the subject.

Sample records:
![image alt](https://github.com/Ktrimalrao/Gemini-pro-sql-llm/blob/b6b4ab865a5fabdf02d082bf2698dcaa06c5172f/Screenshot%202024-12-28%20211620.png)

---

# Steps:
- **run :** "python sqlite.py" -- it will print all the data which will trained Gemini-pro
- **run :** "streamlit run sql.py"  -- now it will open a web page you will input Query

---

## Future Enhancements
- **Support for Multiple Databases**: Enable users to upload and interact with custom databases.
- **Advanced Query Processing**: Improve LLM prompts for handling complex SQL queries.
- **Enhanced Visualizations**: Add graphical representation of query results.
- **Mobile Compatibility**: Create a mobile app for on-the-go database querying.

---

For more details and the source code, visit the project repository.  
Simplify your database interactions today! 🚀
