from PyPDF2 import PdfFileMerger


def merge(infiles, outfile, logger):
    logger("--- pdfTools: merge ---")

    if len(infiles) == 1:
        print("Please provide more than 1 infile")
        return False
    if outfile in infiles:
        print("The outfile can not be one of the infiles")
        return False

    merger = PdfFileMerger()

    for infile in infiles:
        input = open(infile, "rb")
        merger.append(input)
        logger("Appended:", infile)

    output = open(outfile, "wb")
    merger.write(output)
    logger("Wrote:", outfile)
    return True