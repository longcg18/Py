N = int(input())

alist = []
for i in range (N):
    cmds = input()
    splits_cmds = cmds.split(' ')
    cmd = splits_cmds[0]
    
    if (cmd == "print"):
        print(alist)
    elif (cmd == "sort"):
        alist = sorted(alist)
    elif (cmd == "insert"):
        pos = int(splits_cmds[1])
        val = int(splits_cmds[2])
        if (pos >= len(alist)):
            alist.append(val)
        else: 
            alist.insert(pos, val)
        #print("pos = ", pos, " val = ", val)
    elif (cmd == "append"):
        val = int(splits_cmds[1])
        alist.append(val)
    elif (cmd == "pop"):
        alist.pop()
    elif (cmd == "reverse"):
        alist.reverse()
    elif (cmd == "remove"):
        val = int(splits_cmds[1])
        alist.remove(val)
    else: 
        print("Unknown cmd")
    #print(cmds)
    
        
#print(cmds)