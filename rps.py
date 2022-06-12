#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:02:54 2022

@author: asad
"""

from random import choice


def rock_paper_scissors():
    msg = """
Welcome to Rock Paper Scissors

Rules
===================
Rock beats Scissors
Paper beats Rock
Scissors beats Paper

Enter:  r for Rock
        p for papper
        s for scissors
"""

    moves_dict = {
            'r': "Rock",
            'p': "Paper",
            's': "Scissors"
            }
    
    moves = list(moves_dict.keys()) # Get list of moves from move dictionary
    
    print(msg)
    
    while True: # Start Game Loop
        user_move = input("Enter Move>>> ").lower()
        
        if user_move not in moves:
            error_msg = """\nMove not recognised.
    Enter:  r for Rock
            p for papper
            s for scissors"""
            
            print(error_msg)
            continue
        
        else:
            cpu_move = choice(moves) # CPU makes a random move
            
            if user_move == cpu_move:
                print("This round was a tie")
                print(f"Player ({moves_dict[user_move]}) : CPU ({moves_dict[cpu_move]})")
                print("Play Again!")
                continue # Restart loop
                
            elif cpu_move == 'r' and user_move == 's': # Rock beats Scissors
                print("CPU WINS!")
                print(f"Player ({moves_dict[user_move]}) : CPU ({moves_dict[cpu_move]})")
            
            elif cpu_move == 's' and user_move == 'r': # Rock beats Scissors
                print("USER WINS!")
                print(f"Player ({moves_dict[user_move]}) : CPU ({moves_dict[cpu_move]})")
                
            
            elif cpu_move == 'p' and user_move == 'r': # Paper beats Rock
                print("CPU WINS!")
                print(f"Player ({moves_dict[user_move]}) : CPU ({moves_dict[cpu_move]})")
            
            elif cpu_move == 'r' and user_move == 'p': # Paper beats Rock
                print("USER WINS!")
                print(f"Player ({moves_dict[user_move]}) : CPU ({moves_dict[cpu_move]})")
                
            
            elif cpu_move == 's' and user_move == 'p': # Scissors beats Paper
                print("CPU WINS!")
                print(f"Player ({moves_dict[user_move]}) : CPU ({moves_dict[cpu_move]})")
            
            elif cpu_move == 'p' and user_move == 's': # Scissors beats Paper
                print("USER WINS!")
                print(f"Player ({moves_dict[user_move]}) : CPU ({moves_dict[cpu_move]})")
            
            break # End Game



if __name__ == "__main__":
    rock_paper_scissors()
