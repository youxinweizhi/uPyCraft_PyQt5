
from microbit import display
from microbit import sleep
from microbit import Image

Image1=Image("99999:80000:77777:00006:55555")#show the number "5",the value of light 0-9
mixed_list = [Image1, Image.HAPPY]

try:
  display.show(mixed_list, loop=True, delay=1000)
except:
  display.clear()