# We can get the output upto 999th catalan number using below program at https://www.jdoodle.com/python-programming-online/
# We can't get the output from 1000th catalan number as it reaches the limit
# Python version - 2.7.16
# Takes input from 'Stdin Inputs'

# Let nth catalan number be C(n)
# Below function returns C(n) and calculates number of recursive function calls made
def nthCatalan(n):
	global count;           # variable for counting number of function calls
	count = count + 1;
	if (n == 0 or n == 1):
		return 1;           # As C(0) = 1 and C(1) = 1
	else:
		return ((4 * n - 2) * nthCatalan(n - 1)) / (n + 1);   # C(n) = ((4n - 2) * C(n - 1))/(n + 1)    for all n >= 1

n = int(input());
count = 0;                     # Number of function calls were intitially set to 0
nthCat = nthCatalan(n);        # nthCatalan(n) returns float value
ans = int(nthCat);             # By type casting float to int, we get the final answer

if n == 1:
	print "1st Catalan number is",ans;
elif n == 2:
	print "2nd Catalan number is",ans;
elif n == 3:
	print "3rd Catalan number is",ans;
else:
 	print "{}th Catalan number is {}".format(n,ans);

print "Number of function calls are", count;

# Time & Space complexity of above program is O(n)