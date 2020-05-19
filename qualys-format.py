import csv
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("You need input Qualys report file path.")
        return -1
    if not os.path.exists(sys.argv[1]):
        print("%s is not exist." % sys.argv[1])
        return -1

    resultfile = sys.argv[1].split('.')[0] + '_formatted' + '.' + sys.argv[1].split('.')[1]

    with open(sys.argv[1]) as f:
        f_csv = csv.reader(f)
        while True:
            headers = next(f_csv)
            if len(headers) == 41 and headers[2] == "DNS":
                break
        with open(resultfile, 'w') as fout:
            result_writer = csv.writer(fout, delimiter='~')
            result_writer.writerow(headers)
            for row in f_csv:
                if row[2] == '':
                    continue
                if len(row) != 41:
                    print("Report format is error.")
                    if os.path.exists(resultfile):
                        os.remove(resultfile)
                    return -1
                result_writer.writerow(row)
            result_writer.writerow('0')

if __name__ == '__main__':
    main()
