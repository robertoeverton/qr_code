# importou a biblioteca que gera qrcode => pip install qrcode
import qrcode

# cria uma funcao que recebe o nome a ser gerado e gera um arquivo png com o mesmo nome 
def Get_QR(name):
    img = qrcode.make(name)
    type(img)  # qrcode.image.pil.PilImage
    img.save(f"./files/{name}.png")

  
# gera uma lista para guardar os dados
Empilhadeiras = [
"EMP_01",
"EMP_02",
"EMP_03",
"EMP_04",
"EMP_05",
"EMP_06",
"EMP_07",
"EMP_08",
"EMP_09",
"EMP_10",
"EMP_11",
"EMP_12",
"EMP_13",
"EMP_14",
"EMP_15",
"EMP_16",
"EMP_17",
"EMP_18",
"EMP_19",
"EMP_20",
"EMP_21",
"EMP_22",
"EMP_23",
"EMP_24",
"EMP_25",
]

for empilhadeira in Empilhadeiras:
   Get_QR(empilhadeira)