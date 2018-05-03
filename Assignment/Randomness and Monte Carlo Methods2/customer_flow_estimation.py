import numpy as np
import matplotlib.pyplot as plt

def getNnP(mean, std):
    variance = (std**2)
    p = 1 - (variance / mean) 
    n = mean / p
    return [n, p]



# u = 10 and std = 2.3 from 11 ~ 12
# u = 15 and std = 2.8 from 12 ~ 1 
# u = 5 and std = 1.6 from 1 ~ 5
# u = 15 and std = 2.8 from 5 ~ 8 
# u = 10 and std = 2.3 from 8 ~ 9 
mean = [10, 10, 15, 15, 5, 5, 5, 5, 5, 5, 5, 5, 15, 15, 15, 15, 15, 15, 10, 10]
std = [2.3, 2.3, 2.8, 2.8, 1.6, 1.6, 1.6, 1.6, \
        1.6, 1.6, 1.6, 1.6, 2.8, 2.8, 2.8, 2.8, \
        2.8, 2.8, 2.3, 2.3]

n = np.zeros(20, dtype='d')
p = np.zeros(20, dtype='d')

# find ns and ps from mean and std. 
for i in np.arange(20): 
    m = mean[i]
    s = std[i]
    temp = getNnP(m, s)
    n[i] = temp[0]
    p[i] = temp[1]

core_customer_means = np.zeros(20, dtype='d')
casual_customer_means = np.zeros(20, dtype='d')
casual_customer_means1 = np.zeros(20, dtype='d') # sensitivity analysis
casual_customer_means2 = np.zeros(20, dtype='d') # change general mall traffic
n_for_casual = np.array([100, 100, 150, 150, 50, 50, 50, 50, 50, \
                        50, 50, 50, 150, 150, 150, 150, 150, \
                        150, 100, 100], dtype='d')
n_for_casual2= n_for_casual * 1.1 # increase general mall traffic 10% 


total_customer_means = np.zeros(20, dtype='d')
total_customer_means2 = np.zeros(20, dtype='d')


for i in np.arange(20): 
    # mean number of core customers in each time zone
    s_core = np.random.binomial(n[i], p[i], 1000)
    core_customer_means[i] = s_core.mean()
    
    # mean number of casual customers in each time zone 
    if i == 0: 
        s_casual = np.random.binomial(n_for_casual[i] - 1, 0.01, 1000)
        casual_customer_means[i] = s_casual.mean()
        casual_customer_means1[i] = s_casual.mean()
        s_casual2 = np.random.binomial(n_for_casual2[i] - 1, 0.01, 1000)
        casual_customer_means2[i] = s_casual2.mean()
    else: 
        total_customers = core_customer_means[i - 1] \
                        + casual_customer_means[i - 1]
        
        s_casual = np.random.binomial(n_for_casual[i], \
                                    0.002 * (total_customers - 1) + 0.01, 1000)
        casual_customer_means[i] = s_casual.mean()
        
        s_casual1 = np.random.binomial(n_for_casual[i], \
                                    0.0025 * (total_customers - 1) + 0.01, 1000)
        casual_customer_means1[i] = s_casual1.mean()
        
        s_casual2 = np.random.binomial(n_for_casual2[i], \
                                    0.002 * (total_customers - 1) + 0.01, 1000)
        casual_customer_means2[i] = s_casual2.mean()
        
    total_customer_means[i] = core_customer_means[i] \
                                + casual_customer_means[i]
    total_customer_means2[i] = core_customer_means[i] \
                                + casual_customer_means2[i]

    
colLabels = ['Mean Number of Core Customers', \
            'Mean Number of Casual Customers', 'Mean Number of Total Customers']
rowLabels = []

data = np.zeros(shape=(21, 3))
for i in np.arange(20):
    rowLabels.append(i + 1)
    data[i, 0] = core_customer_means[i]
    data[i, 1] = casual_customer_means[i]
    data[i, 2] = total_customer_means[i]

rowLabels.append('Total')
data[-1, 0] = core_customer_means.sum()
data[-1, 1] = casual_customer_means.sum()
data[-1, 2] = total_customer_means.sum()

fig, ax = plt.subplots()

fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.table(cellText=data, rowLabels=rowLabels, colLabels=colLabels, loc='center')
fig.tight_layout()

# couldn't figure out adding merged cell for Std
print('Standard Deviation: ', total_customer_means.std())
plt.show()
plt.savefig('table.png')

plt.figure(2)
x = np.arange(20) + 1
plt.plot(x, casual_customer_means1,'b--', x, casual_customer_means, 'r--')
plt.title('Sensitive Analysis')
plt.xlabel('Time frame')
plt.ylabel('Casual Customer means')
plt.show()
plt.savefig('SensitivityAnalysis.png')

plt.figure(3)
plt.plot(x, total_customer_means2,'b--', x, total_customer_means, 'r--')
plt.title('Increased mall traffic by 10%')
plt.xlabel('Time frame')
plt.ylabel('Total customer means')
plt.show()
plt.savefig('TotalCustomer.png')