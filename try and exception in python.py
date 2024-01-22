with open('myfile.txt','w') as file:
    file.write(" $No. 10 !")
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise 

'''class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
    output:
        B
        C
        D
'''
'''try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)


    x, y = inst.args
    print('x = ', x)
    print('y = ', y)

<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x =  spam
y =  eggs
'''