import pandas as pd
import os

def read_text(input_text):
    """
    This function read the text to be classified.
    The input can be:
        - a path for a cvs file containing a list of texts 
        - a list of texts
        - a single text

    """
    if isinstance(input_text, str):
        if os.path.isfile(input_text):            
            return pd.read_csv(input_text).iloc[:,0].tolist()
        else:
            return [input_text]
    
    elif isinstance(input_text, list):
        return  input_text
    else :
        raise TypeError("Please provide adequate input format: a text, a list of texts or a csv file.")

