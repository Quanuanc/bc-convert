import argparse
import os.path
import sys
from pathlib import Path
from typing import Sequence, Optional


def choose_converter(input_file, outdir, config_file):
    input_file_name = Path(input_file).stem
    output_file_name = outdir + os.sep + input_file_name + '.bean'
    print(f'{input_file} -> {output_file_name}, using config: {config_file}')

    if input_file_name.startswith('alipay'):
        print('alipay')
    elif input_file_name.startswith('微信'):
        print('wechat')
    else:
        print('not suitable converter')


def main_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='A beancount importer')

    parser.add_argument(
        '--input',
        '-i',
        type=str,
        help=f'input file'
    )

    parser.add_argument(
        '--outdir',
        '-o',
        type=str,
        help=f'output directory'
    )

    parser.add_argument(
        '--config',
        '-c',
        type=str,
        help=f'config file'
    )

    return parser


def main(cli_args: Sequence[str], prog: Optional[str] = None):
    parser = main_parser()
    if prog:
        parser.prog = prog
    args = parser.parse_args(cli_args)

    if not args.config:
        parser.print_help()

    if args.input:
        choose_converter(args.input, args.outdir, args.config)


if __name__ == '__main__':
    main(sys.argv[1:], 'python -m bc_convert')
