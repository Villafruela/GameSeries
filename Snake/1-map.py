import pgzrun

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

  

pgzrun.go()