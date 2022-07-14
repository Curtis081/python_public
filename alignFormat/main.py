def list_elems_to_str(input_list):
    return list(map(str, input_list))


def get_align_format(input_list, align_direction='^'):
    additional_blank = 4
    data_list = list_elems_to_str(input_list)

    max_len_elem = max(data_list, key=len)
    max_len = len(max_len_elem) + additional_blank
    align_format = '{{:{0}'.format(align_direction) + '{0}'.format(max_len) + 's}'
    return align_format


def get_align_format_demo():
    str_list = ['hello', 'It\'s me', 'abcdefghijklmnopqrstuvwxyz']
    num_list = [123132123, 45465464655, 78978978979879]

    num_list = list_elems_to_str(num_list)

    str_align_format = get_align_format(str_list)
    num_align_format = get_align_format(num_list)
    align_format = str_align_format + num_align_format

    for str_data, num_data in zip(str_list, num_list):
        print(align_format.format(str_data, num_data))


if __name__ == '__main__':
    get_align_format_demo()