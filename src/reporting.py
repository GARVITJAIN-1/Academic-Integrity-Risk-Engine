from fpdf import FPDF

def generate_pdf_report(student_row):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Academic Integrity Risk Report", ln=True)
    pdf.cell(200, 10, txt=f"Student ID: {student_row['student_id']}", ln=True)
    pdf.cell(200, 10, txt=f"Risk Score: {student_row['risk_score']}", ln=True)
    pdf.cell(200, 10, txt=f"Confidence: {student_row['confidence']}%", ln=True)

    pdf.multi_cell(0, 10, txt="Reasons:\n" + "\n".join(student_row["risk_reasons"]))

    pdf.output(f"reports/student_{student_row['student_id']}.pdf")
