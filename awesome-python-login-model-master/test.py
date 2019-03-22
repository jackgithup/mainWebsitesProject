import argparse
parser = argparse.ArgumentParser()
parser.add_argument('echo')     # add_argument()指定程序可以接受的命令行选项
args = parser.parse_args()      # parse_args()从指定的选项中返回一些数据
print(args)
print(args.echo)