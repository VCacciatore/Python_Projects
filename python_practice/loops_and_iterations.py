# for loop example
plays = ["Romeo and Juliet", "Hamlet", "Macbeth", "Othello", "King Lear"]
for play in plays:
    print(f"{play} is a tragedy")
print()

# range() function
numbers = range(1,6)
for num in numbers:
    print(num) # notice it is first number incluseive, last number exclusive
print()
even_nums = range(2, 11, 2) # optional third argument for step sized
for en in even_nums:
    print(en)
print()
squares = [] # empty list declaration
for val in range (1, 11):
    squares.append(val ** 2)
print(squares)
print()

# list selection
print(plays[0:3]) # prints elements 0-2
print(plays[1:4]) # prints elements 1-3
print(plays[2:]) # prints elements 2 - end
print(plays[:2]) # prints elements from beginning to 1
print()

famous_plays = plays[:3]
famous_plays.append("A Midsummer's Night Dream")
famous_plays.append("The Tempest")
print(plays)
print(famous_plays)
comedies = ["A Midsummer's Night Dream", "The Merchant of venice", "Twelfth Night", "The Tempest"]
shakespeare_plays = comedies[:] # copies entire list
shakespeare_plays.append(plays[:]) # list is generic so will add entire second list as one element, so don't do this
print(shakespeare_plays)
shakespeare_plays.pop()
# what we want
for play in plays:
    shakespeare_plays.append(play)
print(shakespeare_plays)
print(comedies)
