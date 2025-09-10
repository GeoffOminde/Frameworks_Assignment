import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv")
    df = df[['title', 'abstract', 'publish_time', 'journal', 'authors', 'source_x']].copy()
    df.dropna(subset=['title', 'publish_time'], inplace=True)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df.dropna(subset=['publish_time'], inplace=True)
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))
    return df

df = load_data()

# --- Streamlit Layout ---
st.title("📊 COVID-19 Research Papers Explorer")
st.write("Analysis of the CORD-19 dataset (metadata.csv)")

# Sidebar filters
years = st.sidebar.multiselect("Select Years:", sorted(df['year'].dropna().unique()), default=[2020])
filtered_df = df[df['year'].isin(years)]

# Show dataset sample
st.subheader("Sample of Data")
st.dataframe(filtered_df.head(20))

# Publications over time
st.subheader("Publications Over Time")
papers_per_year = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.lineplot(x=papers_per_year.index, y=papers_per_year.values, ax=ax)
ax.set_title("Number of Publications per Year")
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
ax.set_title("Top 10 Journals")
st.pyplot(fig)

# Word cloud of titles
st.subheader("Word Cloud of Titles")
titles_text = " ".join(filtered_df['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles_text)
fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
