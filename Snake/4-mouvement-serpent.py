import pgzrun

# Déplacé pour devenir accessible partout (global)
snake_segments = [
        {'x': 3, 'y': 0},
        {'x': 2, 'y': 0},
        {'x': 1, 'y': 0},
        {'x': 0, 'y': 0},
    ]

timer = 0

def update(dt):
  global timer

  timer += dt
  if timer >= 0.15:
    timer = 0
    # Temporaire
    print('tic')

    next_x_position = snake_segments[0]['x'] + 1
    next_y_position = snake_segments[0]['y']

    snake_segments.insert(0, {'x': next_x_position, 'y': next_y_position})
    snake_segments.pop()

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