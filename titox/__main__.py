from argparse import ArgumentParser, FileType
from jinja2 import Template, Environment

environment = Environment(
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
)

def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--items', nargs='+', required=True)
    parser.add_argument('-j', '--j2', type=FileType('r'), required=True)
    args = parser.parse_args()
    print(environment.from_string(args.j2.read()).render(items=args.items))

if __name__ == '__main__':
    main()
