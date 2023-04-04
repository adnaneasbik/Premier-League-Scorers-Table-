import csv 
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest 

player_rank = []
more_info = []
player_club_name = []
player_name = []
goals = []
matches = []


result = requests.get("https://www.lequipe.fr/Football/championnat-d-angleterre/page-classement-individuel/buteurs")
src = result.content
soup = BeautifulSoup(src, "lxml")

players = soup.find_all("a", class_ = "Link table__playerName table__link")
players_rank = soup.find_all("td", class_ = "table__col table__col--rank")
players_name = soup.find_all("span", class_ = "min--phone-xl")
players_club_name = soup.find_all("div", class_ = "table__teamName table__link")
goals_number = soup.find_all("span", class_ = "table__sort table__col--sorted")
matches_number = soup.find_all("td", class_ = "table__col--matches")



for i in range(len(players)):
    player_rank.append(players_rank[i].text.strip())
    player_name.append(players_name[i].text.strip())
    player_club_name.append(players_club_name[i].text.strip())
    goals.append(goals_number[i].text.strip())
    matches.append(matches_number[i].text.strip())
    
    more_info.append(players[i].attrs['href'].replace('/Football/', 'https://www.lequipe.fr/Football/'))

file_list = [player_rank, player_name, player_club_name, goals, matches, more_info]
exported = zip_longest(*file_list)
with open("C:/Users/adnan/OneDrive/Desktop/csv/premier league scorers.csv", "w", encoding='UTF-8') as my_file:
        wr = csv.writer(my_file)
        wr.writerow(["Player Rank", "Player Name", "Player Club", "Goals", "Matches", "More Info"])
        wr.writerows(exported) 





