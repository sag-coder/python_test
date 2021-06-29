#global variable
b=4
a=5
def local(a):
    #local variable
    global b #transform globle
    b=3
    return (a)
print(b)
local(a)
print(a,b, sep=' ')

def pl():
    global egg
    egg=455
pl()
print(egg)