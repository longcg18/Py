from collections import deque

if (__name__ == '__main__'):
    deq = deque()
    N = int(input())
    
    for i in range (N):
        row = input()
        cmds = row.split(' ')

        if (cmds[0] == "print"):
            print(deq, sep=' ')
        elif (cmds[0] == "pop"): 
            deq.pop()
        elif (cmds[0] == "popleft"):
            deq.popleft()
        elif (cmds[0] == "append"):
            val = int(cmds[1])
            deq.append(val)
        elif (cmds[0] == "appendleft"):
            val = int(cmds[1])
            deq.appendleft(val)
        else: 
            print("Unknown Cmd")
    for i in range(len(deq)):
        print(deq[i], end=" ")
