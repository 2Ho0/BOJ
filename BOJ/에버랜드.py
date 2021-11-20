import random

name = ["호영","성원","승준","원진","해빈","수정","민정","지민","민수","현지","규리"]
team1 = random.sample(name,6)
print(team1)

team2 = list(set(name)-set(team1))
print(team2) 


