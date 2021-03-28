# https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen
# print unique letters divided into k sets 


def merge_the_tools(string, k):
    counter = 0
    main_list = []
    sublist = []

    for letter in string:
        if counter < k:
            counter += 1
            sublist.append(letter)
        else:
            main_list.append(sublist)
            counter = 0
            sublist = []
            counter += 1
            sublist.append(letter)
    main_list.append(sublist)
    final_result = [print("".join(list(dict.fromkeys(i)))) for i in main_list]

merge_the_tools("AABCAAADA", 3)
