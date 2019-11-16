import os
import re


def main():
    try:
        source = open('5500ingles.txt', 'r',  encoding = "ISO-8859-1")
        csv = open('5500ingles.csv', 'w+',  encoding = "ISO-8859-1")
        csv.write("AnswerType@Question\n")
        lines = source.readlines()
        for line in lines:
            csv_line = line.split(" ", 1)
            type = csv_line[0].split(":")
            print(type)
            if (type[0] == "HUM" and type[1] == "ind") or type[0] == "NUM" or type[0] == "LOC":
                csv.write(csv_line[0] + '@ ' + csv_line[1][:-1] + ' \n')
    except Exception as e:
        print(e)
    finally:
        source.close()
        csv.close()


if __name__ == '__main__':
    main()
