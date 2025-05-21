import re
import random

DESTINATIONS = {
    "beaches": [
        'Bali', 'Maldives', 'Phuket', 'Maui', 'Boracay', 'Cancun', 'Copacabana',
        'Bondi Beach', 'Santorini', 'Seychelles', 'Tulum', 'Waikiki Beach', 'Navagio Beach',
        'El Nido', 'Whitehaven Beach', 'Pink Sands Beach', 'Anse Source d’Argent', 'Varadero Beach',
        'Seven Mile Beach', 'Playa del Carmen', 'Grace Bay', 'Railay Beach', 'Lanikai Beach',
        'Eagle Beach', 'Ipanema', 'Nungwi Beach', 'Camps Bay', 'Praia da Rocha', 'Diani Beach',
        'Matira Beach', 'Clearwater Beach', 'Siargao', 'Flic en Flac', 'Coron', 'Tossa de Mar',
        'Porto Katsiki', 'La Concha Beach', 'Baia do Sancho', 'Langkawi', 'Manly Beach',
        'Fraser Island', 'Vik Beach', 'Sopot Beach', 'Red Beach (Santorini)', 'Falassarna',
        'Gili Islands', 'Luskentyre Beach', 'Isla Holbox', 'Noosa Main Beach', 'Playa Blanca'
    ],
    "mountains": [
        'Swiss Alps', 'Rocky Mountains', 'Himalayas', 'Andes', 'Mount Fuji', 'Dolomites',
        'Carpathians', 'Caucasus Mountains', 'Atlas Mountains', 'Mount Kilimanjaro',
        'Mount Everest', 'Mount Elbrus', 'Denali (Mount McKinley)', 'Matterhorn',
        'Mount Rainier', 'Mount Cook', 'Mount Etna', 'Table Mountain', 'Mount Ararat',
        'Mount Olympus', 'Zugspitze', 'Mount Kosciuszko', 'Sierra Nevada (Spain)',
        'Mount Roraima', 'Drakensberg', 'Mount Kenya', 'Pico Duarte', 'Mount Aconcagua',
        'Tatra Mountains', 'Mount Sinai', 'Mount Shasta', 'Mount Hood', 'Mount St. Helens',
        'Annapurna', 'Mount Meru', 'Picos de Europa', 'Mount Kinabalu', 'Mount Toubkal',
        'Mount Ngauruhoe', 'Ben Nevis', 'Mount Washington', 'Sayan Mountains',
        'Mount Damavand', 'Gunnbjørn Fjeld', 'Mount Cameroon', 'Mount Erebus',
        'Mount Baker', 'Mauna Kea', 'Mount Pelee', 'Mount Bromo'
    ],
    "cities": [
        'Tokyo', 'Paris', 'New York', 'London', 'Dubai', 'Rome', 'Bangkok', 'Istanbul',
        'Barcelona', 'Singapore', 'Los Angeles', 'Amsterdam', 'Seoul', 'Berlin',
        'Vienna', 'Madrid', 'Sydney', 'Toronto', 'San Francisco', 'Moscow', 'Lisbon',
        'Prague', 'Venice', 'Florence', 'Hong Kong', 'Chicago', 'Beijing', 'Kuala Lumpur',
        'Buenos Aires', 'Cairo', 'Cape Town', 'Athens', 'Stockholm', 'Dublin', 'Lima',
        'Warsaw', 'Oslo', 'Helsinki', 'Edinburgh', 'Montreal', 'Doha', 'Jerusalem',
        'Jakarta', 'Budapest', 'Mexico City', 'Reykjavik', 'Brussels', 'Manila', 'Bogotá',
        'San Diego'
    ]
}

def normalize(text):
    return re.sub(r'\s+', " ", text.strip().lower())

def print_all_packing_tips():
    print("\nPacking tips for mountains:")
    print("- Thermal wear and layers")
    print("- Hiking boots")
    print("- Sunscreen and sunglasses")
    print("- First aid kit")
    print("- Backpack with water bottle")
    print("- Map or GPS device")

    print("\nPacking tips for cities:")
    print("- Versatile clothes")
    print("- Charger and adapters")
    print("- Walking shoes")
    print("- City map or travel app")
    print("- Reusable water bottle")
    print("- Light jacket or umbrella")

    print("\nPacking tips for beaches:")
    print("- Swimwear")
    print("- Sunscreen and hat")
    print("- Flip-flops or sandals")
    print("- Towel or beach mat")
    print("- Sunglasses")
    print("- Waterproof bag\n")

def recommend():
    # Always print packing tips first
    print_all_packing_tips()

    choice = normalize(input('TravelBot: Beaches, Mountains, or Cities? '))
    if choice not in DESTINATIONS:
        print("TravelBot: Sorry, I don't know that type.")
        return

    while True:
        suggestion = random.choice(DESTINATIONS[choice])
        print(f'TravelBot: How about {suggestion}?')
        like = normalize(input("TravelBot: Do you like it? (yes/no) "))
        if like == 'yes':
            print(f'TravelBot: Great! Enjoy your trip to {suggestion}.')
            break
        elif like == 'no':
            print("TravelBot: Okay, let me suggest another.")
        else:
            print("TravelBot: Please answer 'yes' or 'no'.")

def packing_tips():
    location = normalize(input("TravelBot: Where are you going? "))
    days = normalize(input("TravelBot: For how many days? "))
    print(f"\nTravelBot: Packing tips for {days} days in {location}:")

    print("\nIf you are going to the mountains, pack:")
    print("- Thermal wear and layers")
    print("- Hiking boots")
    print("- Sunscreen and sunglasses")
    print("- First aid kit")
    print("- Backpack with water bottle")
    print("- Map or GPS device")

    print("\nIf you are going to a city, pack:")
    print("- Versatile clothes")
    print("- Charger and adapters")
    print("- Walking shoes")
    print("- City map or travel app")
    print("- Reusable water bottle")
    print("- Light jacket or umbrella")

    print("\nIf you are going to the beach, pack:")
    print("- Swimwear")
    print("- Sunscreen and hat")
    print("- Flip-flops or sandals")
    print("- Towel or beach mat")
    print("- Sunglasses")
    print("- Waterproof bag")

def show_help():
    print("\nI can:")
    print("- Suggest destinations (type 'recommend')")
    print("- Give packing tips (type 'packing')")
    print("- Exit the chat (type 'exit')")

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
