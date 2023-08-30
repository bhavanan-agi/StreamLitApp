import streamlit
import pandas


print("Hello")
streamlit.title("My parent's new diner")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

x=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
x = x.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:",list(x.index),['Avocado','Strawberries'])
fruits_to_show=x.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


