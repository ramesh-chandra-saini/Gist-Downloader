
**Gist-Downloader is a python based software which can download all your gist code to ~/Desktop/Gist_Codes_Repo/**


-------------------------------------------------------------------------------

                         Gist-Downloader
    
                      Author : Ramesh Chandra
    
                        Final Year CSE BTech
    
                    National Institute of Technology
    
                         Karnataka Surathkal
    
-------------------------------------------------------------------------------


### What is this repository for? ###

* Gist-Downloader summary
     - **Gist-Downloader is a python based software which can download all your gist code to ~/Desktop/Gist_Codes_Repo/**.
     - **Gist - Gist is a simple way to share snippets and pastes with others using github**
     - Developer
          - **[Ramesh Chandra](https://www.linkedin.com/in/ramesh-chandra-saini/)**
* Version 
      - 1.0


### How do I run this software? ###

* Clone this repo
* Run run.sh (bash run.sh)

### Who can use it? ###

* Any ubuntu OS user

### Who do I talk to? ###

* Repo owner or admin
    - Ramesh Chandra
    - rameshc10695@gmail.com
    - 8546896750
    - [Facebook](https://www.facebook.com/rameshc10695)


### Detailed information of Gist-Downloader: ###

* crawl_gist_info.py
     - input : github handle .
     - output : json format response from api.github.com of all gist 
                    and store response into gist_info.json

* extract_gist_url_and_name.py 
     - input : gist_info.json .
     - output : gist_name_url.json which store only gist name and gist url

* crawl_gist_code.py 
     - input : gist_name_url.json.
     - Output : Create **~/Desktop/Gist_Codes_Repo/**
                     Crawl all gist codes 
                     Store all crawled codes to directory
     
* gist_info.json 
        - store gist information in json format
            which is stored by crawl_gist_info.py
 
 * gist_name_url.json
     - store gist name and gist url 
            which is manipulated by extract_url_and_name.py
          
