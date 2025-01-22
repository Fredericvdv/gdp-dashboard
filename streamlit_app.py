import streamlit as st
import pandas as pd
import plotly.express as px

# Beer categories and their respective beers
beer_categories = {
    "Light & Refreshing": ["Stella", "Grisette (White Beer)", "Silly Saison"],
    "Hoppy & Bitter": ["Lagunitas California IPA", "Duvel"],
    "Strong & Complex": ["La Guillotine", "Tête de Mort", "Kapittel Waton", "Tripel Karmeliet"],
    "Dark & Rich": ["Oester Stout", "Krab"]
}

# Add non-alcoholic drink categories
non_alcoholic_categories = {
    "Sodas": ["Cola", "Dr. Pepper"],
    "Fruit Drinks": ["Appeltizer", "Nalu"],
    "Tea": ["Ice Tea Peach"]
}

# Streamlit app layout
st.title("Hack & Beers")

# Prepare data for charts
categories = list(beer_categories.keys())
beer_counts = [len(beer_categories[category]) for category in categories]

# Prepare data for non-alcoholic drinks chart
non_alc_categories = list(non_alcoholic_categories.keys())
non_alc_counts = [len(non_alcoholic_categories[category]) for category in non_alc_categories]

# Create DataFrame for non-alcoholic drinks
non_alc_df = pd.DataFrame({
    'Category': non_alc_categories,
    'Count': non_alc_counts
})

# Prepare data for charts
df = pd.DataFrame({
    'Category': categories,
    'Count': beer_counts
})

# Pie chart using Plotly
st.subheader("Beer Categories Overview")
fig = px.pie(df, values='Count', names='Category', title='Distribution of Beers by Category')
st.plotly_chart(fig)

# Add non-alcoholic drinks pie chart
st.subheader("Non-Alcoholic Beverages Overview")
non_alc_fig = px.pie(non_alc_df, values='Count', names='Category', title='Distribution of Non-Alcoholic Drinks by Category')
st.plotly_chart(non_alc_fig)

# Display beer list with improved formatting
st.subheader("Beer List")
for category, beers in beer_categories.items():
    st.write(f"### {category}")
    for beer in beers:
        st.write(f"- {beer}")
    st.write("")  # Add spacing between categories

# Display non-alcoholic drink list
st.subheader("Non-Alcoholic Drinks List")
for category, drinks in non_alcoholic_categories.items():
    st.write(f"### {category}")
    for drink in drinks:
        st.write(f"- {drink}")
    st.write("")  # Add spacing between categories

st.markdown("---")
st.markdown("Enjoy your beer tasting session responsibly! 🍺")
