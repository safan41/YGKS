import requests
import json
import re
import time

from bs4 import BeautifulSoup

BASE_URL = "https://www.naqt.com"
ENTRY_REGEX = r' \(.*\)\.'

class Link:
   def __init__(self, link: str) -> None:
      self.link = link
      self.request = requests.get(BASE_URL + self.link)
      self.soup = BeautifulSoup(self.request.text, features='lxml')
      self.entries = []

   def guess(self):
      time.sleep(0.5)
      try:
        self.process1()
      except IndexError:
         pass
      try:
         self.process2()
      except:
         print("Oops")
      return self
   
   def process1(self):
      ygklist = self.soup.select('ul.ygk')[0].find_all('li')
      for entry in ygklist:
          for term in entry.find_all_next('span'):
              if term.find_parent('li') == entry:
                  term.wrap(soup.new_tag('b'))
          self.entries.append(str(entry))

   def process2(self):
      ygklist = self.soup.select('section')
      for entry in ygklist:
         entry.contents[0].wrap(self.soup.new_tag("b"))
         self.entries.append(str(entry.contents[1]))


crequest = requests.get(BASE_URL + "/you-gotta-know/by-category.jsp")
soup = BeautifulSoup(crequest.text, features='lxml')
list = soup.find_all('section')
ygk_raw = [list[i] for i in range(2,17)]
ygklist = {}

for ygk in ygk_raw:
  current = ygk.find('h2').text
  entries = ygk.find_all('li')
  elist = []
  for entry in entries:
    step = entry.text.replace("You Gotta Know\u2026these ", "").title()
    link = Link(entry.find('a')['href'])
    print("Processing " + step)
    elist.append([re.sub(ENTRY_REGEX, "", step), link.guess().entries])
  ygklist[current] = elist


print("Done.")


json_object = json.dumps(ygklist, indent=4)
with open("ygklist.json", "w") as outfile:
    outfile.write(json_object)


print("Export Successful.")