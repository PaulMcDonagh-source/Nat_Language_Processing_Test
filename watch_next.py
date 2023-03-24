# Task 38 watch_next.py

# ----- import section ------------
import spacy
#----------------------------------

# load NLP.
nlp=spacy.load("en_core_web_md")

latest_mov_watched_desc ='''Will he save their world or destroy it? 
                    When the Hulk becomes too dangerous for the earth
                    , the illuminati trick Hulk into a shuttle and launch
                    him into space to a planet where Hulk can llive in peace.
                    Unfortunately, Hulk lands on the planet Sakaar where he is
                    sold into slavery and trained as a gladiator.
                    '''

def recommend_movie(latest_mov_watched_desc):
    # Read movies.txt file and add to list.
    movie_descriptions = {}
    with open("movies.txt", "r", encoding="utf_8_sig") as file:
        data = file.readlines()
        for line in data:
            movie, description = line.strip(" ").split(":")
            movie_descriptions[movie] = description
    
    # calculate similarities between each description in movie_descriptions
    # and the latest_mov_watched_desc.
    for k,v in movie_descriptions.items():
        print(f"{k} : {v}")
    similarity_count = {}
    counter = 0
    for k,v in movie_descriptions.items():
        tokens = nlp(v)
        lmwd = nlp(latest_mov_watched_desc)
        for token1 in tokens:
            for token2 in lmwd:
                # print(token1.text, token2.text, token1.similarity(token2))
                if token1.similarity(token2) > 0.5:
                    counter += 1 
                    similarity_count[k] = counter
    
    # return movie with the highest similarity index.
    print(f"\n\nBased on the last movie you watched, your next recommended movie is: {max(similarity_count)}\n")
    
            
recommend_movie(latest_mov_watched_desc)   

