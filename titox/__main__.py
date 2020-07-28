from argparse import ArgumentParser, FileType


def main():

    parser = ArgumentParser()
    parser.add_argument('-i', '--items', nargs='+', required=True)
    parser.add_argument('-j', '--j2', type=FileType('r'), required=True)
    args = parser.parse_args()


if __name__ == '__main__':
    main()
