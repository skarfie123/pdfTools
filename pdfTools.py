import argparse
from tools.extract import extract
from tools.merge import merge
from tools.rotate import rotate

parser = argparse.ArgumentParser(description="PDF Tools by Skarfie123")
subparsers = parser.add_subparsers(help="desired tool", dest="tool")
parser.add_argument("-v", "--verbose", help="verbose output text", action="store_true")

# tool: extract
extract_parser = subparsers.add_parser(
    "extract", help="extract specified pages", description="Extract specified pages"
)
extract_parser.add_argument("infile", help="input file")
extract_parser.add_argument("pages", help='pages to extract eg. "1-3,6"')
extract_parser.add_argument("outfile", help="output file")

# tool: merge
merge_parser = subparsers.add_parser(
    "merge",
    help="merge multiple pdfs into one",
    description="Merge multiple pdfs into one",
)
merge_parser.add_argument("-i", "--infiles", nargs="+", help="input files")
merge_parser.add_argument("-o", "--outfile", help="output file")

# tool: rotate
rotate_parser = subparsers.add_parser(
    "rotate",
    help="rotate specified 90 degrees clockwise",
    description="Rotate specified 90 degrees clockwise",
)
rotate_parser.add_argument("infile", help="input file")
rotate_parser.add_argument("pages", help='pages to rotate eg. "1-3,6"')
rotate_parser.add_argument("outfile", help="output file")

# parse args
args = parser.parse_args()
logger = print if args.verbose else lambda *args, **kwargs: None
logger("Arguments:", args)

# execute
if args.tool == "extract":
    if not extract(args.infile, args.pages, args.outfile, logger):
        extract_parser.print_help()
elif args.tool == "merge":
    if not merge(args.infiles, args.outfile, logger):
        merge_parser.print_help()
elif args.tool == "rotate":
    if not rotate(args.infile, args.pages, args.outfile, logger):
        rotate_parser.print_help()
else:
    parser.print_help()