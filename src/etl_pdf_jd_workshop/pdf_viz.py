import os
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# Redrex
# file_name = 'Redrex - Fatura (1)'
# path = os.path.abspath(f"src/etl_pdf_jd_workshop/files/pdf/redrex/{file_name}.pdf")

# Jornada
file_name = 'corretora_jornada_de_dados (1)'
path = os.path.abspath(f"src/etl_pdf_jd_workshop/files/pdf/jornada/{file_name}.pdf")

tables = camelot.read_pdf(
    path,
    pages='1-end',
    flavor='stream',
    table_areas=['65, 558, 500, 298'],
    columns=["65, 107, 156, 212, 280, 336, 383, 450"],
    strip_text=" .\n"
)

print(tables[0].parsing_report)

# camelot.plot(tables[0], kind="contour")

# plt.show()

print(tables[0].df)

print("Pause")