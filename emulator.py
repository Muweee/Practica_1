import shlex
import os

vfs_name = "admin: "
cmd_exit = "exit"
while True:
    cmd_line = input(vfs_name)
    
    parts = shlex.split(cmd_line)

    command = parts[0]
    argument = parts[1:]

    if len(parts) == 0:
        continue
  
    if cmd_line.startswith('$'):
        name =cmd_line[1:]
        if name in os.environ:
            print(os.environ[name])
        else:
            print(f'{name}: argument not found')
    
    #parts = shlex.split(cmd_line)
    
    #if len(parts) == 0:
     #   continue
    
    #command = parts[0]
    #argument = parts[1:]
    
    elif command == cmd_exit:
        break;
    elif command == 'ls' or command == 'cd':
        print(parts)
    else:
        print(f'{command}: command not found')
