#!/usr/bin/env python

import os
import sys
import magic
import time
import fnmatch

class FileInfo(object):
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
        
        
    def match(self, exp):
        """Test whether FILENAME matches PATTERN.

        Patterns are Unix shell style:
    
        *       matches everything
        ?       matches any single character
        [seq]   matches any character in seq
        [!seq]  matches any char not in seq
    
        """
        return fnmatch.fnmatch(self.filepath, exp)
    
    def readfile(self):
        if self.is_file:
            with open(self.filepath, 'r') as _file:
                return _file.read()
            
    def __str__(self):
        return str(self.__dict__)


    
def get_files(root):
    
    for root, dirs, files in os.walk(root):
        
        for filename in files:
            filename = os.path.join(root, filename)
            if os.path.isfile(filename) or os.path.isdir(filename):            
                yield FileInfo(filename)
                    
for f in get_files('/'):
    print f
