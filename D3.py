import random
import time

max_num = 30000

def get_val(val, dict):
    for val, value in dict.items():
         if val == value:
             return val
 
    return 0

def problem_code():
    start = time.time()
    first_list = [random.randint(0, max_num*3) for _ in range(max_num)]
    #print("First list generated", first_list)
    second_list = [random.randint(0, max_num*4) for _ in range(max_num)]
    num_list = []
    for num in first_list:
        if num in second_list:
            num_list.append(num)
    print("Run Time for problem code: ",time.time() - start)
    #print(len(num_list))
    return first_list, second_list

def optimized_code(first_list, second_list):
    start = time.time()
    first_dict = {}
    for val in first_list:
        if val in first_dict:
            first_dict[val] += 1
        else:
            first_dict[val] = 1
    #print(first_dict)
    second_dict = {}
    for val in second_list:
        if val in second_dict:
            second_dict[val] += 1
        else:
            second_dict[val] = 1
    num_list_2 = []
    for val in first_dict:
        if val in second_dict:
            for i in range (first_dict[val]):
                num_list_2.append(val)
    print("Run time for solution: ", time.time() - start)
    #print(len(num_list_2))


if __name__ == '__main__':
    first_list, second_list = problem_code()
    optimized_code(first_list, second_list)