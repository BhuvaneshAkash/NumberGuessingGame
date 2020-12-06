import random
attempts_list = []
def show_score():
    if len(attempts_list) <=0:
        print("there is no high score ")
    else :
        print(" your score {} is attempts " . format(attempts_list))
def start_game():
    number = int(random.randrange(0,11))
    count =0
    player_name =  (input("Your Name:  "))
    want_play = input(f" Hi {player_name} you want to play ? (Yes / No)"  )
    show_score()
    while want_play.lower() == "yes":
        guess = int(input("Guess the number: "))
        if guess == number:
            print("Yaa!.. U got it...")
            count += 1
            attempts_list.append(count)
            print(f"your total count {count}")
            print("If you want to play again?"  )
            count =0
            show_score()
            number = int(random.randrange(0,11))
            play_again = input("Did you want to play again: (Yes / NO): ")
            if (play_again.lower) == "no":
                print("Ok... Bye")
        elif guess > number :
            print("The is bigger")
            count += 1
        elif guess < number :
            print("The is smaller")
            count+=1
    else:
        print("That's cool..Bye!")
if __name__ == "__main__":
    start_game()
