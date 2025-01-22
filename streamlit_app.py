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

# Streamlit app layout
st.title("Beer Tasting Presentation 🍺")
st.write("Explore the beers categorized for your tasting experience.")

# Prepare data for charts
categories = list(beer_categories.keys())
beer_counts = [len(beer_categories[category]) for category in categories]

# Prepare data for charts
df = pd.DataFrame({
    'Category': categories,
    'Count': beer_counts
})

# Pie chart using Plotly
st.subheader("Beer Categories Overview")
fig = px.pie(df, values='Count', names='Category', title='Distribution of Beers by Category')
st.plotly_chart(fig)

# Display beer list with improved formatting
st.subheader("Beer List")
for category, beers in beer_categories.items():
    st.write(f"### {category}")
    for beer in beers:
        st.write(f"- {beer}")
    st.write("")  # Add spacing between categories

# Dropdown selection for detailed view
st.sidebar.header("Select a Beer")
selected_category = st.sidebar.selectbox("Choose a category:", categories)
selected_beer = st.sidebar.selectbox("Choose a beer:", beer_categories[selected_category])

# Show selected beer details
st.sidebar.write(f"You selected **{selected_beer}** from the '{selected_category}' category.")

st.markdown("---")
st.markdown("Enjoy your beer tasting session responsibly! 🍺")
