
capitals = {"Russia":"Moscow",
           "Germany":"Berlin",
           "Netherlands":"Amsterdam",
           "Usa":"Washington DC",
           "France":"Paris",
           "Italy":"Rome",
           "Spain":"Madrid",
           "Australia":"Canberra"}

while True:
    
    user = input()
    if user == "close" or user == "quit" or user == "q":
        break
    else:
        user = str.capitalize(user)
        print(capitals.get(user))
        

