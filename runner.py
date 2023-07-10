
from students import Student 

cass = Student("Cassidy", "E65")
stu = Student("Stuart", "E64")


print(cass.say_favourite_language("Python"))
print(cass.say_favourite_language("Java"))
print(cass.what_cohort())


from team import Team

team1 = Team("redsox",["Babe", "Kirk", "Liam"], "Larry")
team2 = Team("oilers", ["Gretzky", "Jim", "Bob"], "Walter")

team1.add_player("Mark")

print(team1.players)

print(team2.has_player("Bob"))

team1.play_game(True)
team2.play_game(False)

team1.play_game(False)
team2.play_game(True)

team1.play_game(True)
team2.play_game(False)

print( team1.points)
print( team2.points)

if team1.points > team2.points:
    print("Team 1 wins")
elif team1.points < team2.points:
     print("Team 2 wins")
else:
     print("Its a draw")









