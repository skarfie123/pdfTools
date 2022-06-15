from utils import parse_pages
from PyPDF2 import PdfFileWriter, PdfFileReader


def substitute(recipient, donor, pages, outfile, logger):
    logger("--- pdfTools: substitute ---")

    if outfile == recipient or outfile == donor:
        print("Error: The outfile can not be the recipient or donor")
        return False

    recipient_pdf = PdfFileReader(open(recipient, "rb"))
    donor_pdf = PdfFileReader(open(donor, "rb"))
    page_list = parse_pages(pages)
    logger("Page List:", [p + 1 for p in page_list])
    output = PdfFileWriter()

    for p in range(recipient_pdf.getNumPages()):
        if p in page_list:
            try:
                output.addPage(donor_pdf.getPage(p))
            except IndexError:
                print(
                    f"Error: Cannot subtitute a page that doesn't exist in donor - {p+1}"
                )
                return False
        else:
            output.addPage(recipient_pdf.getPage(p))

    output_file = open(outfile, "wb")
    output.write(output_file)
    logger("Wrote:", outfile)
    return True
