import requests
import os

print("Welcome to IsItDown.py!")
print("Please write a URL or URLs you want to check. (Separated by comma)")

def is_it_down(url):
  url = url.lower().lstrip().rstrip().strip()
  if 'http://' not in url:
    url = "http://" + url
  
  # print(url)
  try:
    requests.get(url)
  except:
    print(f"{url} is down!")
    return False
  print(f"{url} is up!")
  return True

answer = "y"
while(answer != "n"):
  urls = input()
  url_list = urls.split(',')
  for url in url_list:
    is_it_down(url)
  answer = input("Do you want to start over? y/n: ")