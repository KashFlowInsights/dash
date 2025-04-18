#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install streamlit')
import streamlit as st
import pandas as pd
import numpy as np

# Mock data generation
def generate_mock_data():
   properties = ['Maple St Duplex', 'Oakwood Apartments', 'Sunset Villa', 'Lakeside Townhome', 'Pinecrest Bungalow']
   months = ['Jan', 'Feb', 'Mar', 'Apr']

   data = {
       'Property': properties,
       'Total Units': np.random.randint(2, 10, size=5),
       'Occupied Units': np.random.randint(1, 9, size=5),
       'Monthly Rent Per Unit': np.random.randint(800, 2000, size=5),
       'Jan Rent Collected': np.random.randint(2000, 10000, size=5),
       'Feb Rent Collected': np.random.randint(2000, 10000, size=5),
       'Mar Rent Collected': np.random.randint(2000, 10000, size=5),
       'Apr Rent Collected': np.random.randint(2000, 10000, size=5),
       'Maintenance Cost YTD': np.random.randint(500, 3000, size=5),
       'Recurring Expenses YTD': np.random.randint(1000, 5000, size=5)
   }

   df = pd.DataFrame(data)
   df['Total Revenue YTD'] = df[[f'{month} Rent Collected' for month in months]].sum(axis=1)
   df['Occupancy Rate'] = (df['Occupied Units'] / df['Total Units'] * 100).round(2)
   df['Net Profit YTD'] = df['Total Revenue YTD'] - df['Maintenance Cost YTD'] - df['Recurring Expenses YTD']
   return df

# Dashboard UI
def main():
   st.title("KashFlow Insights: Real Estate Dashboard")
   st.markdown("#### Property Performance Overview")

   df = generate_mock_data()
   properties = df['Property'].tolist()
   selected_property = st.selectbox("Select a Property", ["All Properties"] + properties)

   if selected_property == "All Properties":
       st.dataframe(df)
   else:
       filtered_df = df[df['Property'] == selected_property]
       st.dataframe(filtered_df)

   st.markdown("---")
   st.markdown("### Summary Charts")

   chart_data = df.set_index('Property')
   st.bar_chart(chart_data['Total Revenue YTD'])
   st.bar_chart(chart_data['Net Profit YTD'])
   st.bar_chart(chart_data['Occupancy Rate'])

if __name__ == "__main__":
   main()

