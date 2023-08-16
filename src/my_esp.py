import esptool
from datetime import datetime

def esp_dump(comport):
  command = ['--baud', '460800', 'read_flash', '0', '0x200000', f'outputs/{now}-esp.bin']
  esptool.main(command)
  return True