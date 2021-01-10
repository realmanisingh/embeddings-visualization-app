import nltk

class Preprocess:
    """
    Pipeline for preprocessing text data for the various embedding algorithms.
    
    Attributes:
        text (str): the text that will be preprocessed.
    """
    def __init__(self, text):
        """
        The constructor for the Preprocess class.
     
        param text (str): the text that will be preprocessed
        """
        self.text = text
    
    
    