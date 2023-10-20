movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def highScore(movie):
    return movie["imdb"] > 5.5

def getHihgScore(movie_list):
    return list(filter(highScore, movie_list))

def category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]

def avg(movie_list):
    if not movie_list: return 0.0
    total_imdb = sum(movie["imdb"] for movie in movie_list)
    return total_imdb / len(movie_list)

def avgByCategory(movie_list, category):
    category_movies = category(movie_list, category)
    return avg(category_movies)

print(highScore(movies[0]))

high_score_movies = getHihgScore(movies)
print(high_score_movies)

thriller_movies = category(movies, "Thriller")
print(thriller_movies)

avg_imdb = avg(movies)
print("average IMDB score for all movies:", avg_imdb)

avg_imdb_thriller = avgByCategory(movies, "Thriller")
print("average IMDB score for Thriller movies:", avg_imdb_thriller)
