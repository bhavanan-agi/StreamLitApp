import streamlit
import pandas as pd  # Corrected pandas import
import requests
import snowflake.connector

print("Hello")
streamlit.title("My parent's new diner")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

x = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
x = x.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(x.index), ['Avocado', 'Strawberries'])
fruits_to_show = x.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())  # Corrected pandas function name
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered ', fruit_choice)

# Snowflake code here (if properly formatted)
