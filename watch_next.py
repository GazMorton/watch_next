import spacy
nlp = spacy.load('en_core_web_md')

# open the txt file, read the contents and split each sentence to be an index in the list
open_movies = open('T38 Semantic Similarity/movies.txt','r')
read_movies = open_movies.read()
movies_split = read_movies.split('\n')

planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a
 planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"""

# created a dictionary to store the movies as keys and their similarity score as the values 
movie_dict = {}
# function takes in the planet hulk description as an argument
def watch_next(planet_hulk):
    model_sentence = nlp(planet_hulk)
# loop through the movie description list and compare each to the model sentence  
    for sentence in movies_split:
        similarity = nlp(sentence).similarity(model_sentence)
# assign the first 7 chars as the movie key 
        movie_dict[sentence[0:7]] = similarity
# used max and zip to pull the strongest similarity only
    strongest_key = max(zip(movie_dict.values(), movie_dict.keys()))[1]
    print(f'If you enjoyed Planet Hulk, we would recommend {strongest_key}')

watch_next(planet_hulk)




