#!/usr/bin/env python

from disccrawler import crawl
import argparse

def main():    

    parser = argparse.ArgumentParser(description='DiscCrawler')
    parser.add_argument('root', type=str, help='The path to start searching from')
    match_help = """Test whether FILENAME matches PATTERN.
    
            Patterns are Unix shell style:
    
            *       matches everything
            ?       matches any single character
            [seq]   matches any character in seq
            [!seq]  matches any char not in seq
    
    """
    
    parser.add_argument('--pattern', help=match_help)
    args = parser.parse_args()

    
    if args.pattern:
        for this in crawl(args.root):
            if this.filename_match(args.pattern):
                print this
    
    elif not args.pattern:
          for this in crawl(args.root):
            print this
            
main()
