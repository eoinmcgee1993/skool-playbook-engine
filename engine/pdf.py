from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT

def write_pdf(markdown_text, path):
    styles=getSampleStyleSheet()
    styles["Title"].alignment=TA_LEFT
    doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=45,bottomMargin=45)
    story=[]
    for line in markdown_text.splitlines():
        if not line.strip():
            story.append(Spacer(1,8))
        elif line.startswith("# "):
            story.append(Paragraph(line[2:],styles["Title"]))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:],styles["Heading2"]))
        else:
            story.append(Paragraph(line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"),styles["BodyText"]))
    doc.build(story)
