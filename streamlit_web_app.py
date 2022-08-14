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

/*
#put the first column into a list
color_list=df[0].values.tolist()
#print (color_list)

#pick list for color
option=streamlit.selectbox('Pick a sweatsuit color or style:',list(color_list))

#image caption
product_caption='Our warm, comfortable, '+option+' sweatsuit!!'

#using caption to get info from db
my_crsr.execute("select direct_url, prize, size_list, upsell_product_desc from catalog_for_website where color_or_style= "+option+";")
df2=my_crsr.fetchone()

streamlit.image(
      df2[0],
      width=400,
      caption=product_caption
     )
streamlit.write('Price:',df2[1])
streamlit.write('Sizes Available:',df2[2])
streamlit.write(df2[3])
*/
