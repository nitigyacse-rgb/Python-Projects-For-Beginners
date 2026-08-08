import random

def display_rules():
    print("=" * 45)
    print("         WELCOME TO THE 21 NUMBER GAME")
    print("=" * 45)
    print("Rules:")
    print("1. Players take turns counting up from 1.")
    print("2. On your turn, you can call out 1, 2, or 3 consecutive numbers.")
    print("3. Players take turns alternating choices.")
    print("4. The player who is forced to say 21 loses the game!\n")

def get_user_choice(current_num):
    while True:
        try:
            choice = int(input("How many numbers do you want to add (1, 2, or 3)? "))
            if choice in [1, 2, 3] and current_num + choice <= 21:
                return choice
            elif current_num + choice > 21:
                print(f"Choice exceeds 21. Maximum allowed right now is {21 - current_num}.")
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def get_computer_choice(current_num):
    # Optimal winning strategy: landing on multiples of 4 (4, 8, 12, 16, 20)
    target = (current_num // 4 + 1) * 4
    if target == current_num:
        target += 4
    
    choice = target - current_num
    
    # Fallback to a valid choice if calculated move is out of range
    if choice not in [1, 2, 3] or current_num + choice > 21:
        choice = random.randint(1, min(3, 21 - current_num))
        
    return choice

def play_game():
    display_rules()
    
    order = input("Do you want to go 1st or 2nd? (Enter '1' or '2'): ").strip()
    user_turn = True if order == '1' else False
    
    numbers = []
    current_num = 0

    while current_num < 21:
        if user_turn:
            print(f"\n--- Your Turn (Current total: {current_num}) ---")
            count = get_user_choice(current_num)
            added = list(range(current_num + 1, current_num + count + 1))
            numbers.extend(added)
            current_num = numbers[-1]
            print(f"You called: {added}")
            print(f"Sequence so far: {numbers}")
            
            if current_num == 21:
                print("\nYou called 21! GAME OVER — Computer wins!")
                break
            user_turn = False
        else:
            print(f"\n--- Computer's Turn (Current total: {current_num}) ---")
            count = get_computer_choice(current_num)
            added = list(range(current_num + 1, current_num + count + 1))
            numbers.extend(added)
            current_num = numbers[-1]
            print(f"Computer called: {added}")
            print(f"Sequence so far: {numbers}")
            
            if current_num == 21:
                print("\nComputer called 21! CONGRATULATIONS — You win!")
                break
            user_turn = True

if __name__ == "__main__":
    play_game()