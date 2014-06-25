#!/usr/bin/env python

'''
A prototype file search program
'''

import os
import magic
import fnmatch
import json

class File(object):

    '''
    Aggregates file information
    '''

    def __init__(self, filepath):
        self.depth = filepath.strip('/').count('/')
        self.is_file = os.path.isfile(filepath)
        self.is_dir = os.path.isdir(filepath)
        self.is_link = os.path.islink(filepath)
        self.size = os.path.getsize(filepath)
        self.meta = magic.from_file(filepath).lower()
        self.mime = magic.from_file(filepath, mime=True)
        self.filepath = filepath


    def filename_match(self, exp):
        """Test whether FILENAME matches PATTERN.

        Patterns are Unix shell style:

        *       matches everything
        ?       matches any single character
        [seq]   matches any character in seq
        [!seq]  matches any char not in seq

        """
        return fnmatch.fnmatch(self.filepath, exp)


    def mime_match(self, mime):
        ''' Match a file based on mime type '''
        return self.mime == mime


    def readfile(self):
        ''' Read the files contents '''
        if self.is_file:
            with open(self.filepath, 'r') as _file:
                return _file.read()

    def __str__(self):
        ''' Returns a json encoded version of __dict__ '''
        return json.dumps(self.__dict__, indent=4, sort_keys=2)

def crawl(root):
    ''' Crawl the files system '''

    for root, dirs, files in os.walk(root):

        for filename in files:
            filename = os.path.join(root, filename)
            if os.path.isfile(filename) or os.path.isdir(filename):
                yield File(filename)

for f in crawl('/home/'):
    print f

