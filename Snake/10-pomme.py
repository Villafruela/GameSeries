import pgzrun
import random

# Déplacé pour devenir accessible partout (global)
snake_segments = [
        {'x': 3, 'y': 0},
        {'x': 2, 'y': 0},
        {'x': 1, 'y': 0},
        {'x': 0, 'y': 0},
    ]

timer = 0

# Temporaire
direction_queue = ['right']

# Taille de la map
grid_x_count = 20
grid_y_count = 15

# On défini la taille de la fenêtre
WIDTH  = grid_x_count*16-grid_x_count
HEIGHT = grid_y_count*16-grid_y_count

def update(dt):
  global timer

  timer += dt
  if timer >= 0.15:
    timer = 0
    
    # Temporaire
    if len(direction_queue) > 1:
      direction_queue.pop(0)

    next_x_position = snake_segments[0]['x']
    next_y_position = snake_segments[0]['y']

    if direction_queue[0] == 'right':
      next_x_position += 1
      if next_x_position >= grid_x_count:
        next_x_position = 0

    elif direction_queue[0] == 'left':
      next_x_position -= 1
      if next_x_position < 0:
        next_x_position = grid_x_count - 1

    elif direction_queue[0] == 'down':
      next_y_position += 1
      if next_y_position >= grid_y_count:
        next_y_position = 0

    elif direction_queue[0] == 'up':
      next_y_position -= 1
      if next_y_position < 0:
        next_y_position = grid_y_count - 1

    snake_segments.insert(0, {'x': next_x_position, 'y': next_y_position})
    snake_segments.pop()


def on_key_down(key):
  if (key == keys.RIGHT
  and direction_queue[-1] != 'right'
  and direction_queue[-1] != 'left'):
    direction_queue.append('right')

  elif (key == keys.LEFT
  and direction_queue[-1] != 'left'
  and direction_queue[-1] != 'right'):
    direction_queue.append('left')

  elif (key == keys.DOWN
  and direction_queue[-1] != 'down'
  and direction_queue[-1] != 'up'):
    direction_queue.append('down')

  elif (key == keys.UP
  and direction_queue[-1] != 'up'
  and direction_queue[-1] != 'down'):
    direction_queue.append('up')

food_position = {
    'x': random.randint(0, grid_x_count - 1),
    'y': random.randint(0, grid_y_count - 1),
}

def draw():
  screen.fill((0, 0, 0))
  #grid_x_count = 20
  #grid_y_count = 15
  cell_size = 15

  screen.draw.filled_rect(
    Rect(
      0, 0,
      grid_x_count * cell_size, grid_y_count * cell_size
      ),
    color=(70, 70, 70)
    )

  for segment in snake_segments:
    screen.draw.filled_rect(
      Rect(
        segment['x'] * cell_size, segment['y'] * cell_size,
        cell_size - 1, cell_size - 1
        ),
      color=(165, 255, 81)
    )
  
  for direction_index, direction in enumerate(direction_queue):
        screen.draw.text(
            'direction_queue[' + str(direction_index) + ']: ' + direction,
            (15, 15 + 15 * direction_index)
        )
        
  screen.draw.filled_rect(
        Rect(
            food_position['x'] * cell_size, food_position['y'] * cell_size,
            cell_size - 1, cell_size - 1
        ),
        color=(255, 76, 76)
    )
  
pgzrun.go()