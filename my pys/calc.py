#calcul
#======
def add(a,b):
	return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

a=float(raw_input('first num:'))
b=float(raw_input('first num:'))
op=raw_input('op to perform, +,/,-,*:')

if op=='+':
    print add(a,b)

if op=='-':
    print sub(a,b)

if op=='/':
    print div(a,b)

if op=='*':
    print mul(a,b)
