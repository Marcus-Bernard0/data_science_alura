from random import randrange
import matplotlib.pyplot as plt

notas_matemática = []

for nota in range(8):
    notas_matemática.append(randrange(0, 11))

print(notas_matemática)

x = list(range(1, 9))
y = notas_matemática


plt.plot(x,y, marker = "o")
plt.title("Notas de matemática")
plt.xlabel("Provas")
plt.ylabel("Notas")

plt.show()
