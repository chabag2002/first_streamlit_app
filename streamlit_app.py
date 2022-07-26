import streamlit
import pandas

streamlit.title('Learn Python in 1 week')

streamlit.header('chapter 1: basics')


streamlit.text('Learn about variables')
streamlit.text('Learn about Loops')

streamlit.header('Buils your own fruit smoothies')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_Selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Lime','Avocado'])

fruits_to_show = my_fruit_list.loc[fruits_Selected]

#Display the table on the page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#picklist for teh fruits that are selected



