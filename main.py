# -*- coding: utf-8 -*-
"""
This program allows to extract information from a source file.
Created on Thu Mar 25 12:24:18 2021

@author: romain Boyrie
"""

import io
import re


def searchinfile(filename, filteredfilename, regexpattern):
    """This function take a source file with text, apply a pattern to search
    the matched part of string line in the entire file.
    
    @filename : the name of the text. It must have been encoded in utf-8 to 
    be nicely printed on a utf-8 encoding system. Do not forget to add the 
    format if there is one for your file.
    
    @filteredfilename : the name of the output file. You should not forget the
    format.
    
    @regexpattern : the pattern might be given in rawstring.
    
    """

    with open(filename, encoding='utf-8') as f:
        # Loading the file in a variable
        lines = f.readlines()
        # Preparing searching operation
        p = re.compile(regexpattern)
        # Create the output file
        with io.open(filteredfilename, "w", encoding="utf-8") as f:
            for l in lines:
                ls = re.search(p, l)
                if ls:  # If there is a match
                    f.write(ls.group() + '\n')  # Add it to the output file
            f.close()  # protect memory integrity by closing operation
