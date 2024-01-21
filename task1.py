import argparse
from pathlib import Path
import shutil
import sys

# parse arguments from command line
def parse_argv() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Copying files from directories and sorting them by type')
    parser.add_argument('-s', '--sources', type=Path, required=True,  help='Path to source files')
    parser.add_argument('-o', '--output',type=Path, default=Path('dict'), help='Path to output files (default is dict)')
    return parser.parse_args()

# function to copy files from directory and sort them by type
def recursion_copying_files(source: Path, output: Path) -> None:
    for element in source.iterdir():
        try:
            if element.is_dir():
                recursion_copying_files(element, output)
            else:
                folder = output / element.suffixes[-1][1:]
                folder.mkdir(parents=True, exist_ok=True)
                shutil.copy(element, folder)
        except Exception as e:
            print(f'Problem with access to {element}: {e}')

# main function Task1
def task1() -> None:
    args = parse_argv()
    if Path(args.sources).exists():
        recursion_copying_files(args.sources, args.output)
    else:
        print(f'{args.sources} path does not exist')
        sys.exit(0)


if __name__ == '__main__':
    task1()