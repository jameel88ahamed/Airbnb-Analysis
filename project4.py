#REQUIRED LIBRARIES
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import pymongo
import pandas as pd
import plotly.express as px

#SETTING STREAMLIT PAGE CONFIGURATION
image = Image.open("Airbnb logo.jpg")
st.set_page_config(page_title="Airbnb Data Analysis | By Jameel",
                   page_icon=image,
                   layout='wide',
                   initial_sidebar_state="expanded",
                   menu_items={'About': """# This dashboard app is created by *Jameel*!
                                        Data has been gathered from mongodb atlas"""})

#CREATING MENU ITEMS
with st.sidebar:
    Menu = option_menu("Menu", ["Home", "Overview", "Explore"],
                       icons=["house","graph-up-arrow","bar-chart-line"],
                       menu_icon="menu-button-wide",
                       default_index=0,
                       styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#FF5A5F"},
                                   "nav-link-selected": {"background-color": "#FF5A5F"}})
   
#GETTING CONNECTION WITH MDB
client = pymongo.MongoClient("Enter your command key")
db = client.sample_airbnb
col = db.listingsAndReviews

#READING DATAFRAME
df = pd.read_csv('Airbnb_dataset.csv')

#HOME PAGE
if Menu == "Home":
    col1, col2 = st.columns([1,3])
    with col1:
        st.image("Airbnb.png", width=300)
    with col2:
        st.markdown("<h1 style='text-align: center; color: #FF5A5F;'>Airbnb Data Analysis and Exploration</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #FF5A5F;'>A User-Friendly Tool Using Streamlit</h2>", unsafe_allow_html=True)


    st.write(" ")
    st.write(" ")
    st.markdown("## <span style='color:#FF5A5F;'>Domain</span> : Travel Industry, Property Management and Tourism", unsafe_allow_html=True)
    st.markdown("## <span style='color:#FF5A5F;'>Technologies used</span> : Python, Pandas, MongoDB, Streamlit, & Plotly,", unsafe_allow_html=True)
    st.markdown("## <span style='color:#FF5A5F;'>Description</span> : Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences, The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. In this application going to analyze Airbnb data using Plotly, and develop interactive visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.", unsafe_allow_html=True)

# OVERVIEW PAGE
if Menu == "Overview":
    tab1,tab2 = st.tabs(["$\huge📝 DATA $", "$\huge🚀 TOP CHARTS$"])

    # DISPLAYING SAMPLE DATA OF MDB AND DATAFRAME
    with tab1:
        col1,col2 = st.columns([1,3])
        if col1.button("Click to view sample data"):
            col1.write(col.find_one())
        if col2.button("Click to view Dataframe"):
            col1.write(col.find_one())
            col2.write(df)

    #TOP ANALYSIS CHARTS OF SAMPLE_AIRBNB
    with tab2:
        col1,col2 = st.columns(2)
        with col1:
            country = st.multiselect('Select a Country',sorted(df.Country.unique()),sorted(df.Country.unique()))
            prop = st.multiselect('Select Property_type',sorted(df.Property_type.unique()),sorted(df.Property_type.unique()))
            room = st.multiselect('Select Room_type',sorted(df.Room_type.unique()),sorted(df.Room_type.unique()))
            price = st.slider('Select Price',df.Price.min(),df.Price.max(),(df.Price.min(),df.Price.max()))

        # CONVERTING THE USER INPUT INTO QUERY
        requirements = f'Country in {country} & Room_type in {room} & Property_type in {prop} & Price >= {price[0]} & Price <= {price[1]}'

        col1,col2 = st.columns(2,gap='large')
        with col1:
            # TOP 10 PROPERTY TYPES BAR CHART
            df1 = df.query(requirements).groupby(["Property_type"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
            fig = px.bar(df1,
                         title='Top 10 Property Types with listings count',
                         x='Listings',
                         y='Property_type',
                         orientation='h',
                         color='Property_type',
                         color_continuous_scale=px.colors.sequential.Agsunset_r)
            st.plotly_chart(fig,use_container_width=True)

            # TOP 10 HOSTS BAR CHART
            df2 = df.query(requirements).groupby(["Host_name"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
            fig = px.bar(df2,
                         title='Top 10 Hosts with Highest number of Listings',
                         x='Listings',
                         y='Host_name',
                         orientation='h',
                         color='Host_name',
                         color_continuous_scale=px.colors.sequential.Blackbody_r)
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig,use_container_width=True)

            #TOP 10 AVERAGE NUMBER OF REVIEWS VERSES HOSTS
            Avg_HN_NR = df.groupby('Host_name')['No_of_reviews'].mean().reset_index()
            Top_hosts = Avg_HN_NR.sort_values(by='No_of_reviews', ascending=False).head(10)
            fig = px.bar(Top_hosts, x='Host_name', y='No_of_reviews', labels={'No_of_reviews': 'Average Number of Reviews'},
                title='Top 10 Hosts with Average Number of Reviews', color_discrete_sequence=['#75FA61'])
            fig.update_layout(xaxis_title='Host Name', yaxis_title='Average Number of Reviews')
            st.plotly_chart(fig)

        with col2:
            # TOTAL LISTINGS IN EACH ROOM TYPES PIE CHART
            df3 = df.query(requirements).groupby(["Room_type"]).size().reset_index(name="counts")
            fig = px.pie(df3,
                         title='Total Listings in each Room_types',
                         names='Room_type',
                         values='counts',
                         color_discrete_sequence=px.colors.sequential.Rainbow)
            fig.update_traces(textposition='outside', textinfo='value+label')
            st.plotly_chart(fig,use_container_width=True)

            # TOTAL LISTINGS BY COUNTRY CHOROPLETH MAP
            df4 = df.query(requirements).groupby(['Country'],as_index=False)['Name'].count().rename(columns={'Name' : 'Total_Listings'})
            fig = px.choropleth(df4,
                                title='Total Listings in each Country',
                                locations='Country',
                                locationmode='country names',
                                color='Total_Listings',
                                color_continuous_scale=px.colors.sequential.Plasma)
            st.plotly_chart(fig,use_container_width=True)

            #TOP 10 AVERAGE NUMBER OF REVIEWS IN DIFFERENT ROOM TYPES
            Avg_RT_NR = df.groupby('Room_type')['No_of_reviews'].mean().reset_index()
            top_hosts = Avg_RT_NR.sort_values(by='No_of_reviews', ascending=False).head(10)
            fig = px.bar(top_hosts, x='Room_type', y='No_of_reviews', labels={'No_of_reviews': 'Average Number of Reviews'},
                title='Top 10 Room Types with Average Number of Reviews', color_discrete_sequence=['#FA6D0F'])
            fig.update_layout(xaxis_title='Room Type', yaxis_title='Average Number of Reviews')
            st.plotly_chart(fig)

# EXPLORE PAGE
if Menu == "Explore":
    st.markdown("## Explore more about the Airbnb data")

    # GETTING USER INPUTS
    country = st.multiselect('Select a Country',sorted(df.Country.unique()),sorted(df.Country.unique()))
    prop = st.multiselect('Select Property_type',sorted(df.Property_type.unique()),sorted(df.Property_type.unique()))
    room = st.multiselect('Select Room_type',sorted(df.Room_type.unique()),sorted(df.Room_type.unique()))
    price = st.slider('Select Price',df.Price.min(),df.Price.max(),(df.Price.min(),df.Price.max()))

    # CONVERTING THE USER INPUT INTO QUERY
    requirements2 = f'Country in {country} & Room_type in {room} & Property_type in {prop} & Price >= {price[0]} & Price <= {price[1]}'

    # HEADING 1
    st.markdown("## Price Analysis")

    # CREATING COLUMNS
    col1,col2 = st.columns(2,gap='medium')

    with col1:
        # AVG PRICE BY ROOM TYPE BARCHART
        pr_df = df.query(requirements2).groupby('Room_type',as_index=False)['Price'].mean().sort_values(by='Price')
        fig = px.bar(data_frame=pr_df,
                     x='Room_type',
                     y='Price',
                     color='Price',
                     title='Average Price in each Room type')
        st.plotly_chart(fig,use_container_width=True)

        # HEADING 2
        st.markdown("## Availability Analysis")

        # AVAILABILITY BY ROOM TYPE BOX PLOT
        fig = px.box(data_frame=df.query(requirements2),
                     x='Room_type',
                     y='Availability_365',
                     color='Room_type',
                     title='Availability by Room_type')
        st.plotly_chart(fig,use_container_width=True)

        with col2:
            # AVERAGE PRICE IN COUNTRIES SCATTERGEO
            country_df = df.query(requirements2).groupby('Country',as_index=False)['Price'].mean()
            fig = px.scatter_geo(data_frame=country_df,
                                 locations='Country',
                                 color= 'Price', 
                                 hover_data=['Price'],
                                 locationmode='country names',
                                 size='Price',
                                 title= 'Average Price in each Country',
                                 color_continuous_scale='agsunset')
            col2.plotly_chart(fig,use_container_width=True)
            
            st.markdown("#   ")
            st.markdown("#   ")
            # AVERAGE AVAILABILITY IN COUNTRIES SCATTER GEO
            country_df = df.query(requirements2).groupby('Country',as_index=False)['Availability_365'].mean()
            country_df.Availability_365 = country_df.Availability_365.astype(int)
            fig = px.scatter_geo(data_frame=country_df,
                                 locations='Country',
                                 color= 'Availability_365',
                                 hover_data=['Availability_365'],
                                 locationmode='country names',
                                 size='Availability_365',
                                 title= 'Average Availability in each Country',
                                 color_continuous_scale='agsunset')
            st.plotly_chart(fig,use_container_width=True)

    # HEADING 3
    st.markdown("## Other Analysis")
    col1,col2 = st.columns(2,gap='large')
    with col1:
        #CANCELLATION POLICIES WITH NUMBER OF HOSTS
        policy_counts = df['Cancellation_policy'].value_counts()
        policy_df = pd.DataFrame({'policy': policy_counts.index, 'count': policy_counts.values})
        host_counts = df.groupby('Cancellation_policy')['Host_id'].nunique().reset_index()
        fig = px.bar(host_counts,
                    x='Cancellation_policy',
                    y='Host_id',
                    title='Cancellation Policies vs Host Count',
                    labels={'Host_id': 'Number of Hosts'},
                    color_discrete_sequence=['#FA0A51'])
        st.plotly_chart(fig)

        #HISTOGRAM PLOT OF DISTRIBUTION OF PRICES PER NIGHT
        fig = px.histogram(df, x='Price', nbins=60, title='Distribution of Prices Per Night',
                   labels={'Price': 'Price per Night'}, color_discrete_sequence=['#FF91CB'])
        st.plotly_chart(fig)

        #DISTRIBUTION OF ACCOMODATES IN DIFFERENT ROOM TYPES
        fig = px.box(df, x='Room_type', y='Accomodates', title='Distribution of Accommodates in each Room Type', color_discrete_sequence=['#ABA832'])
        fig.update_layout(
                        xaxis_title='Room_type',
                        yaxis_title='Number of Accommodates',
                    )
        st.plotly_chart(fig)

    with col2:
        #MAP SCATTER PLOTS OF DISTRIBUTION OF LISTINGS ALL OVER THE WORLD
        fig = px.scatter_mapbox(df, 
                        lat='Latitude', 
                        lon='Longitude',
                        hover_name='Name',
                        title='Distribution of Listings In Maps',
                        mapbox_style='open-street-map',
                        zoom=0.0001)
        marker_color = 'blue'
        fig.update_traces(marker=dict(color=marker_color))
        fig.update_layout(
                        margin=dict(l=0, r=0, t=30, b=0),
                        mapbox=dict(center=dict(lat=df['Latitude'].mean(), lon=df['Longitude'].mean())),
                        )
        st.plotly_chart(fig)

        #AVERAGE NIGHTS STAYED IN DIFFERENT ROOM TYPES
        avg_stay = df.groupby(['Room_type'])['Min_nights'].mean().reset_index(name='average_nights_stayed')
        fig = px.bar(avg_stay, x='Room_type', y='average_nights_stayed',
             title='Average Nights Stayed in Each Room Type',
             labels={'Room_type': 'Room Type', 'average_nights_stayed': 'Average Nights Stayed'},
             color_discrete_sequence=['#CC266E'])
        fig.update_layout(
                            xaxis_title='Room Type',
                            yaxis_title='Average Nights Stayed',)
        st.plotly_chart(fig)

        #DISTRIBUTION OF ACCOMODATES IN DIFFERENT PROPERTY TYPES
        fig = px.box(df, x='Property_type', y='Accomodates', title='Distribution of Accommodates in each Property Types', color_discrete_sequence=['#57C770'])
        fig.update_layout(
                        xaxis_title='Property_type',
                        yaxis_title='Number of Accommodates',
                    )
        st.plotly_chart(fig)
