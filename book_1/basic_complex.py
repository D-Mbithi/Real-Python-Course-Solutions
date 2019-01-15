from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Table

xmargin = 3.2 * inch
ymargin = 6 * inch

c = canvas.Canvas('tps_report.pdf', pagesize=letter)
c.setFont('Helvetica', 12)

data = [['#1', '#2', '#3', '#4', '#5'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34'],
        ['40', '41', '42', '43', '44'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34'],
        ['40', '41', '42', '43', '44'],
        ['50', '51', '52', '53', '54']]

t = Table(data)
t.setStyle([('TEXTCOLOR', (0,0), (4,0), colors.red)])
t.wrapOn(c, xmargin, ymargin)
t.drawOn(c, xmargin, ymargin)
c.save()
