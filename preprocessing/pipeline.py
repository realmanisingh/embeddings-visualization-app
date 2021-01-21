import nltk
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
    
    def lowercase(self) -> str:
        """
        Lowercases the text
        
        Returns:
            lower_text (str): the lowercased text
        """
        lower_text = self.text.lower()
        
        return lower_text
    
    def tokenize(self, text: str) -> List[str]:
        """
        Creates word-level tokens of the text
        
        Parameters:
            text (str): text that has been lowercased
        
        Returns:
            tokens (List[str]): list of 
        """
        
    
    
test = "Hello. Hello. Wherever you are. Are you dancing by the dance floor? Or drinking by the bar! 16 bands on the bed."
text = re.sub('[^.A-Za-z0-9]',' ', test)

print(text)