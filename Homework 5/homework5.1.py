movie_duration: float = int(input("enter movie duration:"))
movie_length_hours = movie_duration // 60
movie_length_minutes = movie_duration % 60
print(f"the movie is {movie_length_hours} hours and {movie_length_minutes} minutes long")
