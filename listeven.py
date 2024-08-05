a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
print("Even elements are")
for i in range(0,n):
	if a[i]%2==0:
		print(a[i])


