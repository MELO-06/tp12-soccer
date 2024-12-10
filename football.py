myfile = "Soccer_Football_Clubs_Ranking.csv"

def createtuples(filename):
    table = []
    with open(filename, 'r', encoding="utf8") as file:
        for index, line in enumerate(file):
            if index == 0:
                continue
            line = line.split(",")
            table.append(dict(ranking = line[0], name = line[1], country=line[2], point_score=line[3], year_change = line[4], previous_point=line[5], symbol_change=line[6]))
    return table

def clubsbycontry(country):
    found = False
    for index, teaminfo in enumerate(teams):
        if teaminfo["country"].lower() == country.lower():
            found = True
            print(teaminfo["name"], teaminfo["country"], teaminfo["ranking"], sep=" | ")
    if not found:
        print("No team found in the country: ", country)

def newfile_by_country (country, newfile):
    
    for index, teaminfo in enumerate(teams):
        if teaminfo["country"].lower() == country.lower():
            open(newfile, 'a').write(teaminfo["name"] + " | " + teaminfo["country"] + " | " + teaminfo["ranking"] + "\n")

def best_promotion():
    
    best_promotion = 0
    best_index = 0
    for index, teaminfo in enumerate(teams):
        if int(teaminfo["point_score"])>int(teaminfo["previous_point"]) and int(teaminfo["year_change"]) > best_promotion:
            best_promotion = int(teaminfo["year_change"])
            best_index = index
    print(teams[best_index])

def info_by_name(team_name):
    found = False
    for index, teaminfo in enumerate(teams):
        if teaminfo["name"].lower() == team_name.lower():
            print(teaminfo)
            found = True
            break
    if not found:
        print("Team not found!")

def country_ranking():
    countries = {}

    for teaminfo in teams: 
        if teaminfo["country"].lower() not in countries:
            countries[teaminfo["country"].lower()] = {"ranking_sum": 0, "team_count": 0}
        
        countries[teaminfo["country"].lower()]["ranking_sum"] += int(teaminfo["ranking"])
        countries[teaminfo["country"].lower()]["team_count"] += 1

    for country, stats in countries.items():
        average_ranking = stats["ranking_sum"] / stats["team_count"]
        countries[country] = round(average_ranking,2)

    sorted_countries = sorted(countries.items(), key=lambda item: item[1])
    #countries = sorted(countries.items, key= lambda item=item[1])
    for country_info in sorted_countries:
        print(country_info[0], country_info[1])
    

def menu():
    print("-------------------------")
    print("Select an option: ")
    print("1- List all teams")
    print("2- Clubs per Country")
    print("3- Best Promotion")
    print("4- Create a File for Country")
    print("5- Team Info")
    print("6- Countries Ranking\n")

    option = input()
    while option!= "1" and option!= "2" and option!= "3" and option!= "4" and option!= "5" and option!= "6":
        print("Your option is not valid, please try again.")
        option = input()

    if option == "1":
        print(teams)
    elif option == "2":
        country = input("What country do you want?\n")
        clubsbycontry(country)
    elif option == "3":
        best_promotion()
    elif option == "4":
        country = input("Enter country to create file for: ")
        newfile = input("Enter the name of the new file (e.g., 'germany.txt'): ")
        newfile_by_country(country, newfile)
    elif option == "5":
        team_name = input("Enter the name of the team you want info on: ")
        info_by_name(team_name)
    elif option == "6":
        country_ranking()

teams = createtuples(myfile)

#newfile_by_country("Germany", "germany.txt")
#best_promotion()
#info_by_name("FC Portos")
while True:
    menu()
