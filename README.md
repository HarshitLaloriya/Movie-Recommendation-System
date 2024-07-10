# Movie Recommenndation System on TMDB datasets
Hello, I'm back with another exciting project. I'm hoping that this readme will speak for my work and my enthusiasm for these types of projects.
![MODEL PAGE](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/5a06603a-b151-423f-87ea-93735b8ad5f5)


# Project Overview
This project is a web-based movie recommendation system that uses a pre-trained model to suggest movies based on user input. The system is built using Flask, a Python web framework, and TMDB API to fetch movie details.


<ul>
<li>
  
 **Data Preprocessing:**  The dataset was preprocessed to extract relevant features such as movie title, genre, keywords etc. The data was then cleaned and normalized to ensure consistency and accuracy.
</li>

<li>
  
 **Similarity Calculation:**  The similarity between movies was calculated using the cosine similarity measure, which measures the cosine of the angle between two vectors. The similarity matrix was then sorted to identify the most similar movies.
</li>

<li>
  
 **Recommendation Generation:**  Given a movie, the system identifies the top three most similar movies and returns their titles and other relevant information. The system also includes a fallback recommendation in case the input movie is not found in the dataset.
</li>

<li>
  
 **Web Application:**  The recommendation model is integrated into a Flask web application, which provides a user interface for movie search and recommendation. The application uses the TMDB API to fetch movie details such as posters, banners, and overviews.
</li>
</ul>


The system uses a content-based filtering techniques to recommend movies.  Content-based filtering is used to identify similar movies based on their features. By using this technique, the system is able to provide more accurate and personalized movie recommendations to users.

Overall, the movie recommendation system I designed is a simple yet effective tool for discovering new movies based on user preferences and movie features. The system can be further improved by incorporating additional features such as user ratings, social media integration, and real-time data updates.


# Before and After, What I preplaned or What I change?
This project is truly amazing; after grasping the idea of a recommendation system, I was able to prepare for some of the fundamental tasks. Before beginning, I asked myself questions like, "How does the other recommendation system operate?", "How do they recommend movies to users?", "What kinds of recommendation systems are there?" and so on. I also learned a ton of incredible information while working on this project. Even while some things don't work out the way I had hoped, I still learn a lot about how they operate. I'm going to share my mind map with you all here. Maybe you'll enjoy it:)


![mind map](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/61ca1094-5bb7-40d3-985b-96a3b48af4de)

# Dataset
The dataset used for this project is the TMDB-5000 Dataset, which is downloaded from Kaggle.<br>
**Dataset link :** - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata


# Deployment

The recommendation model is integrated into a Flask web application, which provides a user interface for movie search and recommendation. 


![Website Design](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/6b2a2963-7f41-4a1c-9356-80c016d289dd)

The system uses the TMDB API to fetch movie information, including posters, banners, and other details. The recommended movies are displayed to the user in a JSON format, which can be easily consumed by a JavaScript frontend.


https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/55b5981f-d10b-46e7-944b-8980b185ef19

# Technologies Used
--------------------

* **Python**: The primary programming language used for this project.
* **Scikit-learn**: A machine learning library used for training and evaluating the model.
* **Flask**: A lightweight web framework used for deploying the model.
* **Pandas**: A library used for data manipulation and analysis.
* **Numpy**: A library used for scientific computing in Python 
* **Pickle**: The pickle module in Python allows you to serialize and deserialize Python objects.
* **Requests**: The requests library simplifies making HTTP requests in Python.
* **nltk**:The NLTK (Natural Language Toolkit) is a powerful library for natural language processing (NLP).
* **ast**: The ast (Abstract Syntax Trees) tool for processing trees of the Python abstract syntax grammar.
* **HTML**: The structure and content of a webpage, using tags to define elements.
* **CSS**: Styles the appearance of HTML elements, including layout, colors, and fonts.
* **Javascript** : Adds interactivity and dynamic content to webpages through scripting and programming.

  
![icons8-python-48](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/1af95d8e-0539-4b19-81d2-c96e8ab35deb)
![icons8-numpy-48](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/7ead8b54-2729-4f41-bc1e-2aff91d89feb)
![icons8-pandas-48](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/acf84a7e-e2f6-4b5d-ac4f-c7731ffbb4a0)
![scikit-learn](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/119092ae-d2d6-4cd6-ba37-c2a7e469e30b)
![icons8-flask-48](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/a55fe032-09ee-49d0-8abe-bbf78adfe36f)
![icons8-html-48](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/c53d4d94-cd55-44e1-880e-7597b1b38a0f)
![icons8-css-48](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/076144fc-a1f8-41f3-8723-f62b0f864003)
![icons8-js-48](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/f1fb53db-70f0-4b5d-90c7-6044caa38c76)
![icons8-figma-48](https://github.com/HarshitLaloriya/Movie-Recommendation-System/assets/153602422/1e3b2ba3-3c33-442f-8a6b-fbdc762d0fe3)


# Future Work
-------------

There are several ways to improve and extend this project, including:

* **Collecting more data**: Collecting more movie data to improve the accuracy and robustness of the model.
* **Experimenting with different type of recommendation system**: Trying out different machine learning  recommendation models such as collaborative filtering.
* **Improving the user interface**: Improving the user interface of the deployed model to make it more user-friendly and intuitive.
* **Imporvments in system**: The system can be further improved by incorporating additional features such as user ratings, social media integration, and real-time data updates.


<p align="center">
  <img width="268" alt="symbol" src="https://github.com/HarshitLaloriya/SMS-Classification-Model/assets/153602422/aac7df32-7c7a-46ee-9fcf-84767bc0d029">
</p>



















