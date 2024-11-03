from fpdf import FPDF

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font
pdf.set_font("Arial", "B", 12)

# Title
pdf.cell(0, 10, "USG Grant Budget Proposal | Laksh Dhir | SXSW 2025", 0, 1, "C")
pdf.ln(10)

# Program Expenses
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "PROGRAM EXPENSES", 0, 1)
pdf.set_font("Arial", "", 12)

# Program Fees
pdf.cell(60, 10, "Program Fees", 0)
pdf.cell(40, 10, "$0", 0)
pdf.cell(40, 10, "$800", 0)
pdf.cell(40, 10, "$800", 0)
pdf.cell(0, 10, "Student registration fees for SXSW 2025.", 0, 1)

# Personal Expenses
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "PERSONAL EXPENSES", 0, 1)
pdf.set_font("Arial", "", 12)

# Flights
pdf.cell(60, 10, "Flights", 0)
pdf.cell(40, 10, "$0", 0)
pdf.cell(40, 10, "$410", 0)
pdf.cell(40, 10, "$410", 0)
pdf.cell(0, 10, "Roundtrip flights to and from Austin, TX.", 0, 1)

# Living Arrangements
pdf.cell(60, 10, "Living Arrangements", 0)
pdf.cell(40, 10, "$1200", 0)
pdf.cell(40, 10, "$664", 0)
pdf.cell(40, 10, "$1864", 0)
pdf.cell(0, 10, "Cheapest Lodging next to the convention center.", 0, 1)

# Food
pdf.cell(60, 10, "Food", 0)
pdf.cell(40, 10, "$0", 0)
pdf.cell(40, 10, "$150", 0)
pdf.cell(40, 10, "$150", 0)
pdf.cell(0, 10, "$30 food per day of stay.", 0, 1)

# Business Cards
pdf.cell(60, 10, "Business Cards", 0)
pdf.cell(40, 10, "$0", 0)
pdf.cell(40, 10, "$30", 0)
pdf.cell(40, 10, "$30", 0)
pdf.cell(
    0,
    10,
    "Business cards to invite possible research and business collaboration to serve children in the Austin Area.",
    0,
    1,
)

# USG Funds Total
pdf.cell(0, 10, "", 0, 1)
pdf.cell(0, 10, "USG Funds Total: $800", 0, 1)

# Personal Funds Total
pdf.cell(0, 10, "Personal Funds Total: $2,244", 0, 1)

# Total Cost
pdf.cell(0, 10, "Total Cost: $3,044", 0, 1)

# Save the PDF to a file
pdf_output_path = "/usr/local/bin/python3 /Users/anuragkej/PythonTutoring/hi.pdf"
pdf.output(pdf_output_path)

pdf_output_path
