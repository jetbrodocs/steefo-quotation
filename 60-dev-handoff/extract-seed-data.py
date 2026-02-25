"""
Extract seed data (introduction, terms, exclusions) from sample PDFs.
Run from the project root: python3 60-dev-handoff/extract-seed-data.py
"""

import pdfplumber
import os

BASE = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.join(os.path.dirname(BASE), "00-inbox")
SEED_DIR = os.path.join(BASE, "seed-data")
os.makedirs(SEED_DIR, exist_ok=True)

QTN_542 = os.path.join(INBOX, "Technical Offer_QTN-542-R2_P460.pdf")
QTN_569 = os.path.join(INBOX, "Technical Offer_QTN-569_P480.pdf")


def extract_pages(pdf_path, page_numbers):
    """Extract text from specific pages (1-indexed)."""
    texts = []
    with pdfplumber.open(pdf_path) as pdf:
        for pn in page_numbers:
            page = pdf.pages[pn - 1]
            text = page.extract_text()
            if text:
                texts.append(text)
    return "\n\n".join(texts)


def extract_tables(pdf_path, page_numbers):
    """Extract tables from specific pages (1-indexed)."""
    all_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for pn in page_numbers:
            page = pdf.pages[pn - 1]
            tables = page.extract_tables()
            for table in tables:
                all_tables.append(table)
    return all_tables


# --- Introduction text (same in both PDFs) ---
print("Extracting introduction text...")
intro_text = extract_pages(QTN_569, [1])
with open(os.path.join(SEED_DIR, "introduction-raw.txt"), "w") as f:
    f.write(intro_text)
print(f"  Saved introduction-raw.txt")

# --- Terms & Conditions from QTN-542 (pages 40-41) ---
print("Extracting terms from QTN-542 (pages 40-41)...")
terms_542 = extract_pages(QTN_542, [40, 41])
with open(os.path.join(SEED_DIR, "terms-qtn-542-raw.txt"), "w") as f:
    f.write(terms_542)
print(f"  Saved terms-qtn-542-raw.txt")

# --- Terms & Conditions from QTN-569 (pages 73-74) ---
print("Extracting terms from QTN-569 (pages 73-74)...")
terms_569 = extract_pages(QTN_569, [73, 74])
with open(os.path.join(SEED_DIR, "terms-qtn-569-raw.txt"), "w") as f:
    f.write(terms_569)
print(f"  Saved terms-qtn-569-raw.txt")

# --- Exclusions from QTN-542 (page 42) ---
print("Extracting exclusions from QTN-542 (page 42)...")
excl_542 = extract_pages(QTN_542, [42])
with open(os.path.join(SEED_DIR, "exclusions-qtn-542-raw.txt"), "w") as f:
    f.write(excl_542)
print(f"  Saved exclusions-qtn-542-raw.txt")

# --- Exclusions from QTN-569 (page 75) ---
print("Extracting exclusions from QTN-569 (page 75)...")
excl_569 = extract_pages(QTN_569, [75])
with open(os.path.join(SEED_DIR, "exclusions-qtn-569-raw.txt"), "w") as f:
    f.write(excl_569)
print(f"  Saved exclusions-qtn-569-raw.txt")

# --- Scope of Supply tables from QTN-542 (pages 37-39) ---
print("Extracting scope of supply from QTN-542 (pages 37-39)...")
scope_542 = extract_pages(QTN_542, [37, 38, 39])
with open(os.path.join(SEED_DIR, "scope-of-supply-qtn-542-raw.txt"), "w") as f:
    f.write(scope_542)
print(f"  Saved scope-of-supply-qtn-542-raw.txt")

# --- Scope of Supply tables from QTN-569 (pages 53-55 main mill, 71-72 wire rod) ---
print("Extracting scope of supply from QTN-569 (pages 53-55, 71-72)...")
scope_569 = extract_pages(QTN_569, [53, 54, 55, 71, 72])
with open(os.path.join(SEED_DIR, "scope-of-supply-qtn-569-raw.txt"), "w") as f:
    f.write(scope_569)
print(f"  Saved scope-of-supply-qtn-569-raw.txt")

print("\nAll seed data extracted.")
