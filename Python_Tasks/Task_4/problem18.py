if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for _ in range(N):
        command = input().split()
        cmd_type = command[0]
        args = command[1:]
        
        if cmd_type == 'insert':
            lst.insert(int(args[0]), int(args[1]))
        elif cmd_type == 'print':
            print(lst)
        elif cmd_type == 'remove':
            lst.remove(int(args[0]))
        elif cmd_type == 'append':
            lst.append(int(args[0]))
        elif cmd_type == 'sort':
            lst.sort()
        elif cmd_type == 'pop':
            lst.pop()
        elif cmd_type == 'reverse':
            lst.reverse()
