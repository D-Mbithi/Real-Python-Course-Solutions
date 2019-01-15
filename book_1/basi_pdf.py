from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf")
c.drawString(250, 500, "hello world")
c.save()
