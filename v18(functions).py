'''
def fun(*args):
    tpl = ()
    for v in args:
        tpl+= (v,)
    print(tpl) 
        
ar = [10,20,30,40,50,60,70]
fun(*ar)
'''

# unpacking arguments
def print_it(a,b,c,d,e):
    print(a,b,c,d,e)


lst = [10,20,30,40,50]
tpl = ('a','b','c','d','e')
s = {1,2,3,45,5}
print_it(*lst)
print_it(*tpl)
print_it(*s)

