def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x for x in [len(vector) for vector in vector_variables[1:]])

print(vector_size_check([1,2,3], [2,3,4], [5,6,7])) #True
print(vector_size_check([1, 3], [2,4], [6,7])) #True
print(vector_size_check([1, 3, 4], [4], [6,7])) #False

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [sum(elements) for elements in zip(*vector_variables)]

print(vector_addition([1, 3], [2, 4], [6, 7])) #Expected value: [9, 14]
print(vector_addition([1, 5], [10, 4], [4, 7])) #Expected value: [15, 16]

def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [elements[0]*2 - sum(elements) for elements in zip(*vector_variables)]

print(vector_subtraction([1, 3], [2, 4])) # Expected value: [-1, -1]
print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]

def scalar_vector_product(alpha, vector_variables):
    return [alpha * elements for elements in vector_variables]

print (scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15
print (scalar_vector_product(3,[2,2])) # Expected value: [6, 6]
print (scalar_vector_product(4,[1])) # Expected value: [4]
