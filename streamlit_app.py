import streamlit
streamlit.header('tarun')

streamlit.title('my parents new healthy diner')
streamlit.title('my parents new healthy diner')
streamlit.text('breakfast menu')
streamlit.text('omega 3 bluberry oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('Breakfast favorites')
streamlit.text('breakfast menu')
streamlit.text(' 🥣 omega 3 bluberry oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
tps://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt
  # Display the table on the page.



