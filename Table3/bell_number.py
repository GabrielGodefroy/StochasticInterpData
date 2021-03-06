# The Bell numbers count the possible partitions of a set.
#
# This Python script compute and display the Bell number (Bn) up to n = 50
#
# The Bell numbers are computed using the Bell triangle method
# described here: https://en.wikipedia.org/wiki/Bell_triangle
#
# Note: In Python, integers have arbitrary precision. This makes it possible to represent an arbitrarily large range of integers (only limited by memory available).



def display_bell_numbers(bell_numbers):
	for index, bellnumbers in enumerate(bell_numbers):
		print(index, bellnumbers)


def compute_bell_numbers(up_to):
	bell_triangle = compute_bell_triangle(up_to)
	return [elem[0] for elem in bell_triangle]


def compute_bell_triangle(up_to):
	bell_triangle = [[1]];
	for i in range(1, up_to):
		bell_triangle.append([None for a in range(i+1)])
		for j in range(0,i+1):
			if(j==0):
				bell_triangle[i][j] = bell_triangle[i-1][i-1] 	
			else:
				bell_triangle[i][j] = bell_triangle[i-1][j-1] +\
										bell_triangle[i][j-1]
	return bell_triangle


def main():
	UP_TO = 50;
	bell_numbers = compute_bell_numbers(up_to=UP_TO);
	display_bell_numbers(bell_numbers)


main()
