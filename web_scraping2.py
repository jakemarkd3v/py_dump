import requests


url = "https://realpython.github.io.fake-jobs/"
page = requests.get(url)
oup = Beautifulsoup(page.content, "html_parser")

print()
