# importing required libraries 
from flask import Flask, request, render_template, jsonify
import pickle, requests

# TMDB ->API headers
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3Mjk3ZjAxMjlhY2YwMDc1ZmFjZjViZjI4MjY3YTJiZCIsIm5iZiI6MTcyMDQyMDkxNC44NDExMzIsInN1YiI6IjY2OGI3ZTI5NzBmOTlkOGQ5ZGU1ZDAxZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kJQV99up0W6H7Cmgnvys154mqvbs9L4SdRwY1eSHiPk"
}

# loading similarities by unpicking file
similarities = pickle.load(open('similarities.pkl', 'rb'))
df = pickle.load(open('data.pkl', 'rb'))

# prediction model function
def recommendation_system(movie:str):
    if  (df[df['title']==movie].index.empty) == True:
        return "Movie Not Found"
    else:
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


# route for search
@app.route(rule="/predict")
def predict():

    # movie name coming from website input.
    movie = request.args.get('movie') 
    # applying function on the movie. 
    recommend_movies = recommendation_system(movie.title())
    
    # if movie not found in dataframe['title']
    if recommend_movies == "Movie Not Found":
        # sending json to js
        return jsonify({"output" : "None"})
    

    # if movie found in dataframe['title']
    else:
        # object to send to js in json format 
        recommendation_movies_info = {}
        
        # image link prefix
        image_url_prefix = "https://image.tmdb.org/t/p/w500/"

        for x,i in enumerate(recommend_movies.keys()):
            
            # API-> return's the data of movie
            url = f"https://api.themoviedb.org/3/movie/{i}?language=en-US"
            response = requests.get(url=url, headers=headers)

            # filling json with important attributes only
            recommendation_movies_info[str(x)] = {
                "title": response.json()['title'],
                "tagline": response.json()['tagline'],
                "vote": response.json()['vote_average'],
                "overview": response.json()['overview'],
                "poster_path": image_url_prefix + response.json()['poster_path'],
                "banner": image_url_prefix +  response.json()['backdrop_path'],
                "homepage": response.json()['homepage']
            }
            # sometimes the homepage attribute return's ("") empty string
            # so we are checking if homepage is empty or not
            # if homepage link is empty then redirecting search to Google. 
            if recommendation_movies_info[str(x)]['homepage'] == "":
                recommendation_movies_info[str(x)]["homepage"] =  ("https://www.google.com/search?q=" + response.json()['title'].replace(" ", "+"))
        
        # sending json to js
        return jsonify(recommendation_movies_info)

"""The line if __name__ == "__main__": is a common construct in Python scripts. Let’s break down what it means and why it’s used:

Purpose:
The purpose of this construct is to differentiate between whether a Python script is being executed as the main program or if it is being imported as a module into another script.
It helps prevent unintended execution of code when a script is imported.

Explanation:
When Python runs a script, it sets a special variable called __name__.
If the script is the main program being executed directly (not imported), __name__ is set to "__main__".
If the script is imported as a module into another program, __name__ is set to the name of the module (e.g., the filename without the .py extension).

Usage:
The code block following if __name__ == "__main__": will only run when the script is executed directly (as the main program).
It won’t run when the script is imported as a module."""

if __name__ == "__main__":
    app.run(debug=True)