import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

label_format = '{:,.0f}'

# Reading and adding the row
miasta = pd.read_csv('../data/miasta.csv')
miasta.loc[len(miasta)] = [2010, 460, 555, 405]

# Making a Gdansk plot
ax = miasta["Gdansk"].plot(title='Gdańsk', marker='o', color='r')
ax.set_xlabel("Lata", fontsize=12)
ax.set_ylabel("L. ludnosci (tys.)", fontsize=12)
ax.xaxis.set_major_locator(ticker.FixedLocator(list(range(0, len(miasta["Rok"])))))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(miasta["Rok"]))
ax.set_xticklabels(miasta["Rok"], rotation=45)
plt.show()

# Making full data plot
tempCities = miasta
years = tempCities.pop("Rok")
for i in range(len(tempCities)):
    plt.figure()
    ax = tempCities.plot(marker='o', title="Ludnosc w miastach Polski")
    ax.set_xlabel("Lata", fontsize=12)
    ax.set_ylabel("L. ludnosci (tys.)", fontsize=12)
    ax.xaxis.set_major_locator(ticker.FixedLocator(list(range(0, len(years)))))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(years))

plt.show()





