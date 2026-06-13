from recommender.content_based import recommend, movies

movie = input("Enter movie name: ")

matches = movies[movies["title"].str.contains(movie, case=False, na=False)]

if len(matches) == 0:
    print("Movie not found!")
else:
    selected_movie = matches.iloc[0]["title"]

    print(f"\nSelected: {selected_movie}")
    print("\nRecommended Movies:\n")

    print(recommend(selected_movie))