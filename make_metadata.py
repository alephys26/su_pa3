import os
import argparse

def list_of_strings(arg):
    return arg.split(',')

def make_protocol(args):
    with open("metadata_custom.txt", "w") as f:
        for directories in args.in_dir:
            for file in os.listdir(directories):
                if file[-3:] == 'wav' or file[-3:]=='mp3':
                    f.write(file+"\n")
        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "in_dir",
        metavar="in-dir",
        help="path to the dataset directory.",
        type=list_of_strings,
    )
    args = parser.parse_args()
    make_protocol(args)
