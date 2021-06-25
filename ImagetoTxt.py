#pip install pywhatkit
from pywhatkit import image_to_ascii_art
input_img='python.png'
output_file_txt='ascii_python.txt'
print(image_to_ascii_art(imgpath=input_img, output_file=output_file_txt))