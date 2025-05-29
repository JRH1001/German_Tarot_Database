import json

tarot_cards = {}
with open("tarot_database.json") as file:
    data = json.load(file)
for card in data:
    tarot_cards[card] = json.loads(data[card])
    
with open("tarot_database_formated.json", "w") as file:
    json.dump(tarot_cards, file, indent=4)
    
    
    