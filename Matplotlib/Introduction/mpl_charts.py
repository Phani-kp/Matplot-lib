from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [60, 40, 30, 13]
labels = ['Sixty','Forty','Thirty', 'Thirteen']
explode = [0, 0, 1, 0]

plt.pie(slices, labels = labels, explode= explode, shadow = True, startangle = 90, autopct = '%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title("My awesome Pie Chart")
plt.tight_layout()
plt.show()