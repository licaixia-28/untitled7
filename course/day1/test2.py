
def order_by(a):
	n = len(a)
	for i in range(n):
		for j in range(n-i-1):
			if a[j] >=a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]
	return a

a = [6,3,8,1,4,1,9,5]

b = order_by(a)
print(b)


