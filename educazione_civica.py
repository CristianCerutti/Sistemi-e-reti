import matplotlib.pyplot as plt
import csv

mesi_n = []
temperatura = []
giacca = []
scuola = []
videogame = []
data_file = open("./data.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader:
    mesi_n.append(int(row[0]))
    temperatura.append(int(row[1]))
    giacca.append(int(row[2]))
    scuola.append(int(row[3]))
    videogame.append(int(row[4]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Relazione Educazione Civica')

ax1.plot(mesi_n, temperatura, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('temperatura media in c°')

ax2.plot(mesi_n, giacca, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Media uso giacca')

ax3.plot(mesi_n, scuola, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni scuola')

ax4.plot(mesi_n, videogame, 'o-y')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Media tempo gioco')

plt.show()