import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Rang Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)
