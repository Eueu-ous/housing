import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
Price_filter = st.slider('Minimal Median House Price', 0, 500001, 200000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose Location Type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# "Low(<=2.5)","Medium (>2.5 & <4.5)","High"
income_level = st.sidebar.radio(
    "Choose income level",
    ("Low","Medium","High")

)
if income_level == "Low":
    filtered_df = df[df['median_income']<=2.5]
elif income_level == 'Medium':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] <= 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]


filtered_df = filtered_df[(filtered_df['median_house_value'] >= Price_filter) & (filtered_df['ocean_proximity'].isin(location_filter))]


# # show on map
st.subheader('See more filters in the sidebar:')
st.map(filtered_df)


# show the plot
st.subheader('Histogram of Median House Values')
fig, ax = plt.subplots(figsize=(20, 5))
filtered_df['median_house_value'].plot.hist(bins=30)
st.pyplot(fig)
