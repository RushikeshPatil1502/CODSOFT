import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Created Demo Movie data

data = pd.read_excel("movies_smart_dataset.xlsx")

df = pd.DataFrame(data)

# Converted Text into numbers

vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(df["genre"])

# For Similarity Calculation

similarity = cosine_similarity(matrix)


def recommend(movie_name):
    movie_name = movie_name.lower()
    df["title_lower"] = df["title"].str.lower()

    if movie_name not in df["title_lower"].values:
        return ["Movie not found in database"]

    idx = df[df["title_lower"] == movie_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in scores[1:6]:  # top 5 (better!)
        recommendations.append(df.iloc[i[0]]["title"])

    return recommendations


movie = input("Enter a movie you like: ")
recs = recommend(movie)

print("\nRecommended movies:")
for r in recs:
    print("-", r)
