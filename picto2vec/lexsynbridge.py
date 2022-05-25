import pandas as pd
import numpy as np

class LexSynBridge:
    def __init__(self, filename):
        self.df = pd.read_csv("data/lex2syn_original.csv", names=[ "lexunit", "synset"])
        self.init_conversion_dict()
    
    def init_conversion_dict(self):
        self.syn2lex_dict = {}
        for index, row in self.df.iterrows():
            synset = row["synset"]
            lexunit = row["lexunit"]
    
            if not synset in self.syn2lex_dict:
                self.syn2lex_dict[synset] = []
            
            self.syn2lex_dict[synset].append(lexunit)
        
    def syn2lex(self, synset):        
        if synset not in self.syn2lex_dict:
            if type(synset) != float:
                print(f"{synset} to lexunit failed!")
                return False
            else:
                return np.nan
        else:
            return ",".join(self.syn2lex_dict[synset])