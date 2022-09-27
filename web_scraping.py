import urllib

file = urlib3.urlopen("https://www.google.com")
for f in file:
    print(f.string())
