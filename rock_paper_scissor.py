import random
loop = True

while loop:
    try:
        x_times = int(input("how many rounds do you wanna play? "))
        while x_times <= 0:
            x_times = int(input("how many rounds do you wanna play? "))
        loop = False
    except ValueError:
        print("give me a correct value man!!!")

options = ["rock", "paper", "scissor"]
user_score = ai_score = draw = 0
name = input("what is your name? ")
print("\nrock = 1\npaper = 2\nscissor = 3\n")
for x in range(x_times):
    print(f"round {x+1}/{x_times}")
    while True:
        try:
            a = int(input("give your choice:"))
            while a not in [1,2,3]:
                a = int(input("give your choice:"))
                print("\nIDIOT")
            break
        except ValueError:
            print("\nIDIOT")

    user_choice = ["rock","paper", "scissor"][a-1]

    ai_choice = random.choice(options)
    print(f"\n{name} chose: {user_choice}")
    print(f"AI chose: {ai_choice}")
    i = options.index(user_choice)

    if user_choice in options and ai_choice == ["paper", "scissor", "rock"][i]:
        print("AI wins\n")
        ai_score += 1
    elif user_choice == ai_choice:
        print("its a draw\n")
        draw += 1
    else:
        print(f"{name} wins\n")
        user_score += 1
    if x+1 == x_times:
        if ai_score > user_score:
            print(f"AI score:{ai_score}\n{name}:{user_score}\nDraw: {draw}\nUltimately AI wins")
        elif ai_score < user_score:
            print(f"AI score:{ai_score}\n{name}:{user_score}\nDraw: {draw}\nUltimately {name} wins")
        elif ai_score == user_score:
            print(f"AI score:{ai_score}\n{name}:{user_score}\nDraw: {draw}\nSo its a draw")