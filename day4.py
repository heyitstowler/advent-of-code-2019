# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# 156218-652527

def crack_code(minimum, maximum):
  valid = 0
  for i in range(1,10):
    for j in range(i, 10):
      for k in range(j, 10):
        for l in range(k, 10):
          for m in range(l, 10):
            for n in range(m, 10):
              number = i * 100000 + j * 10000 + k * 1000 + l * 100 + m * 10 + n
              if number < minimum:
                continue
              if number > maximum:
                break
              if i is j or j is k or k is l or l is m or m is n:
                valid += 1
              else:
                continue
  return valid

print(crack_code(156218, 652527))

# Part 2

def crack_code_v2(minimum, maximum):
  valid = 0
  for i in range(1,10):
    for j in range(i, 10):
      for k in range(j, 10):
        for l in range(k, 10):
          for m in range(l, 10):
            for n in range(m, 10):
              number = i * 100000 + j * 10000 + k * 1000 + l * 100 + m * 10 + n
              if number < minimum:
                continue
              if number > maximum:
                break
              if i is j and j is not k:
                valid += 1
                continue

              if i is not j and j is k and k is not l:
                valid += 1
                continue
              if j is not k and k is l and l is not m:
                valid += 1
                continue
              if k is not l and l is m and m is not n:
                valid += 1
                continue
              if l is not m and m is n:
                valid += 1
                continue
              else:
                continue
  return valid

print(crack_code_v2(156218, 652527))