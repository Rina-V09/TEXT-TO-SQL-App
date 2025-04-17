from dotenv import load_dotenv
load_dotenv() #load all the environment variable

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Function to load Google Gemini Model and provide sql query as response
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response=model.generate_content([prompt[0],question])
    return response.text

#Function to retrieve Query from the sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define your prompt
prompt = ["""
You are an expert in converting natural language questions to SQL queries! 
The SQL database is designed for a Text-to-SQL application and contains the following table:

Table: STUDENT  
Columns: NAME, CLASS, SECTION, MARKS  

For example:

Example 1 - How many students are there in the database?  
The SQL command will be:  
SELECT COUNT(*) FROM STUDENT;

Example 2 - Retrieve all students studying in the Data Science class.  
The SQL command will be:  
SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

Example 3 - Find all students in section 'A' with marks above 80.  
The SQL command will be:  
SELECT * FROM STUDENT WHERE SECTION = 'A' AND MARKS > 80;

Ensure the generated SQL query is **correct, optimized, and does not include unnecessary keywords**.  
The SQL query should not contain extra symbols like ``` at the beginning or end.
"""]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL Query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

## If submit is Clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is: ")
    for row in response:
        print(row)
        st.header(row)

def load_css(file_name):
    with open(file_name, "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Call this function after setting up Streamlit
load_css("style.css")
