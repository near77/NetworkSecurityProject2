import sys
from model import user_classify

def main():
    print(sys.argv[1])
    user_classify(sys.argv[1])

if __name__ == "__main__":
    main()