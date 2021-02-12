from gensim.models import Word2Vec
from typing import List
from pandas import DataFrame
from preprocessing import preprocess

def create_word2Vec(tokens: List[str]) -> DataFrame:
    """
    Creates an instance of a Word2Vec model and creates embeddings
    for the input text
    
    Parameters:
        tokens (str): List of tokens for some text
    """
    
    model = Word2Vec(sentences=tokens, size=60, sg=1, min_count=1)
    
    return model
    

test = create_word2Vec(["hello there", "I see you"])
print(list(test.wv.vocab))
