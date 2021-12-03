import numpy as np

with open("input.txt", "r") as f:
    lines = np.array([list(line.replace("\n", "")) for line in f.readlines()])    
    
    def oxygen_bit(index, matrix):
        if len(matrix) == 1:
            return(matrix[0])
        else:
            lines_t = matrix.transpose()
            
            line_check = [int(i) for i in lines_t[index]]
            ones = np.count_nonzero(line_check)
            zeros = len(line_check) - ones

            if ones > zeros:
                winning_value = "1"
            elif ones < zeros:
                winning_value = "0"
            else:
                winning_value = "1"
        correct_lines = np.array([line for line in matrix if line[index] == winning_value])            
        
        return(oxygen_bit(index + 1, correct_lines))

    def co2_bit(index, matrix):
        if len(matrix) == 1:
            return(matrix[0])
        else:
            lines_t = matrix.transpose()
            
            line_check = [int(i) for i in lines_t[index]]
            ones = np.count_nonzero(line_check)
            zeros = len(line_check) - ones

            if ones > zeros:
                winning_value = "0"
            elif ones < zeros:
                winning_value = "1"
            else:
                winning_value = "0"
        correct_lines = np.array([line for line in matrix if line[index] == winning_value])            
        
        return(co2_bit(index + 1, correct_lines))

oxygen = oxygen_bit(0, lines)
co2 = co2_bit(0, lines)
oxygen_int = int("".join(oxygen),2)
co2_int = int("".join(co2),2)

print(oxygen_int , co2_int)
print(oxygen_int * co2_int)


        
    



