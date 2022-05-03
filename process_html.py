###
#Process the html file and search the json object for all equities (etfs, stocks etc.)
###
import numpy as np
import pandas as pd
import re

class Processor:
    def __init__(self,filename):
        self.html_file=filename

    def printFileName(self):
        print(self.html_file)
    

processor = Processor("html_output.log")
processor.printFileName()