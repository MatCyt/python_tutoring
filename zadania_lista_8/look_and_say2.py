import numpy as np
import argparse



def split_to_unique(converted_numbers):
    ''' split list of strings to lists of unique values grouped together'''
    result = [[]]

    for n in converted_numbers:
        if n not in result[-1]:
            result.append(list(n))
        else:
            result[-1].append(n)

    del result[0]
    return result

def look_and_say(argsn):
    converted_numbers = [i for i in str(argsn)]

    unique_values = split_to_unique(converted_numbers)

    output = ''

    for i in unique_values:
        count = len(i)
        value = np.unique(i)[0]
        count_value = '{}{}'.format(str(count), value)
        output = output + count_value

    return output

def main():
    my_parser = argparse.ArgumentParser(description='dlugosc ciagu')
    my_parser.add_argument('n', type=int)
    args = my_parser.parse_args()

    output = look_and_say(args.n)

    print(output)
    return output


if __name__ == '__main__':
    main()


