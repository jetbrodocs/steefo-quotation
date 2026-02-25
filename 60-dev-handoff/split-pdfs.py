"""
Split sample quotation PDFs into individual equipment item files.
Run from the project root: python3 60-dev-handoff/split-pdfs.py
"""

from pypdf import PdfReader, PdfWriter
import os

BASE = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.join(os.path.dirname(BASE), "00-inbox")

# --- QTN-542-R2 (42 pages, 1-indexed) ---
QTN_542_PATH = os.path.join(INBOX, "Technical Offer_QTN-542-R2_P460.pdf")
QTN_542_OUT = os.path.join(BASE, "sample-pdfs", "qtn-542-items")

# Page ranges are 1-indexed inclusive, converted to 0-indexed for pypdf
QTN_542_ITEMS = [
    ("01-510mm-heavy-duty-roughing-mill", 5, 8),
    ("02-410mm-continuous-intermediate-mill", 9, 11),
    ("03-360mm-continuous-intermediate-mill", 12, 14),
    ("04-320mm-continuous-intermediate-mill", 15, 17),
    ("05-280mm-continuous-finishing-mill-6-stand", 18, 20),
    ("06-auxiliary-equipment", 21, 23),
    ("07-electricals", 24, 24),
    ("08-automatic-cooling-bed-twin-channel-cold-shear", 25, 28),
    # Note: Dividing Shear starts at bottom of page 28 — sharing page with Cooling Bed
    # In the actual PDF, page 28 has Cooling Bed content + start of Dividing Shear
    # For splitting purposes, we include page 28 in Cooling Bed and skip separate Dividing Shear split
    # since it doesn't have its own dedicated pages in QTN-542
    ("09-bar-finishing-bundling-tying-machine", 29, 31),
    ("10-tmt-system", 32, 35),
    ("11-utm-machine", 36, 36),
]

# --- QTN-569 (75 pages, 1-indexed) ---
QTN_569_PATH = os.path.join(INBOX, "Technical Offer_QTN-569_P480.pdf")
QTN_569_OUT = os.path.join(BASE, "sample-pdfs", "qtn-569-items")

QTN_569_ITEMS = [
    ("01-550mm-heavy-duty-roughing-mill", 6, 9),
    ("02-400mm-continuous-intermediate-mill", 10, 12),
    ("03-360mm-continuous-intermediate-mill", 13, 15),
    ("04-320mm-continuous-intermediate-mill", 16, 18),
    ("05-280mm-continuous-finishing-mill-4-stand", 19, 21),
    ("06-auxiliary-equipment", 22, 28),
    ("07-electricals", 29, 37),
    ("08-automatic-cooling-bed-twin-channel-cold-shear", 38, 41),
    ("09-continuous-operating-dividing-shear-tmt-bars", 42, 42),
    ("10-bar-finishing-bundling-tying-machine", 43, 44),
    ("11-tmt-system", 45, 50),
    ("12-central-oil-lubrication-system", 51, 52),
    ("13-wire-rod-block-mill", 56, 70),
]


def split_pdf(input_path, output_dir, items):
    """Split a PDF into individual item files based on page ranges."""
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    print(f"\nProcessing: {os.path.basename(input_path)} ({total_pages} pages)")

    os.makedirs(output_dir, exist_ok=True)

    for name, start_page, end_page in items:
        writer = PdfWriter()
        for page_num in range(start_page - 1, end_page):  # Convert to 0-indexed
            writer.add_page(reader.pages[page_num])

        output_path = os.path.join(output_dir, f"{name}.pdf")
        with open(output_path, "wb") as f:
            writer.write(f)

        page_count = end_page - start_page + 1
        print(f"  {name}.pdf — pages {start_page}-{end_page} ({page_count} pages)")

    print(f"  Done. {len(items)} files written to {output_dir}")


if __name__ == "__main__":
    split_pdf(QTN_542_PATH, QTN_542_OUT, QTN_542_ITEMS)
    split_pdf(QTN_569_PATH, QTN_569_OUT, QTN_569_ITEMS)
    print("\nAll splits complete.")
