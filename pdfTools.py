import argparse

parser = argparse.ArgumentParser(description="PDF Tools by Skarfie123")
subparsers = parser.add_subparsers(help="desired tool", dest="tool")
parser.add_argument("-v", "--verbose", help="Verbose output text", action="store_true")

extract_parser = subparsers.add_parser(
    "extract", help="extract specified pages", description="Extract specified pages"
)
extract_parser.add_argument("infile", help="input file")
extract_parser.add_argument("pages", help='pages to extract eg. "1-3,6"')
extract_parser.add_argument("outfile", help="output file")

merge_parser = subparsers.add_parser(
    "merge",
    help="merge multiple pdfs into one",
    description="Merge multiple pdfs into one",
)
merge_parser.add_argument("outfile", help="output file")
merge_parser.add_argument("-i", "--inputs", nargs="+")

rotate_parser = subparsers.add_parser(
    "rotate",
    help="rotate specified 90 degrees clockwise",
    description="Rotate specified 90 degrees clockwise",
)
rotate_parser.add_argument("infile", help="input file")
rotate_parser.add_argument("pages", help='pages to rotate eg. "1-3,6"')
rotate_parser.add_argument("outfile", help="output file")

args = parser.parse_args()
logger = print if args.verbose else lambda *args, **kwargs: None
logger("Arguments:", args)
