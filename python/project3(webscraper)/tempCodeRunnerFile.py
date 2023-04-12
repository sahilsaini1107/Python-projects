# specify the URL of the website you want to scrape
url = "https://leetcode.com/contest/"

# send a request to the website to get its HTML content
response = requests.get(url)