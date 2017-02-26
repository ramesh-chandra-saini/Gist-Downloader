
Gist-Downloader is a python based software which can download all your gist code to ~/Desktop/Gist_Codes_Repo/

        detailed information of software:

        crawl_gist_info.py 
            input : handle 
            output : json format response from api.github.com of all gist 
                    and store it gist_info.json
        gist_info.json 
            store gist information in json format
            which is stored by crawl_gist_info.py
            
        extract_gist_url_and_name.py 
            input : gist_info.json
            output : gist_name_url.json which store only gist name and gist url
        
        gist_name_url.json 
            store gist name and gist url 
            which is manipulated by extract_url_and_name.py
        
        crawl_gist_code.py 
            input : gist_name_url.json
            Output : Create ~/Desktop/Gist_Codes_Repo/
                     Crawl all gist codes 
                     Store all crawled codes to directory
