movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating":8.0
    }
]
#q1 total_number_of_movies

movies_count=len(movies)
#print("movie_count",movies_count)

#-----------------------------------------------------------------------------------------------------------

#q2 movies with genre Drama

genre_filter=[m.get("title") for m in movies if "Drama" in m.get("genres")]

#print(genre_filter)

#-----------------------------------------------------------------------------------------------------------

#q3 latest movie

def get_year(mov):

    return mov.get("year")

latest_movie_data=max(movies,key=get_year)

latest_movies=[m.get("title")for m in movies if m.get("year")==latest_movie_data.get("year")]

#print(latest_movies)

#-----------------------------------------------------------------------------------------------------------

#q4 top movie (movie with higest rating)

def get_rating(mov):

    return mov.get("rating")

top_movie_data=max(movies,key=get_rating)

top_rated_movies=[m.get("title") for m in movies if m.get("rating")==top_movie_data.get("rating")]

#print(top_rated_movies)

#-----------------------------------------------------------------------------------------------------------

#q5 movies with language malayalam

malayalam_movies=[m.get("title")for m in movies if m.get("language")=="Malayalam"]

#print(malayalam_movies)

#-----------------------------------------------------------------------------------------------------------

#q6 movies released after year 2016

movies_after_2016=[m.get("title")for m in movies if m.get("year")>2016 ]

#print(movies_after_2016)

#-----------------------------------------------------------------------------------------------------------

#q7 movie with lowest rating

def get_rating(mov):

    return mov.get("rating")

least_movie_data=min(movies,key=get_rating)

least_rated_movies=[m.get("title") for m in movies if m.get("rating")==least_movie_data.get("rating")]

#print(least_rated_movies)

#-----------------------------------------------------------------------------------------------------------

#q8 malayalam movies with genere Action
def get_genres(mov):

    return mov.get("genres")

malayalam_genres_movies=[m.get("title")for m in movies if m.get("language")=="Malayalam"and m.get("genres")=="Drama"]

print(malayalam_genres_movies)

#-----------------------------------------------------------------------------------------------------------
#q9 movies releasd in same years
movie_dictionary={}

for m in movies:

    release_year=m.get("year")

    if release_year in movie_dictionary:

        movie_dictionary.get(release_year).append(m.get("title"))

    else:

        movie_dictionary[release_year]=[m.get("title")]



#print(movie_dictionary)

#-----------------------------------------------------------------------------------------------------------

# q10 oldest movie

#def get_year(mov):

   # return mov.get("year")

oldest_movie_data=min(movies,key=get_year)

oldest_movies=[m.get("title")for m in movies if m.get("year")==oldest_movie_data.get("year")]

#print(oldest_movies)

#-----------------------------------------------------------------------------------------------------------

# q11 movie name with generes either Drama or Comedy

# def get_genres(mov):

#     return mov.get("genres")

drama_or_comedy_movies=[m.get("title")for m in movies if "Comedy" in m.get("genres")or"Drama" in m.get("genres")]

print(drama_or_comedy_movies)

#-----------------------------------------------------------------------------------------------------------

#number of movies released in each year

years=[m.get("year")for m in movies]

year_count={y:years.count(y) for y in years}

#print(year_count)

#-----------------------------------------------------------------------------------------------------------

#print list of geners

genres={g for m in movies for g in m.get("genres")}

#print(genres)

#-----------------------------------------------------------------------------------------------------------

#genres and its movie count

all_genres=[g for m in movies for g in m.get("genres")]

genres_count={g:all_genres.count(g)for g in all_genres}

# print(genres_count)

#-----------------------------------------------------------------------------------------------------------

# movie name in ascendin order

sorted_movies=sorted(movies,key=lambda mov:mov.get("title"))

sorted_movie_titles=[m.get("title")for m in sorted_movies]

print(sorted_movie_titles)