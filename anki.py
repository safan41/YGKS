import genanki
import json
import os
import random

CATEGORIES = {
   "FA": ["Visual Art", "Performance", "Music and Auditory Art"],
   "HISTORY": ["History"],
   "LIT": ["Literature"],
   "RMPSS": ["Geography", "Mythology", "Philosophy", "Religion", "Social Science"],
   "SCI": ["Science", "Mathematics"],
   "TRASH": ["Miscellaneous", "Popular Culture", "Sports"]
}

SETS = {}

class InfoSet(genanki.Note):
  def __init__(self, set, model=genanki.CLOZE_MODEL, sort_field=None, tags=None, guid=None, due=0):
     super().__init__(model, [set,''], sort_field, tags, guid, due)

  @property
  def guid(self):
    return genanki.guid_for(self.fields[0], self.fields[1])

for file in os.scandir('export'):
    if file.is_file():
        print("Ran")
        SETS[file.path.removesuffix(".json")] = json.load(open(file.path))

print(SETS)

# INFOS: list[genanki.Note] = []
# for category in CATEGORIES:
#    for sub in category:
#       SETS: list[dict[str]] = []
#       for set in SETS:
#          deck = genanki.Deck(
#             random.randrange(1 << 30, 1 << 31),
#             set.keys()[0]
#          )
#          for info in INFOS:
#             deck.add_note(info)
#          export = '/export/anki/{}.apkg'.format(set.keys()[0])
#          genanki.Package(deck).write_to_file(export)
#          print("Generated "+ export)
#       print("SUBCATEGORY " + sub + " FINISHED!!!")
#    print("!!!CATEOGRY " + category + "FINISHED!!!!")
