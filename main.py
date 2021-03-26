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

    :param filename: the name of the text. It must have been encoded in utf-8 to
    be nicely printed on a utf-8 encoding system. Do not forget to add the
    format if there is one for your file.
    :param filteredfilename: the name of the output file. You should not forget the
    format.
    :param regexpattern:  the pattern might be given in rawstring.
    :return:
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

def addinfile(filename, filteredfilename, regexpattern, regexsubstitution):
    """

    :param filename:
    :param filteredfilename:
    :param regexpattern:
    :param regexsubstitution:
    :return:
    """
    with open(filename, encoding='utf-8') as f:
        # Loading the file in a variable
        lines = f.readlines()
        # Creation of the output file
        with io.open(filteredfilename, "w", encoding="utf-8") as f:
            for line in lines:
                transformed_line = re.sub(regexpattern, regexsubstitution, line)
                if len(transformed_line) > 0:  # Controlling of an existent match, if not write as it is.
                    print(line, transformed_line)  # To Do : streaming of the output file
                    f.writelines(transformed_line)
                else:
                    f.writelines(line)
            f.close()
