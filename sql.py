from dotenv import load_dotenv
load_dotenv()  ## Load all the Environment(venv) variable
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

## Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google GEMINI_MODEL & Provide response as Query
def get_gemini_response(question,promt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([promt[0],question])
    return response.text

## Function to retrive Query from DataBase
def read_sql_query(sql,db):
    connection = sqlite3.connect(db)
    curs = connection.cursor()
    curs.execute(sql)
    rows = curs.fetchall()
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    
    """
]

## Streamlit app
st.set_page_config(page_title='I can retrive any SQL query')
st.header("Gemini App to Retrive SQL Data")

question = st.text_input("Input",key='input')
submit = st.button("Ask the question")

## If Click in submit:
if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    response = read_sql_query(response,"student.db")
    st.subheader("The Response is : ")
    for row in response:
        print(row)
        st.header(row)
    