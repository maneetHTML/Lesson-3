import re
import random
DESTINATIONS = {
    "beaches": [
        'Bali', 'Maldives', 'Phuket', 'Maui', 'Boracay', 'Cancun', 'Copacabana',
        'Bondi Beach', 'Santorini', 'Seychelles', 'Tulum', 'Waikiki Beach', 'Navagio Beach'
    ],
    "mountains": [
        'Swiss Alps', 'Rocky Mountains', 'Himalayas', 'Andes', 'Mount Fuji', 'Dolomites',
        'Carpathians', 'Caucasus Mountains', 'Atlas Mountains', 'Mount Kilimanjaro',
        
    ],
    "cities": [
        'Tokyo', 'Paris', 'New York', 'London', 'Dubai', 'Rome', 'Bangkok', 'Istanbul',
        'Barcelona', 'Singapore', 'Los Angeles', 'Amsterdam', 'Seoul', 'Berlin',
 
    ]
}

def normalize(text):
    return re.sub(r'\s+'," ",text.strip().lower())
def recommend():
    choice=normalize(input('TravelBot: Beaches,Mountains, or cities'))

    if choice not in DESTINATIONS:
        print("TravelBot: Sorry, I don't know that type.")
        return
    while True:
        suggestion=random.choice(DESTINATIONS[choice])
        print(f'TravelBot: How about {suggestion}?')
        like=normalize(input("TravelBot: Do you like it? (yes/no)"))
        if like =='yes':
            print(f'TravelBot: Great! Enjoy your trip to {suggestion}.')
            break
        elif like=='no':
            print("TravelBot: Okay,let me suggest another.")
        else:
            print("TravelBot: Please answer'yes' or 'no'. ")
def packing_tips():
    location=normalize(input("TravelBot: Where are you going?"))
    days=normalize(input("TravelBot: For how many days?"))
    print(f"TravelBot: Packing tips for {days} days in {location}:")
    print("-Versatile clothes")
    print("-Charger and adapters")
    print("-Walking shoes")
    print("-City map or travel app")
    print("-Reusable water bottle")
    print("-Light jacket or umbrella")

def show_help():
    print("I can:")
    print("- suggest destinations (type 'recommend')")
    print("- give packing tips (type 'packing')")
    print("- exit the chat (type 'exit')")
def chat():
    print("Hello! I'm TravelBot.")
    name = input("Your name? ")
    print(f"Nice to meet you, {name}!")
    show_help()
    while True:
        user = normalize(input(f"{name}: "))
        if 'recommend' in user or 'suggest' in user:
            recommend()
        elif 'pack' in user or 'packing' in user:
            packing_tips()
        elif 'help' in user:
            show_help()
        elif 'exit' in user or 'bye' in user:
            print("TravelBot: Goodbye and safe travels!")
            break
        else:
            print("TravelBot: Sorry, I didn't get that. Type 'help' for options.")

if __name__ == '__main__':
    chat()