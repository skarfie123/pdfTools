def parse_pages(pages):
    page_ranges = (x.split("-") for x in pages.split(","))
    page_list = [i for r in page_ranges for i in range(int(r[0]) - 1, int(r[-1]))]
    return page_list
