# Global variables
state = {}
# functions 
def init_game():
  state['board'] = {
    'a1' : ' ', 'b1' : ' ', 'c1' : ' ', 
    'a2' : ' ', 'b2' : ' ', 'c2' : ' ', 
    'a3' : ' ', 'b3' : ' ', 'c3' : ' ', 
  }
  state['turn'] = 'x'
  state['player_x'] = []
  state['player_o'] = []
  print_board()
  get_move()

def print_board(): 
  print(f"\n    A   B   C\n1)  {state['board']['a1']} | {state['board']['b1']} | {state['board']['c1']}\n   -----------\n2)  {state['board']['a2']} | {state['board']['b2']} | {state['board']['c2']}\n   -----------\n3)  {state['board']['a3']} | {state['board']['b3']} | {state['board']['c3']}")

def get_move(): 
  print(f"\nPlayer {state['turn'].capitalize()}'s turn")
  move = input("Input your move(ex. B2):").lower()
  if move in state['board'].keys() and move not in state['player_x'] and move not in state['player_o']: 
    state['board'][move] = state['turn'].capitalize()
    state[f"player_{state['turn']}"].append(move)
    print_board()
    get_winner()
  else: 
    print("that is not a valid move. Try again:")
    get_move()

def get_winner(): 
  win_combos = [['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'], ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'], ['a1', 'b2', 'c3'], ['c1', 'b2', 'a3']]
  for combo in win_combos: 
    if all(moves in state[f"player_{state['turn']}"] for moves in combo):
      return print(f"Player {state['turn'].capitalize()} wins!")
  if len(state['player_x']) + len(state['player_o']) == 9:
    return print("It's a tie!")
  if state['turn'] == 'x':
      state['turn'] = 'o'
  else: 
    state['turn'] = 'x'
  get_move() 
  
#run game 
print("----------------------\nLet's play Py-Pac-Poe!\n----------------------\n(Tic-Tac-Toe in Python)\n")
init_game()