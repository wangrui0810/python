__author__ = 'WR'
def is_prime(x):
	flag = 1
	if x==2:
		flag = 1
	else:
		n = int(x**0.5)
		for i in range(2, n+1):
            if x%i == 0:
                flag = 0
                break

	return flag
print 6**0.5

for i in range(100):
    if is_prime(i) == 0:
        print ("%d is not prime" % i)
    else:
        print '%d is prime' % i




