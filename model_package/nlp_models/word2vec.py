from gensim.models import Word2Vec
from typing import List
from pandas import DataFrame
from model_package.preprocessing import preprocess

def create_word2Vec(tokens: List[str]) -> DataFrame:
    """
    Creates an instance of a Word2Vec model and creates embeddings
    for the input text
    
    Parameters:
        tokens (str): List of tokens for some text
    """
    
    model = Word2Vec(sentences=tokens, size=60, sg=1, min_count=1)
    
    return model
    

test_string = "Hello. Hello. Wherever you are. Are you dancing by the dance floor? Or drinking by the bar! 16 bands on the bed."

test_pipeline = preprocess.Preprocess(test_string)
test_lower = test_pipeline.lowercase(test_string)
test_remove = test_pipeline.remove_symbols_and_numbers(test_lower)
test_tokens = test_pipeline.tokenize(test_remove)

test = create_word2Vec(test_tokens)
print(list(test.wv.vocab))
print(test['the'])
