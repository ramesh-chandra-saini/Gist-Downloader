
clear

echo 'You are using Gist Downloader developed by Ramesh Chandra'
echo

echo 'Crawling gist information...'
python crawl_gist_info.py 

echo 'Extracting gist name and gist url..'
python extract_gist_url_and_name.py 

echo 'Crawling gist code using url '
python crawl_gist_code.py 

echo 'You Are Done!!!'
echo 'Go to you Desktop'
echo 'Check directory Gist_Codes_Repo '

echo 'Thanks for using Gist Downloader'
echo 'any suggestion or improvement are most welcomed'
echo 'you can reach out to me here : https://www.facebook.com/rameshc10695 '

