from urllib.request import urlopen

link = 'https://www.realpython.com/practice/dionysus.html'

link_text = urlopen(link)

text = link_text.read().decode('utf-8')

print(text)
