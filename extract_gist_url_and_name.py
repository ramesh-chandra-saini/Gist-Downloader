#!/usr/bin/env python

#__author__ = "Ramesh Chandra"

import json


#This script make an extract url and file name from gist_info.json 
#and write new json

#to get gist name and gist url
def get_gist_name_url(gist):
    gist_name,gist_url = '',''
    if 'files' in gist:
        gist_object=""
        #get gist object name
        for i in gist['files']:
            gist_object = gist['files'][i]
        #if gist_object name is not empty 
        if gist_object != "":
            if 'filename' in gist_object:
                gist_name = gist_object['filename']
            if 'raw_url' in gist_object:
                gist_url = gist_object['raw_url']
    return gist_name,gist_url
def main():
     #load gist_info.json to extract name and url of gists
    with open('gist_info.json') as data_file:    
        gist_data = json.load(data_file)
    if gist_data=='':
        print 'No gist available or invalid handle'
    
    #write gist filename and gist url to gist_name_url.json
    gist_name_url_data = []
    for gist in gist_data :
        gist_name,gist_url  = get_gist_name_url(gist)
        #if url and name are valid
        if gist_name !='' and gist_url != '':
            #print "filename : ",gist_name
            #print "url : ",gist_url    
            gist_name_url_data.append({
                'filename' : gist_name,
                'url' : gist_url 
            }) 
            
    #now dump gist name and url to gist_name_url.json
    with open('gist_name_url.json', "w") as outfile:
        json.dump(gist_name_url_data, outfile, indent=4)
         
#main function
if __name__ == "__main__":
    main()
