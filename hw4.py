import sympy
n = 2649376219191757686333291073027588009793925231566294290337286424331787812414080960960191670815548639

#Q6
print('n = ' + ' is prime: ' + str(sympy.isprime(n)))

q = n//2

#Q7 and Q8
if sympy.isprime(q) and sympy.isprime(n):
  print('n is a safe prime')
  print('Sophie Germain prime' + 'is ' + str(q))
else:
  print('n is not a safe prime')

def get_period(n):
  L=1
  while(True):
    if (10**L-1)%n==0:
      break
    L+=1
  return L

#Q9,Q10,Q11
flag_2 = False
flag_5 = False
flag_full = False
for i in range(pow(10,20)+1, pow(10,20)+1000):
  if flag_2 and flag_5 and flag_full:
    break
  if get_period(i) == 2 and not flag_2:
    print("period 2: ", i)
    flag_2 = True
  if get_period(i) == 5 and not flag_5:
    print("period 5: ", i)
    flag_5 = True
  if get_period(i) == i-1 and not flag_full:
    print("full period: ",i)
    flag_full = True
