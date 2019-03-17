from urllib.request import urlopen

url = "https://www.returndates.com/"

html = urlopen(url).read().decode('utf-8')

start_tag = "<title>"
end_tag = "</title>"

start_index = html.find(start_tag) + len(start_tag)
end_index = html.find(end_tag)

print(html[start_index:end_index])
