# Part 1

def calculate_fuel_requirement(mass):
  return (mass // 3) - 2

def get_module_masses(file):
  input = open(file, 'r')
  string_masses = input.readlines()
  input.close()
  return [ int(mass) for mass in string_masses ]

masses = get_module_masses('day-1-input.txt')
fuel_requirements = [ calculate_fuel_requirement(mass) for mass in masses ]
print('Initial fuel requirement:', sum(fuel_requirements))

# Part 2

def calculate_total_fuel_requirement(mass):
  initial_requirement = calculate_fuel_requirement(mass)
  return recursive_fuel_requirement(initial_requirement)

def recursive_fuel_requirement(initial_fuel_mass):
  additional_fuel = calculate_fuel_requirement(initial_fuel_mass)
  if (additional_fuel < 1):
    return initial_fuel_mass
  else:
    return initial_fuel_mass + recursive_fuel_requirement(additional_fuel)

new_fuel_requirements = [ calculate_total_fuel_requirement(mass) for mass in masses ]
total_fuel_requirement = sum(new_fuel_requirements)
print('Total fuel requirement:', total_fuel_requirement)

