
from math import sqrt, pow

c1 = float(input("Digite o valor do cateto1 "))
c2 = float(input("Digite o valor do cateto2 "))


m_c1 = pow(c1, 2) #9
m_c2 = pow(c2, 2) #16

h = m_c1 + m_c2 #25 
sqrt_h = sqrt(h)

#outra forma seria com math.hypot


print(f"A hipotenusa vale {sqrt_h}") 