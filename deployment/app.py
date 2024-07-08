from flask import Flask, request, render_template, jsonify
import pickle, requests, json

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3Mjk3ZjAxMjlhY2YwMDc1ZmFjZjViZjI4MjY3YTJiZCIsIm5iZiI6MTcyMDQyMDkxNC44NDExMzIsInN1YiI6IjY2OGI3ZTI5NzBmOTlkOGQ5ZGU1ZDAxZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kJQV99up0W6H7Cmgnvys154mqvbs9L4SdRwY1eSHiPk"
}

# loading similarities by unpicking file
similarities = pickle.load(open('similarities.pkl', 'rb'))
df = pickle.load(open('data.pkl', 'rb'))

# prediction model function
def recommendation_system(movie:str):
    movie_index = df[df['title']==movie].index[0]
    movie_similarities = similarities[movie_index]
    top_3 = sorted(enumerate(iterable=movie_similarities), reverse=True, key=lambda x:x[1])[1:4]
    recommend_movies = {str(df.loc[movie_index,'id']) : movie}
    for i in top_3:
        recommend_movies[str(df.loc[i[0],'id'])] = df.loc[i[0],'title']
    return recommend_movies

# initializing flask application
app = Flask(__name__)

# main route
@app.route(rule="/")
def main():
    return render_template("index.html")


@app.route(rule="/predict")
def predict():
    movie = request.args.get('movie')  
    recommend_movies = recommendation_system(movie)
    recommendation_movies_info = {}
    image_url_prefix = "https://image.tmdb.org/t/p/w500/"

    for i in recommend_movies.keys():
        url = f"https://api.themoviedb.org/3/movie/{i}?language=en-US"
        response = requests.get(url=url, headers=headers)
        recommendation_movies_info[str(i)] = {
            "title": response.json()['title'],
            "tagline": response.json()['tagline'],
            "vote": response.json()['vote_average'],
            "overview": response.json()['overview'],
            "poster_path": image_url_prefix + response.json()['poster_path'],
            "banner": image_url_prefix +  response.json()['backdrop_path']
        }
    print(recommendation_movies_info)
    return jsonify(recommendation_movies_info)


if __name__ == "__main__":
    app.run(debug=True)