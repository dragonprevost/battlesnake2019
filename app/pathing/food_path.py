from astar import aStar
from filters import SnakePartFilter

# Do food tree here
def food_path(food_list,board):
    snake_heads = [info.get_head() for info in board.get_enemies()]
    snake_heads.append(board.get_our_snake().get_head())
    for food in food_list:
        food_to_head = aStar(food,snake_heads,board,SnakePartFilter(snake_heads))
        if not food_to_head: continue
        if food_to_head[-1] == board.get_our_snake().get_head():
            return food_to_head
    return None

def find_food(board,food_list):
    snake_heads = [info.get_head() for info in board.get_enemies()]
    snake_heads.append(board.get_our_snake().get_head())
    for food in food_list:
        food_to_head = aStar(food,snake_heads,board,SnakePartFilter(snake_heads))
        if not food_to_head: continue
        if food_to_head[-1] == board.get_our_snake().get_head():
            return food_to_head
    return None


