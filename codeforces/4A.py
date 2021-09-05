def can_divide(w):
	return w % 2 == 0 and w != 2

w = int(input())
print('YES' if can_divide(w) else 'NO')
