import csv
import os
#准备10000行的csv作为样例，进行拆分
example_path = 'all_train.csv' # 需要拆分文件的路径
example_result_valid = 'valid.csv' # 拆分后文件的路径
example_result_train = 'train.csv' # 拆分后文件的路径

with open(example_path, 'r', newline='') as example_file:
    example = csv.reader(example_file)

    i = 1
    for row in example:
        if(i%10 ==0):
            if not os.path.exists(example_result_valid):
                with open(example_result_valid, 'w', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1
            else:
                with open(example_result_valid, 'a', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1
        else:
            if not os.path.exists(example_result_train):
                with open(example_result_train, 'w', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1
            else:
                with open(example_result_train, 'a', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1
    print("finished!")
