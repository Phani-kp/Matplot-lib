import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data1.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color = '#444444', linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label = 'Python')

# overall_median = 57287

plt.fill_between(ages, py_salaries)
plt.legend()

plt.title('Median Salary (USD) By Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()