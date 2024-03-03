import spacy
nlp = spacy.load('en_core_web_md')

# Read the text file with the list of movies.
movies_file = open("movies.txt")
movies_list = []
for movie in movies_file:
    movies_list.append(movie)

#print(movies_list)


# Create a function to return which movies a user would watch next if they have watched "Planet Hulk".
# Return the title of the most similar movie.
def movie_recommendation(description):
    description = nlp(description)
    max_similarity = 0
    title_recommendation = ""
    for movie in movies_list:
        similarity = nlp(movie).similarity(description)
        # Check if the similarity score is higher than the previous one.
        if (similarity > max_similarity):
            max_similarity = similarity
            title_recommendation = movie
    return title_recommendation

print(movie_recommendation("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."))
