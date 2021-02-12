import nltk
nltk.download('punkt')
import re
from typing import List

class Preprocess:
    """
    Pipeline for preprocessing text data for the various embedding algorithms.
    
    Attributes:
        text (str): the text that will be preprocessed.
    """
    def __init__(self, text: str):
        """
        The constructor for the Preprocess class.
        
        Parameters:
            text (str): the text that will be preprocessed
        """
        self.text = text
    
    def lowercase(self, text: str) -> str:
        """
        Lowercases the text
        
        Parameters:
            text (str): the text that will be lowercased
        
        Returns:
            lower_text (str): the lowercased text
        """
        lower_text = text.lower()
        
        return lower_text
    
    def remove_symbols_and_numbers(self, text: str) -> str:
        """
        Removes symbols and numbers from the text
        
        Parameters:
            text (str): the text that will have symbols and numbers removed
            
        Returns:
            clean_text (str): the text that has the symbols and numbers removed
        """
        
        clean_text = re.sub('[^.?!A-Za-z]',' ', text)
        
        return clean_text
    
    def tokenize(self, text) -> List[str]:
        """
        Creates word-level tokens of each sentence in the text
        
        Parameters:
            text (str): text that has been lowercased and cleaned (symbols and numbers removed)
        
        Returns:
            tokens (List[str]): list of 
        """
        sentences = re.split('[.!?]', text)        
        tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
        
        return tokens
        
        
        
    
    
test_string = "Hello. Hello. Wherever you are. Are you dancing by the dance floor? Or drinking by the bar! 16 bands on the bed."

test_pipeline = Preprocess(test_string)
test_lower = test_pipeline.lowercase(test_string)
test_remove = test_pipeline.remove_symbols_and_numbers(test_lower)
test_tokens = test_pipeline.tokenize(test_remove)


print(test_tokens)