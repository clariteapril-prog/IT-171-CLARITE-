player_x = 0
player_y = 0
treasure_x = 5
treasure_y = 3
game_running = True
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
while game_running:
    move = input("Enter move (up/down/left/right): ")


    if move == 'w':
        player_x += 1
    elif move == 's':
        player_x -= 1
    elif move == 'a':
        player_y += 1
    elif move == 'd':
        player_y -= 1
        
    print(f"Player position: ({player_x}, {player_y})")
    if player_x == treasure_x and player_y == treasure_y:
        print("You've reached your destination")
        break
    
    if move == "quit":
        print("You have exit the game")
        break
