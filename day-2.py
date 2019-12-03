# Part 1

class IntcodeComputer:
  def run_list(self, list):
    # For part 2
    self.program = list
    self.position = 0
    self.running = True
    while (self.running):
      self.execute()
    return self.program[0]
    
  def run_string(self, program_string):
    # For testing
    self.program = [int(num) for num in program_string.split(',')]
    self.position = 0
    self.running = True
    while (self.running):
      self.execute()
    return self.program[0]

  def run_file(self, program):
    self.load_program(program)
    self.position = 0
    self.running = True
    while (self.running):
      self.execute()
    return self.program[0]
    
  def load_program(self, file):
    input = open(file, 'r')
    program_string = input.readlines()[0]
    input.close()
    self.program = [int(num) for num in program_string.split(',')]

  def execute(self):
    current_op = self.program[self.position]
    if current_op == 1:
      self.add()
    elif current_op == 2:
      self.multiply()
    elif current_op == 99:
      self.terminate()
    
    self.position += 4
  
  def get_indices(self):
    idx = self.position
    a_idx = self.program[idx + 1]
    b_idx = self.program[idx + 2]
    c_idx = self.program[idx + 3]
    return (a_idx, b_idx, c_idx)

  def add(self):
    (a_idx, b_idx, target_idx) = self.get_indices()
    sum = self.program[a_idx] + self.program[b_idx]
    self.program[target_idx] = sum

  def multiply(self):
    (a_idx, b_idx, target_idx) = self.get_indices()
    product = self.program[a_idx] * self.program[b_idx]
    self.program[target_idx] = product
  
  def terminate(self):
    self.running = False

computer = IntcodeComputer()
print(computer.run_file('day-2-input.txt'))

# Part 2

input = open('day-2-input.txt', 'r')
program_string = input.readlines()[0]

for noun in range(100):
  for verb in range(100):
    program_list = [int (num) for num in program_string.split(',')]
    program_list[1] = noun
    program_list[2] = verb
    output = computer.run_list(program_list)
    if output == 19690720:
      print('noun:', noun, 'verb:', verb)
      break
