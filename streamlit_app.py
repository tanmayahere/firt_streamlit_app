import streamlit

streamlit.title('My parents new Healthy diner')

streamlit.header('🍞Breakfast Menu')
streamlit.text('🍇Omega3 & Blueberry')
streamlit.text('🌮Kale, Spinach')
streamlit.text('🥚Hard-Boiled Free-Egg')

streamlit.header('🍒🍑Build your own Fruit breakfast Menu🍌🍍')

impot pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
