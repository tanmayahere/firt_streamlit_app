import streamlit

streamlit.title('My Moms new Healthy diner')

streamlit.header('🍞Breakfast Menu')
streamlit.text('🍇Omega3 & Blueberry')
streamlit.text('🌮Kale, Spinach')
streamlit.text('🥚Green Tea')

streamlit.header('🍒🍑Build your own Fruit breakfast Menu🍌🍍')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
