from rembg import remove
from PIL import Image

input_path = 'Foto.jpg'
output_path = 'FotoSinFondo.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
