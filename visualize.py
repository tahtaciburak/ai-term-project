import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = []
scores = []
times = []
with open("game.log","r") as f:
    lines = f.readlines()
    for line in lines:
        string = line.replace("\n"," ").split(" ")
        times.append(float(string[2]))
        scores.append(int(string[1]))
        t.append(int(string[0]))
# Data for plotting

fig, ax = plt.subplots()
plt.scatter(t,times)
plt.show()
