import matplotlib.pyplot as plt
## Line Plot
x=[1,2,3,4,5]
y=[1,4,9,16,25]
z=[1,8,27,64,125]

plt.subplot(2,2,1)

plt.plot(x,y, color='red', linestyle='solid', marker='o')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Square Number')

plt.subplot(2,2,2)
plt.plot(x,z, color='blue', linestyle='-.', marker='o')
plt.xlabel('X axis')
plt.ylabel('Z axis')
plt.title('Cube Number')

plt.subplot(2,2,3)
plt.plot(y,z, color='Green', linestyle='-.', marker='o')
plt.xlabel('Y axis')
plt.ylabel('Z axis')
plt.title('Square Cube Number')
plt.show()

##Bar Plot
categories=['A','B','C','D','E']
values = [5,6,7,8,9]

plt.bar(categories,values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Nothing summa')
plt.show()
