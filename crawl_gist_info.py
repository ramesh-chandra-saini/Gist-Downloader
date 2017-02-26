#!/usr/bin/env python

#__author__ = "Ramesh Chandra"

import urllib
import json
import re 

#This script make an API call to github 
#json response gist.json 
#for more info . https://api.github.com/users/rameshchandrasiraura/gists

def hitAPI(url):
    #create http request
    response = urllib.urlopen(url)
    
    #get data from json response
    data = json.loads(response.read())

    #print data
    return data
    
def storeJSON(data):
    #write json response to text file
    filename = "gist_info.json"
    #json in proper format
    jsondata = json.dumps(data, indent=4, skipkeys=True, sort_keys=True)
    #open file to write
    fd = open(filename, 'w')
    #to convert ascii
    jsondata =  jsondata.decode('utf-8')
    #write jsondata to file
    fd.write(jsondata)
    #close file 
    fd.close()

#check validity of github handle
def get_handle(attempt=0):
    attempt += 1
    #Prepare URLs with github handle
    print '\nEnter your github handle'
    handle = raw_input()
    #print 'rameshchandrasiraura'
    #handle = 'rameshchandrasiraura'
    
    git_user_name_regex = '^\w+-?\w+(?!-)$'
    if re.search(git_user_name_regex,handle):
        print 'Valid Handle : ',handle
        return handle
    else:
        print 'Invalid Handle :',handle
        if attempt>3:
            return ''
        get_handle(attempt)
#driver function
def main():

    print "Getting Url of your gists..."
   
    handle = get_handle()
     
    if handle=='':
        print 'Script stopped'
        print 'more than 3 attempts with invalid handle'
        exit()
    url = "https://api.github.com/users/"+handle+"/gists"
    print 'getting gists url...'
    #create API CALL
    data = hitAPI(url)
    
    #Store JSON into File
    storeJSON(data)
    print "Done"
    
#main function
if __name__ == "__main__":
    main()

