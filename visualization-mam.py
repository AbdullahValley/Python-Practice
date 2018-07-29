import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
f = open('gapminder.csv', 'r')
data = f.read()
print(data)


year=[1950,1970,1990,2010]
pop=[2.519,3.629, 5.263, 6.972]
plt.plot(year,pop)
plt.show()

plt.scatter(year,pop)
plt.show()


population = pd.read_csv('gapminder.csv', index_col=0)
#life_exp=population.loc[:,'life_exp']
#gdp_cap=population.loc[:,'gdp_cap']
life_exp = population['life_exp']
gdp_cap = population['gdp_cap']
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
plt.show()

pop=population.loc[:,'population']
plt.scatter(pop,life_exp)
plt.show()



plt.hist(life_exp)
# Display histogram
#plt.show()


# Build histogram with 5 bins
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins

plt.hist(life_exp,bins=20)
# Show and clean up again
plt.show()
plt.clf()


# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
# Add title
plt.title(title)
# After customizing, display the plot
plt.show()



# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000,10000,100000]
tick_lab = ['1k','10k','100k']
# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)
# After customizing, display the plot
plt.show()

