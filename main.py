import pyspiel
import numpy as np
import mcts as MCTS
from gui import GUI
import pygame
import sys

def play_game(game, human_player):
    state = game.new_initial_state()
    gui = GUI()

    while not state.is_terminal():
        gui.update_board(state.observation_tensor(), state.legal_actions())
        current_player = state.current_player()
        
        if current_player == human_player:
            legal_actions = state.legal_actions()
            action = None
            while action not in legal_actions:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        clicked_pos = gui.get_clicked_position(event.pos)
                        if clicked_pos in legal_actions:
                            action = clicked_pos
        else:
            action = MCTS.select_action(state)

        state.apply_action(action)

    # Game over
    gui.update_board(state.observation_tensor())
    
    if state.returns()[human_player] > 0:
        winner = human_player
    elif state.returns()[human_player] < 0:
        winner = 1 - human_player
    else:
        winner = None
    
    gui.show_winner(winner)

def main():
    game = pyspiel.load_game("othello")
    human_player = 1  # 1 for black, 0 for white
    play_game(game, human_player)

if __name__ == "__main__":
    main()