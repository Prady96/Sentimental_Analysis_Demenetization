import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv('demo.csv')
data['positive'] = data['label'] == "POSITIVE"
df = data['positive'].value_counts()
print(df[0])
print(df[1])

slices = [df[0], df[1]]
activites = ['negative', 'positive']
colors = ['r', 'g']
plt.pie(slices, labels=activites, colors=colors)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Demonitization Results 04')
plt.legend()
plt.show()
