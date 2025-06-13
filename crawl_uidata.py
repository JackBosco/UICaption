# import statements
import time
import io
import os
import csv
import asyncio
import argparse
from tqdm import tqdm
import sys
from .utils import *

parser = argparse.ArgumentParser()
    
parser.add_argument("--o", help='Absolute path of output data folder.', required=True)
parser.add_argument("--i", help='Absolute path of input url text file.', required=True)

# parse args if this script is called directly from cmd
if __name__ == '__main__': 
    args = parser.parse_args()

folder_path = args.o
url_file = args.i

# Extract all the urls to crawl from the url file
website_urls = collect_web_urls(url_file)

# Crawl all web-urls and save files with image urls, corresponding preceding and succeeding text.
asyncio.run(aextract_images(website_urls, folder_path))
