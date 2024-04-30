import os
import argparse

def list_of_strings(arg):
    return arg.split(',')

def make_protocol(args):
    with open("protocol.txt", "w") as f:
        for directories in args.in_dir:
            if args.real:
                for file in os.listdir(directories):
                    f.write("XYZ " + file[:-4] +" - " + " - " + " bonafide" +"\n")
            else:
                for file in os.listdir(directories):
                    f.write("XYZ " + file[:-4] +" - " + " A01 " + " spoof" +"\n")
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
        type=bool,
    )
    # parser.add_argument()
    args = parser.parse_args()
    make_protocol(args)
