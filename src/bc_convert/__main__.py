import argparse
import os.path
import sys
from pathlib import Path
from typing import Sequence, Optional

from src.bc_convert.converter.alipay import Alipay
from src.bc_convert.converter.wechat import Wechat


def convert(converter):
    converter.parse()
    converter.write()


def choose_converter(input_file, outdir, config_file):
    current_dir = os.path.dirname(os.path.realpath('__file__'))
    input_file_name = Path(input_file).stem
    output_file = os.path.join(outdir, input_file_name + '.bean')
    print(f'{input_file} -> {output_file}, using config: {config_file}')

    absolute_input_file = os.path.join(current_dir, input_file)
    absolute_config_file = os.path.join(current_dir, config_file)

    if input_file_name.startswith('alipay'):
        converter = Alipay(absolute_input_file, absolute_config_file)
        convert(converter)
    elif input_file_name.startswith('微信'):
        converter = Wechat(absolute_input_file, absolute_config_file)
        convert(converter)
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
