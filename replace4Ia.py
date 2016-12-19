'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
###

'''
'''
pd.read_csv('10-10-1.csv')
df.to_excel('foo.xlsx', sheet_name='Sheet1')


###
df = pd.read_csv('10-10-1dat.csv')
#print df
plt.plot(df)
plt.show()
#, sep=',' header '18', skiprows '17'
'''

import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('10-10-1.csv', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()