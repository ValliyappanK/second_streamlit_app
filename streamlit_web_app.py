import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

#connect to snowflake
my_cnctn=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_crsr=my_cnctn.cursor()

# run a snowflake query and put it all in a var called my_catalog
my_crsr.execute("select color_or_style from catalog_for_website")
my_catalog=my_crsr.fetchall()

#put the data into a data frame
df=pandas.DataFrame(my_catalog)

#temp write the data frame
streamlit.write(df)
