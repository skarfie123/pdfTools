import argparse
from tools.delete import delete
from tools.extract import extract
from tools.merge import merge
from tools.rotate import rotate
from tools.substitute import substitute

parser = argparse.ArgumentParser(description="pdfTools by skarfie123")
subparsers = parser.add_subparsers(title="tools", dest="tool", metavar="{TOOL}")
parser.add_argument("-v", "--verbose", help="verbose output text", action="store_true")

# tool: delete
delete_parser = subparsers.add_parser(
    "delete", help="delete specified pages", description="Delete specified pages"
)
delete_parser.add_argument("infile", help="input file")
delete_parser.add_argument("pages", help='pages to delete eg. "1-3,6"')
delete_parser.add_argument("outfile", help="output file")

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

# tool: substitute
substitute_parser = subparsers.add_parser(
    "substitute",
    help="substitute specified pages from donor into recipient",
    description="Substitute specified pages from donor into recipient",
)
substitute_parser.add_argument("recipient", help="input file as base")
substitute_parser.add_argument("donor", help="input file to pick substitutes")
substitute_parser.add_argument("pages", help='pages to substitute eg. "1-3,6"')
substitute_parser.add_argument("outfile", help="output file")

# parse args
args = parser.parse_args()
logger = print if args.verbose else lambda *args, **kwargs: None
logger("Arguments:", args)

# execute
if args.tool == "delete":
    if not delete(args.infile, args.pages, args.outfile, logger):
        delete_parser.print_usage()
elif args.tool == "extract":
    if not extract(args.infile, args.pages, args.outfile, logger):
        extract_parser.print_usage()
elif args.tool == "merge":
    if not merge(args.infiles, args.outfile, logger):
        merge_parser.print_usage()
elif args.tool == "rotate":
    if not rotate(args.infile, args.pages, args.outfile, args.angle, logger):
        rotate_parser.print_usage()
elif args.tool == "substitute":
    if not substitute(args.recipient, args.donor, args.pages, args.outfile, logger):
        substitute_parser.print_usage()
else:
    parser.print_help()