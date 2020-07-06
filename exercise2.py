# -*- coding: utf-8 -*-
"""
Write a Python program to read first n lines of a file

@author: erick
"""

def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',2)