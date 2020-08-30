# movie_recommandation
Basic movie recommendation projects to apply learning from one of the lab in the Machine Learning course of the IBM Professional Certificate

## Repository structure
In this repository you will find the following 
* At the root the Jupyter Notebook where I first tried out the algorithm.
* A Python script that consolidates the main steps of the Jupyter Notebook 
* A folder called app that contains an executable obtained by running `pyinstaller basic_movie_recommender.py`
* A Input Movies folder that contains a few example of inputs
* A Recommendations folder containing the recommendations for the user in CSV.

## Input
The app (executable) takes as an input a txt file with the user favorite movies and the user ratings of those movies. It will prompt the user to enter a username just for the sake of giving an appropriate name to the output file.

## Ouput 
The output file will be a simple CSV in which the user can find a list of movie with a recommendation for each movie.

## Dataset
The dataset that was provided by Coursera. The exact source was not specified.
The The dataset contains movies from 1874 to 2016. For each movie we have the release year and tags about the genres of the movie.

## Algorithm
Basic content-based recommendation system purely based on the tags (genres) of the movies
