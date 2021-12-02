with open("sweeps.txt", 'r') as inFile:
    currentNumber = 0
    secondNumber = 0
    thirdNumber = 0
    lastNumber = 0
    currentTotal = 0
    pastTotal = 0
    count = 0
    for line in inFile:
        if currentNumber == 0:
            currentNumber = int(line)
        else:
            lastNumber = thirdNumber
            thirdNumber = secondNumber
            secondNumber = currentNumber
            currentNumber = int(line)
            print(currentNumber, secondNumber, thirdNumber, lastNumber)
            if int(currentNumber + secondNumber + thirdNumber) > int(secondNumber + thirdNumber + lastNumber) and lastNumber != 0 and thirdNumber != 0 and currentNumber != 0 and secondNumber != 0:
                count += 1
        
    



        # print(currentNumber, secondNumber, lastNumber)
        # if currentNumber == 0:
            # currentNumber = int(line)
        # if currentNumber != 0 and secondNumber == 0:
            # secondNumber = currentNumber
            # currentNumber = int(line)            
        # if currentNumber != 0 and secondNumber != 0 and lastNumber == 0:
            # lastNumber = secondNumber
            # secondNumber = currentNumber
            # currentNumber = int(line)
        # else:
            # lastNumber = secondNumber
            # secondNumber = currentNumber
            # currentNumber = int(line)
            # if currentTotal == 0:
                # currentTotal = lastNumber + secondNumber + currentNumber
            # else:
                # print(lastNumber, secondNumber, currentNumber,currentTotal)
                # pastTotal = currentTotal
                # currentTotal = lastNumber + secondNumber + currentNumber
                # if int(currentTotal) > int(pastTotal) and pastTotal != 0:
                    # count += 1
                    # print(lastNumber, secondNumber, currentNumber, currentTotal, pastTotal, "true")
                # else:
                    # print(lastNumber, secondNumber, currentNumber, currentTotal, pastTotal, "false")
            

            
    print(count)