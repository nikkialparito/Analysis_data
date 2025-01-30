
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
     

st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

import pandas as pd  # Import pandas with alias pd

df_reshaped = pd.read_csv('netflix_titles.csv')

# prompt: create streamlit dashboard

st.title("Netflix Dashboard")

# Display the DataFrame
st.header("Netflix Data")


# Create a bar chart showing the number of movies and TV shows
st.header("Number of Movies and TV Shows")
st.plotly_chart(fig)


# Create a scatter plot showing the relationship between release year and rating
st.header("Relationship between Release Year and Rating")
fig = px.scatter(df, x="release_year", y="rating")
st.plotly_chart(fig)

# Create a map showing the distribution of content by country
st.header("Distribution of Content by Country")
country_counts = df["country"].value_counts().reset_index()
country_counts.columns = ["Country", "Count"]

# Handle cases where country is not specified
country_counts = country_counts[country_counts["Country"].notna()]

fig = px.choropleth(country_counts,
                    locations="Country",
                    locationmode="country names",
                    color="Count",
                    color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig)


# Create a pie chart showing the distribution of content by rating
st.header("Distribution of Content by Rating")
rating_counts = df["rating"].value_counts()
fig = px.pie(values=rating_counts.values, names=rating_counts.index)
st.plotly_chart(fig)
     
script_content = """
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
@st.cache_data
def load_data():
    file_path = "netflix_titles.csv"  # Update with your file path
    df = pd.read_csv(file_path)
    df_movies = df[df['type'] == 'Movie']  # Filter only movies
    return df_movies

df = load_data()

# Sidebar - Country Filter
st.sidebar.title("Filters")
all_countries = df['country'].dropna().unique().tolist()
selected_country = st.sidebar.selectbox("Select a Country", ["All"] + all_countries)

# Filter data based on selection
if selected_country != "All":
    df_filtered = df[df['country'] == selected_country]
else:
    df_filtered = df

# Count movies per country
movies_per_country = df_filtered['country'].value_counts()

# Main Title
st.title("📽️ Netflix Movies Dashboard")

# Show Movie Count Bar Chart
st.subheader("Number of Movies Per Country")
fig, ax = plt.subplots(figsize=(10, 5))
movies_per_country.plot(kind='bar', ax=ax, color="skyblue")
ax.set_xlabel("Country")
ax.set_ylabel("Number of Movies")
st.pyplot(fig)

# Show Table
st.subheader("Movie Data")
st.dataframe(df_filtered[['title', 'country', 'release_year', 'duration', 'rating']])

# Footer
st.markdown("🔍 **Use the sidebar to filter movies by country!**")
"""

file_path = "/content/drive/MyDrive/app.py"  # Change this if needed

with open(file_path, "w") as file:
    file.write(script_content)

print(f"Script saved as {file_path}")
