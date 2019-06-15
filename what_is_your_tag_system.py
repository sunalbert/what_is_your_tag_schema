# coding=utf-8
# /*
#  * @Author: jasonhavend
#  * @Date: 2019-06-13 10:02:40
#  * @Last Modified by:   jasonhavend
#  * @Last Modified time: 2019-06-13 10:02:40
#  */
import pandas as pd
import argparse
import os


def look_only_one_column(col_list):
    prefixs = set()
    labels = set()
    for tag in col_list[1:]:  # skip the first line
        tag = str(tag)
        if tag == 'O' or tag == 'o' or tag =='0':
            prefixs.add('O')            
            labels.add('O')
        elif '-' in tag:
            prefixs.add(tag.split('-')[0])
            labels.add(tag.split('-')[1])
        elif '_' in tag:
            prefixs.add(tag.split('_')[0])
            labels.add(tag.split('_')[1])
        else:
            labels.add(tag)
    print('Prefix:', end=' ')
    print(prefixs)
    print('Label:', end=' ')
    print(labels)


def main(args):
    # load data
    if not os.path.exists(args.file_path):
        print('{} not exists!'.format(args.file_path))
        return
    print('FILENAME = {}'.format(args.file_path))    
    seps = [',', '\t', ' ']
    data = None
    for sep in seps:
        try:
            data = pd.read_csv(args.file_path, sep=sep)
        except ValueError as e:
            continue
    if data is None:
        print('The format of {} is not right for dataframe!')
        return
    data.columns = list(range(1, len(data.columns)+1))
    for col in data.columns[1:]:
        print('Look column = {}'.format(col))
        look_only_one_column(data[col])
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("--file_path",
                        default='train.csv',
                        type=str,
                        required=True,
                        help="The input file path. Should can be read as the dataframe' format using 'pandas.read_csv'")
    args = parser.parse_args()
    main(args)
