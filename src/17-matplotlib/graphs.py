import matplotlib.pyplot as plt

"""
# Stack Plot
year = [2011,2012,2013,2014,2015]

player1 = [8,10,12,7,9]
player2 = [7,12,5,15,21]
player3 = [18,20,22,25,19]


plt.plot([],[],color="y",label="player1")
plt.plot([],[],color="r",label="player2")
plt.plot([],[],color="b",label="player3")

plt.stackplot(year,player1,player2,player3, colors=["y","r","b"])
plt.title("Goals scored by year")
plt.xlabel("year")
plt.ylabel("Goal count")
plt.legend()
plt.show()

"""


"""
Pie Chart

goal_types = 'Penalty','Shot on target','Free kick'

goals = [12,35,7]
colors = ['y','r','b']

plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05), autopct="%1.1f%%")
plt.show()


"""
"""
Bar Chart

# Learning note: two slightly offset x positions per bar group is how you get bars side by side instead of stacked.
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

plt.legend()
plt.xlabel("Day")
plt.ylabel("Distance (km)")
plt.title("Vehicle info")
"""

"""
Histogram
ages = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
age_groups = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,age_groups,histtype="bar",rwidth=0.8)
plt.xlabel("age groups")
plt.ylabel("Number of people")
plt.title("Histogram")
"""

plt.show()
