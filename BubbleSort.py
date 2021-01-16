def bubble_sort(input_list):
    is_end = False
    fin_adjust = 1
    while (not is_end):
        loop_swap = False
        for index in range(len(input_list) - fin_adjust):
            if input_list[index] < input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
                loop_swap = True
        if not loop_swap:
            is_end = True
        fin_adjust += 1 # 端から順番に確定していくから
    print(input_list)

bubble_sort([2,8,3,5,1,7,4,9,6,10])
