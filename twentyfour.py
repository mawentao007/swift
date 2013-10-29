def is_ok(dest,a,b):
	if a + b == dest:
		return '%d + %d' %(a,b)
	if a - b == dest:
		return '%d - %d' %(a,b)
	if b - a == dest:
		return '%d - %d' %(b,a)
	if a * b == dest:
		return '%d * %d' %(a,b)
	if float(a)/b == dest:
		return '%d / %d' %(a,b)
	if float(b)/a == dest:
		return '%d / %d' %(b,a)

def sub_dest(dest,o):
	yield "%d - (%%s)" %o,o - dest
	yield "%d + (%%s)" %o,dest - o
	yield "(%%s)-%d"   %o,o+dest
	yield "(%%s)*%d"   %o,float(dest)/o
	yield "(%%s)/%d"   %o,dest*o
	yield "%d/(%%s)"   %o,float(o)/dest

def get_result(dest,l):
	if len(l) == 2:
		yield is_ok(dest,l[0],l[1])
		return

	for i in range(len(l)):
		s1 = [l[x] for x in range(len(l)) if x != i]
		for s,sub in sub_dest(dest,l[i]):
			for r in get_result(sub,s1):
				if r:
					yield s % r
	
for result in get_result(24,[1,4,5,6]):
	print result
