import streamlit
import pandas

streamlit.title('Learn Python in 1 week')

streamlit.header('chapter 1: basics')


streamlit.text('Learn about variables')
streamlit.text('Learn about Loops')

streamlit.header('Buils your own fruit smoothies')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#picklist for teh fruits that are selected
fruits_selected = streamlit.multiselect("Pick some fruits:" , list(my_fruit_list.index), ['Lime'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

#display teh table on teh page
streamlit.dataframe( fruits_to_show)



