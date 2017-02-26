#!/usr/bin/env python

#__author__ = "Ramesh Chandra"

import urllib
import json
import os
import platform
import subprocess
import os.path


import os.path
import json
from pprint import pprint

import urllib
from bs4 import BeautifulSoup

import shutil

#This script make an API call to github 
#json response gist.json 
#for more info . https://api.github.com/users/rameshchandrasiraura/gists

#extract gist code  content from url 
def hitGithub(url):
    gist_code = urllib.urlopen(url).read()
    return gist_code

#driver function
def main():
    #create directory
    print 'Creating Directory..'
    desktop = os.path.expanduser('~') + '/Desktop/'
    directory = desktop+'Gist_Codes_Repo/'
    
    #create Gist_Codes_Repo if not present
    if not os.path.exists(directory):
        os.makedirs(directory)
   
   #load gist_name_url.json
    with open('gist_name_url.json') as gist_file:    
        gist_name_url_data = json.load(gist_file)
    
    print 'Crawling your gist repo...'
    for gist in gist_name_url_data:
        gist_file_name = gist['filename']
        gist_url = gist['url']
        print "[Gist Name] => ",gist_file_name
        
        gist_code = hitGithub(gist_url)
        gist_code_file  = open(directory+gist_file_name,'w')
        gist_code_file.write(gist_code)
        gist_code_file.close()     
     
    print "Done"
    print "your all code are stored in "+directory
#main function
if __name__ == "__main__":
    main()

