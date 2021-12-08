def calculate(segment):
    digits = [0] * 10
    display = [0] * 7
    # [0/A]
    # [1/B][2/C] 
    # [3/D]
    # [4/E][5/F]
    # [6/G]
    possible= ["a", "b", "c", "d", "e", "f", "g"]
    signal = sorted(segment[0], key = len )
    signal = [''.join(sorted(s)) for s in signal]
    number = segment[1]
    len6 = []
    for digit in signal:
        # Remove the easiests ones. 
        match len(digit):
            case 2:
                digits[1] = digit              
                CF = [num for num in digit]   
            case 3: 
                digits[7] = digit
                A = [line for line in digit if line not in CF] 
                display[0] = A[0]
            case 4:
                digits[4] = digit
                lines = [line for line in digit if line not in CF + A]
                BD = lines
            case 6:
                len6.append(digit) 
                if not all(elem in digit for elem in CF):
                    for elem in CF:
                        if elem in digit:
                            display[5] = elem
                        else: 
                            display[2] = elem
                if not all(elem in digit for elem in BD):
                    for elem in BD:
                        if elem in digit:
                            display[1] = elem
                        else:
                            display[3] = elem               
            case 7:
                digits[8] = digit      
        
    ABCDF = [x for x in display if x != 0]
    
    for digit in len6:
        if all(elem in digit for elem in ABCDF):
            display[6]= [i for i in digit if i not in ABCDF][0]
    
    display[4] = [x for x in possible if x not in display][0]

    remaining = [x for x in signal if x not in digits]
    for digit in remaining:
        if len(digit) == 6:
            if display[3] not in digit:
                digits[0] = digit
            elif display[2] not in digit:
                digits[6] = digit
            elif display[4] not in digit:
                digits[9] = digit
        elif len(digit) == 5:
            if display[1] not in digit and display[5] not in digit:
                digits[2] = digit
            elif display[1] not in digit and display[4] not in digit:
                digits[3] = digit
            elif display[2] not in digit and display[4] not in digit:
                digits[5] = digit
    
    for i , num in enumerate(number):
        number[i] = "".join(sorted(num))

    answer = []

    for num in number:
        answer.append(str(digits.index(num)))

    answer = int("".join(answer))

    return(answer)

with open("input.txt", "r") as f:
    segments = [segment.split(" | ") for segment in f.readlines()]
    for segment in segments:
        segment[0] = segment[0].split(" ")
        segment[1] = segment[1].replace("\n", "").split(" ")
        
    total = 0
    for segment in segments:
        total += calculate(segment)

    print(total)