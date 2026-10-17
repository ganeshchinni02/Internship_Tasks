#Lists
#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    output_list = []
    
    for _ in range(N):
        command = input().split()
        cmd_type = command[0]
        
        if cmd_type == "insert":
            output_list.insert(int(command[1]), int(command[2]))
        elif cmd_type == "print":
            print(output_list)
        elif cmd_type == "remove":
            output_list.remove(int(command[1]))
        elif cmd_type == "append":
            output_list.append(int(command[1]))
        elif cmd_type == "sort":
            output_list.sort()
        elif cmd_type == "pop":
            output_list.pop()
        elif cmd_type == "reverse":
            output_list.reverse()
