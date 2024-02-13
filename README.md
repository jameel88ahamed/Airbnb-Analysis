# Introduction
  Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences, The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. Data analysis on millions of listings provided through Airbnb is a crucial factor for the company. These millions of listings generate a lot of data - data that can be analyzed and used for security, business decisions, understanding of customers' and implementation of innovative services.

# Problem Statement
  This project aims to analyze Airbnb data by extracting data from MongoDB Atlas sample_airbnb, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.

# Required Libraries
- Streamlit : To Create Graphical user Interface and build web application.
- Pymongo : To store and retrieve the data by connecting with MongoDB Atlas.
- Pandas : To Clean and maipulate the data.
- Plotly, Seaborn, Matplotlib.pyplot - To plot and visualize the data.

# Workflow:
## Step 1:
MongoDB Connection and Data Retrieval: Establishing a connection to the MongoDB Atlas database and retrieve the Airbnb dataset. Performing queries and data retrieval operations to extract the necessary information for your analysis.

## Step 2:
Data Cleaning and Preparation: Cleaning the Airbnb dataset by handling missing values, removing duplicates, and transforming data types as necessary. Preparing the dataset for EDA and visualization tasks, ensuring data integrity and consistency.

## Step 3:
Geospatial Visualization: Developing a streamlit web application that utilizes the geospatial data from the Airbnb dataset to create interactive maps. Visualizing the distribution of listings across different locations, allowing users to explore prices, ratings, and other relevant factors.

## Step 4:
Price Analysis and Visualization: Using the cleaned data to analyze and visualize how prices vary across different locations, property types, and seasons. Creating dynamic plots and charts that enable users to explore price trends, outliers, and correlations with other variables.

## Step 5:
Location-Based Insights: Investigating how the price of listings varies across different locations. Visualizing these insights on interactive maps and creating dashboards in tools like Tableau.

## Step 6:
Interactive Visualizations: Developing dynamic and interactive visualizations that allow users to filter and drill down into the data based on their preferences. Enable users to interact with the visualizations to explore specific regions, property types, or time periods of interest.

## Step 7:
Dashboard Creation: Utilizing Tableau toll to create a comprehensive dashboard that presents key insights from my analysis. Combining different visualizations, such as maps, charts, and tables, to provide a holistic view of the Airbnb dataset and its patterns.

# Results:
The following are conclusions drawn from the Exploratory Data Analysis:

- The most preferred room type is Entire home/apartment, that might be because people might want a homely atmosphere.

- Maria Host has the highest number of listings.

- Shuang is the most reviewed host

- Shared rooms have the most availability, probably because people prefer their privacy and prefer staying in entire homes or private rooms.

- The average stay in an entire home is 7 nights and private rooms & shared rooms is around 5 nights.

# Dashboard Image:
![Dashboard 1](https://github.com/jameel88ahamed/Airbnb-Analysis/assets/155420430/0d7eb135-fcf2-4e14-8e9c-c445d1f9de67)
