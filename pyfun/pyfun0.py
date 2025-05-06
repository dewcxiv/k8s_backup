import matplotlib.pyplot as plt

moods = ['Excited', 'Bored', 'Sleepy', 'Curious']
values = [30, 20, 10, 40]

plt.pie(values, labels=moods, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title("Today's Mood at the Office")
plt.show()