def compare_string(input_str, compared_str):
    if (input_str == compared_str):
        # print(input_str + " is find")
        return True
    else:
        return False


def compare_list_value_service(input_list, compared_str):
    compared_result = False
    # prepare to concate dictionary value or list element
    new_list = []
    for value in input_list:
        # print(value)

        if (isinstance(value, dict)):
            dict_value_to_list = list(value.values())
            # append each element in list to new list
            for value in dict_value_to_list:
                new_list.append(value)

        elif (isinstance(value, list)):
            # append each element in list to new list
            for v in value:
                new_list.append(v)

        elif (isinstance(value, tuple)):
            # append each element in tuple to new list
            for v in value:
                new_list.append(v)

        else:
            compared_result_temp = compare_string(value, compared_str)
            compared_result = compared_result | compared_result_temp

    return new_list, compared_result


def compare_list_value_service_loop(temp_list, compared_str):
    compared_result = False

    # compare to the indicate string while-Loop until list is empty
    while len(temp_list) > 0:
        temp_list, compared_result_temp = compare_list_value_service(temp_list, compared_str)
        compared_result = compared_result | compared_result_temp

    return compared_result


if __name__ == '__main__':
    test_list = [1, 'a', 1.5, 'bux', {1: 'c', 2: 'b'}, [1, 2, 3]]

    thirdLinkList = [{0: "apple"}, {'v1': ['xxx', 'yyy'], 'v2': ['test', 'ball']}, {2: 'cat'},
                     {3: ['tpp', 'ppt'], 4: ['tp', 'dis']}]
    secondLinkList = ([{0: thirdLinkList}, {1: "dog"}, {2: "egg"}])
    firstLinkList = [{0: secondLinkList}, {1: "fish"}, {2: "grow"}]

    compared_str = 'apple'
    r = compare_list_value_service_loop(firstLinkList, compared_str)

    print(compared_str + " is find") if r else print(compared_str + " is not find")

