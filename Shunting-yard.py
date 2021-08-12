y = open("test_output.txt", "w")

import queue

def shunt(file):
    for a in file:
        c = []
        q = queue.Queue()
        Y = a.split()
        z = {"+":5, "-":10, "*":15, "/": 20}
        for i in Y:
            if i not in ("+", "-", "*", "/", "(", ")"):
                q.put(i)
            elif i != ")" :
                if len(c) == 0 :
                    c.append(i)
                elif i == "(" or c[-1] == "(":
                    c.append(i)
                else:
                    for ie in reversed(c):
                        if ie == "(":
                            break
                        elif z[i] <= z[ie]:
                            q.put(ie)
                            c.pop()
                    c.append(i)

            elif i == ")":
                for a  in reversed(c):
                    if a == "(":
                        c.pop()
                        break  
                    else:    
                        q.put(a)
                        c.pop()  
        while c:
            q.put(c.pop())


            
        f = open("test_output.txt", "a")
        x = list(q.queue)
        for element in x:
            f.write(element + " ")
        f.write('\n')
    f.close()
        
def rpn_calcu (expr):
    s = []
    ops = { "+": lambda x,y: x+y, "-": lambda x,y: y-x, "/": lambda x,y: y/x, "*": lambda x,y: x*y}

    instructions = expr.split()
    
    for i in instructions:
        if i in ops:
            s.append(ops[i](s.pop(), s.pop()))
        else:
            value = float(i)
            s.append(value)
    return s.pop()




