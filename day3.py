# Part 1

class Grid:
  def __init__(self):
    self.x_axis = {}
    self.intersections = []
    self.intersections_sum = []
    self.current_x = None
    self.current_y = None
    self.symbol = None
    self.steps = 0
  
  def get(self):
    x_coord = self.current_x
    y_coord = self.current_y
    y_axis = self.x_axis.get(x_coord, {})
    return y_axis.get(y_coord, None)

  def add_wire_unit(self):
    x_coord = self.current_x
    y_coord = self.current_y
    y_axis = self.x_axis.get(x_coord, None)
    if y_axis is None:
      self.x_axis[x_coord] = {}
      y_axis = self.x_axis.get(x_coord)
      y_axis[y_coord] = { 'wire': self.symbol, 'steps': self.steps }
    else:
      y_value = y_axis.get(y_coord, None)
      if y_value is None:
        y_axis[y_coord] = { 'wire': self.symbol, 'steps': self.steps }
      elif y_value['wire'] is not self.symbol and y_value['wire'] is not 'X':
        y_axis[y_coord] = { 'wire': self.symbol, 'steps': self.steps }
        self.intersections.append(abs(x_coord) + abs(y_coord))
        self.intersections_sum.append(self.steps + y_value['steps'])

  def add_wire_length(self, instruction):
    direction = instruction[0]
    steps = int(instruction[1:])
    functions = {
      'R': self.right,
      'L': self.left,
      'U': self.up,
      'D': self.down,
    }
    functions[direction](steps)



  def right(self, steps):
    for _ in range(steps):
      self.current_x += 1
      self.steps += 1
      self.add_wire_unit()

  def left(self, steps):
    for _ in range(steps):
      self.current_x -= 1
      self.steps += 1
      self.add_wire_unit()

  def up(self, steps):
    for _ in range(steps):
      self.current_y += 1
      self.steps += 1
      self.add_wire_unit()

  def down(self, steps):
    for _ in range(steps):
      self.current_y -= 1
      self.steps += 1
      self.add_wire_unit()
      
  def map_wire_path(self, path, symbol):
    self.symbol = symbol
    self.current_x = 0
    self.current_y = 0
    for instruction in path:
      self.add_wire_length(instruction)
    self.current_x = None
    self.current_y = None
    self.symbol = None
    self.steps = 0
  
  def minimum_manhattan_distance(self):
    return min(self.intersections)
  
  def minimum_intersection_sum(self):
    return min(self.intersections_sum)

def load_paths(filename):
  input = open(filename, 'r')
  wires = input.readlines()
  input.close()
  return [ wire.split(',') for wire in wires ]
    
grid = Grid()
paths = load_paths('day3-input.txt')
for idx, path in enumerate(paths):
  grid.map_wire_path(path, str(idx))

print(grid.minimum_manhattan_distance())
print(grid.minimum_intersection_sum())
