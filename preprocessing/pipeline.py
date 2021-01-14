import nltk

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
        
    
    