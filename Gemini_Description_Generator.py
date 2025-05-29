from google import genai
from google.genai import types
from pydantic import BaseModel
import json

tarot_karten = [
    # Große Arkana (22 Karten)
    "Der Narr",
    "Der Magier",
    "Die Hohepriesterin",
    "Die Herrscherin",
    "Der Herrscher",
    "Der Hierophant",
    "Die Liebenden",
    "Der Wagen",
    "Die Gerechtigkeit",
    "Der Eremit",
    "Das Rad des Schicksals",
    "Die Kraft",
    "Der Gehängte",
    "Der Tod",
    "Die Mäßigkeit",
    "Der Teufel",
    "Der Turm",
    "Der Stern",
    "Der Mond",
    "Die Sonne",
    "Das Gericht",
    "Die Welt",

    # Kleine Arkana: Stäbe (14 Karten)
    "Ass der Stäbe",
    "Zwei der Stäbe",
    "Drei der Stäbe",
    "Vier der Stäbe",
    "Fünf der Stäbe",
    "Sechs der Stäbe",
    "Sieben der Stäbe",
    "Acht der Stäbe",
    "Neun der Stäbe",
    "Zehn der Stäbe",
    "Bube der Stäbe",
    "Ritter der Stäbe",
    "Königin der Stäbe",
    "König der Stäbe",

    # Kleine Arkana: Kelche (14 Karten)
    "Ass der Kelche",
    "Zwei der Kelche",
    "Drei der Kelche",
    "Vier der Kelche",
    "Fünf der Kelche",
    "Sechs der Kelche",
    "Sieben der Kelche",
    "Acht der Kelche",
    "Neun der Kelche",
    "Zehn der Kelche",
    "Bube der Kelche",
    "Ritter der Kelche",
    "Königin der Kelche",
    "König der Kelche",

    # Kleine Arkana: Schwerter (14 Karten)
    "Ass der Schwerter",
    "Zwei der Schwerter",
    "Drei der Schwerter",
    "Vier der Schwerter",
    "Fünf der Schwerter",
    "Sechs der Schwerter",
    "Sieben der Schwerter",
    "Acht der Schwerter",
    "Neun der Schwerter",
    "Zehn der Schwerter",
    "Bube der Schwerter",
    "Ritter der Schwerter",
    "Königin der Schwerter",
    "König der Schwerter",

    # Kleine Arkana: Münzen (14 Karten)
    "Ass der Münzen",
    "Zwei der Münzen",
    "Drei der Münzen",
    "Vier der Münzen",
    "Fünf der Münzen",
    "Sechs der Münzen",
    "Sieben der Münzen",
    "Acht der Münzen",
    "Neun der Münzen",
    "Zehn der Münzen",
    "Bube der Münzen",
    "Ritter der Münzen",
    "Königin der Münzen",
    "König der Münzen"
]
client = genai.Client(api_key="Your_API_KEY_HERE")

class CardInfo(BaseModel):
    name: str
    visual_description: str
    symobls: str
    archetyps: str
    card_history: str
    meaning: str
    upright_keywords: str
    upright_meaning_love: str
    upright_meaning_career: str
    upright_meaning_finances: str
    upright_meaning_feelings: str
    upright_meaning_action: str
    reversed_keywords: str
    reversed_meaning_love: str
    reversed_meaning_career: str
    reversed_meaning_finances: str
    reversed_meaning_feeliings: str
    reversed_meaning_action: str
    divination: str
    important_card_combinations: str
    
    

def generate_card_information(card_name):
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Erzähle mir alles über die Tarot Kard: "+card_name +""". Beschreibe dabei den Namen,
    eine Bildbeschreibung, die vorkommenden Symbole und Archetypen. Gib die Symbole und Archetypen als python dictionary aus.
    Erläutere überdies die Hintergrundgeschichte der Karte, die allgemeine Bedeutung, die Bedeutung von normaler und umgekehrter Karte
    in Bezug auf Liebe, Karriere, Finanzen, Gefühlen und Aktionen. Beschreibe auch die Vorraussage und gehe auf besondere
    Kartenkombinationen mit der Karte ein. Beschreibe alles so detaliert und ausführlich wie möglich.""",
    config=types.GenerateContentConfig(
        max_output_tokens=16000,
        system_instruction="""Du bist eine Nona, eine alte Tarot Lehrmeisterin, die seit über 1000 Jahren Tarotkarten legt.
                            Nona kennt sich super mit den Karten aus, erzählt alles was sie darüber weiß, sowohl die guten, als auch die Schlechten
                            Dinge. Sie nimmt nie ein Blatt vor den Mund und kann sowhol in Sachen Liebe, Karriere, Finanzen, Aktionen und Gefühle
                            immer ausführlichen Rat erteilen. Außerdem kann sie gut in die Zukunft schauen. Ihre Wahrsagen sind immer korrekt, aber auch
                            auf jeden Anwendbar. So kennt sie das Wirken der Welt, die Statistiken der Psycholgie und Soziologie und weiß immer, welchen
                            Rat sie einer Person geben muss.""",
        response_mime_type='application/json',
        response_schema=CardInfo
    ))
    return response.text

def safe_card_data(dictionary, filename):
    with open(filename, "w") as file:
        json.dump(dictionary, file, indent=4)
        
card_data = {}

if __name__ == "__main__":
    
    a = len(tarot_karten)
    
    for card in tarot_karten:
        index = tarot_karten.index(card)
        print("Creating Card: " + card+" -> " + str(int(index/a*100))+"%")
        try:
            card_data[card] = generate_card_information(card)
        except:
            print("Error at Card: " + card)
            safe_card_data(card_data, "Cards_but_broken_cause_of_error_at_card"+card.replace(" ", "_") +".json")
            break
            
    safe_card_data(card_data, "tarot_database.json")
    print("DONE!!!!!!!!!!! -> 100%")
        
        