# %% [markdown]
# # Movie Analysis - Learning to Code

# %% [markdown]
# ## Loading csv File into Data Frame

# %% [markdown]
# ### Get the necessary library to import csv into a data frame

# %%
import pandas as pd

# %% [markdown]
# ### Load the CSV into a Dataframe and print the first few rows

# %%
movies = pd.read_csv("movies.csv")
movies.head()

# %% [markdown]
# ## Health check of the data frame

# %% [markdown]
# ### Check for NAN/missing

# %%
movies.info()
movies.isna().sum()

# %% [markdown]
# ### Handle missing data

# %%
movies['Rating'] = movies['Rating'].fillna(movies['Rating'].mean())
movies['BoxOffice'] = movies['BoxOffice'].fillna(0)

# %% [markdown]
# ## Data Analysis

# %% [markdown]
# ### Average rating per Genre

# %%
avg_rating_genre = movies.groupby("Genre")['Rating'].mean()
avg_rating_genre

# %% [markdown]
# ### Top 5 movies

# %%
top_movies = movies.sort_values(by='BoxOffice', ascending=False).head(5)
top_movies[['Title','BoxOffice']]

# %% [markdown]
# ## Data Plotting

# %% [markdown]
# ### Import necessary libraries

# %%
import matplotlib.pyplot as plt

# %% [markdown]
# ### Plotting

# %%
# Bar chart: Average rating by genre
avg_rating_genre.plot(kind='bar', figsize=(8,5), title="Average Rating by Genre")
plt.ylabel("Rating")
plt.show()

# Scatter plot: BoxOffice vs Rating
plt.scatter(movies['Rating'], movies['BoxOffice'])
plt.xlabel("Rating")
plt.ylabel("Box Office")
plt.title("BoxOffice vs Rating")
plt.show()

# Histogram: Ratings distribution
movies['Rating'].hist(bins=10)
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.show()


