import pandas as pd
import numpy as np

def main(input_csv,username):
    movies_df=pd.read_csv('movies.csv')

    ##Preprocessing
    #Using regular expressions to find a year stored between parentheses
    #We specify the parantheses so we don't conflict with movies that have years in their titles
    movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))',expand=False)
    #Removing the parentheses
    movies_df['year'] = movies_df.year.str.extract('(\d\d\d\d)',expand=False)
    #Removing the years from the 'title' column
    movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '')
    #Applying the strip function to get rid of any ending whitespace characters that may have appeared
    movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
    #Every genre is separated by a | so we simply have to call the split function on |
    movies_df['genres'] = movies_df.genres.str.split('|')
    #Copying the movie dataframe into a new one since we won't need to use the genre information in our first case.
    moviesWithGenres_df = movies_df.copy()

    #For every row in the dataframe, iterate through the list of genres and place a 1 into the corresponding column
    for index, row in movies_df.iterrows():
        for genre in row['genres']:
            moviesWithGenres_df.at[index, genre] = 1
    #Filling in the NaN values with 0 to show that a movie doesn't have that column's genre
    moviesWithGenres_df = moviesWithGenres_df.fillna(0)

    inputMovies=pd.read_csv(input_csv)
    inputMovies.columns=('title','rating')
    #Filtering out the movies by title
    inputId = movies_df[movies_df['title'].isin(inputMovies['title'].tolist())]
    #Then merging it so we can get the movieId. It's implicitly merging it by title.
    inputMovies = pd.merge(inputId, inputMovies)

    #Filtering out the movies from the input
    userMovies = moviesWithGenres_df[moviesWithGenres_df['movieId'].isin(inputMovies['movieId'].tolist())]
    #Resetting the index to avoid future issues
    userMovies = userMovies.reset_index(drop=True)
    #Dropping unnecessary issues due to save memory and to avoid issues
    userGenreTable = userMovies.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)
    #Dot produt to get weights
    userProfile = userGenreTable.transpose().dot(inputMovies['rating'])
    #Now let's get the genres of every movie in our original dataframe
    genreTable = moviesWithGenres_df.set_index(moviesWithGenres_df['movieId'])
    #And drop the unnecessary information
    genreTable = genreTable.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)

    #Multiply the genres by the weights and then take the weighted average
    recommendationTable_df = ((genreTable*userProfile).sum(axis=1))/(userProfile.sum())
    recommended_movies=recommendationTable_df.to_frame('recommendation')

    #Putting the output into a dataframe & export into a CSV
    recommended_movies=recommended_movies.merge(how='left', on='movieId',right=movies_df)
    recommended_movies.sort_values(by='recommendation', ascending=False, inplace=True)
    recommended_movies.to_csv(username+'_recommended_movies.csv')

input_csv=input('Enter path to CSV : ')
username=input('Enter your Use Name : ')

main(input_csv,username)
    
