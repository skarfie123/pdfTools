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
required_merge_parser = merge_parser.add_argument_group("required arguments")
required_merge_parser.add_argument(
    "-i", "--infiles", nargs="+", help="input files", required=True
)
required_merge_parser.add_argument("-o", "--outfile", help="output file", required=True)

# tool: rotate
rotate_parser = subparsers.add_parser(
    "rotate",
    help="rotate specified pages",
    description="Rotate specified pages",
)
rotate_parser.add_argument("infile", help="input file")
rotate_parser.add_argument("pages", help='pages to rotate eg. "1-3,6"')
rotate_parser.add_argument("outfile", help="output file")
rotate_parser.add_argument(
    "-a",
    "--angle",
    help="angle to rotate by (degrees clockwise) - default: 90",
    type=int,
    default=90,
    choices=[90, 180, 270],
)

# parse args
args = parser.parse_args()
logger = print if args.verbose else lambda *args, **kwargs: None
logger("Arguments:", args)

# execute
if args.tool == "extract":
    if not extract(args.infile, args.pages, args.outfile, logger):
        extract_parser.print_usage()
elif args.tool == "merge":
    if not merge(args.infiles, args.outfile, logger):
        merge_parser.print_usage()
elif args.tool == "rotate":
    if not rotate(args.infile, args.pages, args.outfile, args.angle, logger):
        rotate_parser.print_usage()
else:
    parser.print_help()