import pgzrun

# Déplacé pour devenir accessible partout (global)
snake_segments = [
        {'x': 3, 'y': 0},
        {'x': 2, 'y': 0},
        {'x': 1, 'y': 0},
        {'x': 0, 'y': 0},
    ]

timer = 0

direction = 'right'

def update(dt):
  global timer

  timer += dt
  if timer >= 0.15:
    timer = 0
    # Temporaire
    print('tic')

    next_x_position = snake_segments[0]['x']
    next_y_position = snake_segments[0]['y']

    if direction == 'right':
        next_x_position += 1
    elif direction == 'left':
        next_x_position -= 1
    elif direction == 'down':
        next_y_position += 1
    elif direction == 'up':
        next_y_position -= 1

    snake_segments.insert(0, {'x': next_x_position, 'y': next_y_position})
    snake_segments.pop()


def on_key_down(key):
  global direction

  if key == keys.RIGHT and direction != 'left':
      direction = 'right'
  elif key == keys.LEFT and direction != 'right':
      direction = 'left'
  elif key == keys.DOWN and direction != 'up':
      direction = 'down'
  elif key == keys.UP and direction != 'down':
      direction = 'up'

def draw():
  screen.fill((0, 0, 0))
  grid_x_count = 20
  grid_y_count = 15
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
  
pgzrun.go()