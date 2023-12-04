import random

num_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input()
        friends[name] = 0

    total_amount = float(input("Enter the total amount:\n"))

    if total_amount <= 0:
        print("No one is joining for the party")
    else:
        share_per_friend = round(total_amount / num_friends, 2)

        for friend in friends:
            friends[friend] = share_per_friend

        choice = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")
        if choice.lower() == "yes":
            lucky_one = random.choice(list(friends.keys()))
            print(f"{lucky_one} is the lucky one!")

            for friend in friends:
                if friend != lucky_one:
                    friends[friend] = round(total_amount / (num_friends - 1), 2)
            friends[lucky_one] = 0

        else:
            print("No one is going to be lucky")

        print(friends)
