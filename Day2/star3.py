forwardNo = 0
depth = 0
aim = 0
with open("input.txt", 'r') as inFile:
    for line in inFile:
        line = line.rstrip()
        if "forward" in line:
            forwardNo = forwardNo + int(line[-1])
        if "down" in line:
            depth = depth + int(line[-1])
        if "up" in line:
            depth = depth - int(line[-1])
        
    print(depth)
    print(forwardNo)
    print(depth * forwardNo)
    
    forwardNo = 0
    depth = 0
    aim = 0
    
    for line in inFile:
        line = line.rstrip()
        if "forward" in line:
            forwardNo = forwardNo + int(line[-1])
            depth = depth + (aim*int(line[-1]))
        if "down" in line:
            aim = aim + int(line[-1])
        if "up" in line:
            aim = aim - int(line[-1])
            
    print(depth)
    print(forwardNo)
    print(aim)
    print(depth * forwardNo)