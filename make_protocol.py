import os
import argparse

def list_of_strings(arg):
    return arg.split(',')

def make_protocol(args):
    with open("protocol/protocol_test_for.txt", "a+") as f:
        for directories in args.in_dir:
            if args.real=="True":
                for file in os.listdir(directories):
                    if file[-3:] == 'wav' or file[-3:]=='mp3':
                        f.write('real_'+file +" bonafide" +"\n")
            elif args.real=="False":
                for file in os.listdir(directories):
                    if file[-3:] == 'wav' or file[-3:]=='mp3':
                        f.write('fake_'+file +" spoof" +"\n")
        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "in_dir",
        metavar="in-dir",
        help="path to the dataset directory.",
        type=list_of_strings,
    )
    parser.add_argument(
        "real",
        type=str,
    )
    # parser.add_argument()
    args = parser.parse_args()
    make_protocol(args)
