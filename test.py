import argparse


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", type=str, help="test")
    args = parser.parse_args()
    print(args.test)
    
    
    if args.test == "testtest":
        print("saaaameeee")
    else:
        print("diiiffffff")