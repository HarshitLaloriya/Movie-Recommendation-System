from flask import Flask, request, render_template, jsonify
import pickle

# loading similarities by unpicking file
similarities = pickle.load(open('similarities.pkl', 'rb'))
df = pickle.load(open('data.pkl', 'rb'))

# prediction model function
def recommendation_system(movie:str):
    movie_index = df[df['title']==movie].index[0]
    movie_similarities = similarities[movie_index]
    top_3 = sorted(enumerate(iterable=movie_similarities), reverse=True, key=lambda x:x[1])[1:4]
    recommend_movies = dict()
    for i in top_3:
        recommend_movies[df.loc[i[0],'id']] = df.loc[i[0],'title']
    return recommend_movies.keys()

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
    return jsonify(recommend_movies)


if __name__ == "__main__":
    app.run(debug=True)