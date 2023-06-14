import random
friends_value = int(input("Enter the number of friends joining (including you):\n"))
friends = dict()
if friends_value <= 0:
    print("No one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for i in range(friends_value):
        friend = input()
        friends[friend] = 0
    total = int(input("\nEnter the total bill value:\n"))
    answer = input("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    if answer == "Yes":
        name = random.choice(list(friends))
        print('\n', f'{name} is the lucky one!', sep="")
        total = round(total / (friends_value - 1), 2)
        for friend in friends:
            friends[friend] = total
            friends[name] = 0
    else:
        print("\nNo one is going to be lucky")
        total = round(total / friends_value, 2)
        for friend in friends:
            friends[friend] = total
    print("\n", friends, sep="")