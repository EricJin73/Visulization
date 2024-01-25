import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="white")
plt.rcParams["font.size"] = 20
plt.rcParams["font.sans-serif"] = 'Times New Roman'
plt.rcParams["font.weight"] = 'bold'
#########################################################
data = pd.read_excel(r'time.xlsx', sheet_name='Sheet1')
model = pd.read_excel(r'time.xlsx', sheet_name='model')

textFS = 16
ticksFS = 12

f, ax = plt.subplots(figsize=(10,5))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

x = data['Year']
y = data['Number']

bar_width = 1
al = 0.8

plt.bar(x, height=y, width=bar_width, color='#7C78CB', label='Paper', 
        alpha=0.5)

sns.lineplot(x=model['Year'], y=model['Number'], hue=model['Type'],
             palette='viridis_r',
             lw=3,
             ls='solid',
             dashes=False,
             alpha=0.8
            )

legend1 = ax.legend(loc='upper left', title='', frameon=False)
legend1.get_frame().set_alpha(0.0)

plt.xticks( fontsize=ticksFS)
plt.xlabel('', fontsize=textFS)
plt.ylabel('Number of papers and models', fontsize=textFS)
plt.yticks(fontsize=ticksFS)

plt.ylim(0, 24)
plt.grid(axis="y")
plt.gcf().subplots_adjust(left=0.10, bottom=0.15)
plt.show()
