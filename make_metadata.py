import os
import argparse

def make_protocol(args):
    count = 0
    ind = 0
    with open(f"metadata/metadata_for{ind}.txt", "w") as f:
        for file in os.listdir(args.in_dir):    
            if file[-3:] == 'wav' or file[-3:]=='mp3':
                count+=1
                f.write(file+"\n")
            if count==10:
                ind+=1
                count = 0
                f.close()
                f =open(f"metadata/metadata_for{ind}.txt", "w")
                f.write(file+"\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "in_dir",
        metavar="in-dir",
        help="path to the dataset directory.",
        type=str,
    )
    args = parser.parse_args()
    make_protocol(args)
