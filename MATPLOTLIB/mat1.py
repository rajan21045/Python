import matplotlib.pyplot as plt


# # # sample data
# # # x= [1,2,3,4,5]
# # # y= [3,4,5,6,7]
# # # z = [7,15,4,21,13]

# # # # plot with different markers
# # # plt.plot(x,y, marker= 'o', linestyle= '-', color = 'b', label= 'Circle Marker')
# # # plt.plot(x,[i-1 for i in y], marker= '^', linestyle= '--', color = 'r', label= 'Triangle Marker')
# # # plt.plot(x, z, color=(0.1, 0.2, 0.5), marker='^', linestyle='solid', label='RGB Line')

# # # # add title and label
# # # plt.title("Plot With Different Markers")
# # # plt.xlabel('X-Axis')
# # # plt.ylabel('Y-Axis')

# # # # show legend()
# # # plt.legend()
# # # plt.grid(True, axis='x', linestyle='--', linewidth=0.5, color='gray')
# # # plt.grid(True, axis='y', linestyle='-', linewidth=0.7, color='red')

# # # # display the plot
# # # plt.show()

# # # x = [1,2,3,4,5]
# # # y = [2,3,5,7,11]
# # # z=[1,4,6,8,10]
# # # # creaate figure
# # # plt.figure(figsize=(10,5))
# # # # First subplot
# # # plt.subplot(1,2,1)
# # # plt.plot(x,y,marker='o', linestyle='-', color='blue')
# # # plt.title("Subplot-1")
# # # plt.xlabel("X-Axis")
# # # plt.ylabel('Y-Axis')

# # # # Second subplot
# # # plt.subplot(1,2,2)
# # # plt.plot(x,z,marker='^', linestyle='--', color='red')
# # # plt.title('Subplot 2')
# # # plt.xlabel("X-Axis")
# # # plt.ylabel("Y-Axis")

# # # plt.tight_layout()
# # # plt.show()

# # x = [1,2,3,4,5]
# # y1= [2,3,5,7,11]
# # y2 = [1,4,6,8,10]
# # y3 = [2,4,6,8,10]
# # y4 = [1,3,5,7,9]

# # fig,axis = plt.subplots(2,2,figsize=(10,8))
# # # first subplot
# # axis[0,0].plot(x,y1, marker='o', linestyle='-', color='blue')
# # axis[0,0].set_title("Population Census")
# # axis[0,0].set_xlabel('Time')
# # axis[0,0].set_ylabel('Population')

# # # second plot
# # axis[0,1].plot(x,y2, marker='^', linestyle='-', color='red')
# # axis[0,1].set_title("Sale Census")
# # axis[0,1].set_xlabel('Time')
# # axis[0,1].set_ylabel('Sales')

# # # third plot
# # axis[1,0].plot(x,y3, marker='s', linestyle='-', color='green')
# # axis[1,0].set_title("Temperature Census")
# # axis[1,0].set_xlabel('Month')
# # axis[1,0].set_ylabel('Degrees')

# # # fourth plot
# # axis[1,1].plot(x,y4, marker='d', linestyle='-', color='purple')
# # axis[1,1].set_title("Profit Census")
# # axis[1,1].set_xlabel('Time')
# # axis[1,1].set_ylabel('Profit')

# # plt.tight_layout()
# # plt.show()


# # vertical bar graph
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [3,7,2,5,4]
# plt.bar(categories, values, color='skyblue', edgecolor='black', linewidth=1.2)
# plt.title('Customized Bar Graph')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.grid(True, axis='y', linestyle='--', linewidth=0.7)
# plt.show()

# # Horizontal Bar Graph
# categories = ['BCA', 'BIM', 'CSIT', 'Diploma', 'BHM']
# values = [31,27,48,59,22]

# plt.barh(categories, values, color='orange', edgecolor='black', linewidth=1.2)

# plt.title('Horizontal Bar Graph')
# plt.xlabel('Values')
# plt.ylabel('Categories')

# plt.grid(True, axis='x', linestyle='--', linewidth=0.7)
# plt.show()

# semesters=['2nd', '4th', '6th', '8th']
# boys = [21,17,19,11]
# girls = [11,18,14,19]

# x=range(len(semesters))
# plt.bar(x,boys,width=0.4, label='Boys', color='skyblue', align='center')
# plt.bar(x, girls, width=0.4, label='Girls', color='pink',align='edge')

# plt.title("Number of Boys VS Girls")
# plt.xlabel("Semesters")
# plt.ylabel("Number of Students")

# plt.xticks(x,semesters)
# plt.legend()
# plt.show()

# pie chart

labels = ['BCA', 'BIM', 'CSIT', 'Diploma', 'BHM']
sizes = [31, 27,48,59, 22]
colors = ['gold', 'lightcoral', 'skyblue', 'orange', 'green']
explode=(0.1,0,0,0,0)

plt.pie(sizes, explode=explode, labels=labels,colors=colors, autopct='%1.1f%%', shadow=True)
plt.title('Ditribution of Students Across Faculty')
plt.show()