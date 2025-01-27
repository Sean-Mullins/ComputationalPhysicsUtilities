import matplotlib.pyplot as plt
import numpy as np
import interatomic_distances_V5

mu, sigma = 0, 0.5 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

bins = 30

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
          linewidth=2, color='r')

plt.hist(interatomic_distances_V5.data_flt, 100)

plt.show()