import streamlit
import pandas

streamlit.title('Learn Python in 1 week')

streamlit.header('chapter 1: basics')


streamlit.text('Learn about variables')
streamlit.text('Learn about Loops')

streamlit.header('Buils your own fruit smoothies')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:" , list(my_fruit_list.Fruit))

streamlit.dataframe(my_fruit_list)



