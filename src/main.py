import time
import usb.core

from serial.tools.list_ports import comports
from constants import avrdude_old_products, avrdude_products, flashrom_products, esptool_products
from my_avr import avr_dump, avr_old_dump
from my_flashrom import flashrom_dump
from my_esp import esp_dump

def enumerate_usb_devices():
  return set([item for item in usb.core.find(find_all=True)])

def enumerate_serial_devices():
  return set([item for item in comports()] + [item for item in usb.core.find(find_all=True)])

def check_new_usb_devices(old_devices):
  devices = enumerate_usb_devices()
  added = devices.difference(old_devices)
  removed = old_devices.difference(devices)
  return [devices, added, removed]

def dump(info):
  is_dumped = False
  if info['product'] in avrdude_old_products:
    print('|- Try dumping ' + info['comport'] + ' using avrdude (Old bootloader)...')
    is_dumped = avr_old_dump(info['comport'])

  if info['product'] in avrdude_products:
    print('|- Try dumping ' + info['comport'] + ' using avrdude...')
    is_dumped = avr_dump(info['comport'])

  if info['product'] in esptool_products:
    print('|- Try dumping ' + info['comport'] + ' using esptool...')
    is_dumped = esp_dump(info['comport'])

  if info['product'] in flashrom_products:
    print('|- Try dumping using flashrom...')
    is_dumped = flashrom_dump()

  if not is_dumped:
    print('|- ... fail')

def info(port):
  print("Device:", port.device)
  print("Name:", port.name)
  print("Description:", port.description)
  print("Hardware ID:", port.hwid)
  print("Manufacturer:", port.manufacturer)
  print("Product:", port.product)
  print("Serial Number:", port.serial_number)
  print("Location:", port.location)
  print("VID:", port.vid)
  print("PID:", port.pid)
  print("Interface:", port.interface)
  print("-----------------------------")

def show_usb_info(item):
  product = item.product
  comport = None
  for port in comports():
    if port.product == product:
      comport = port.device
      break

  print('  |- Product: ' + product)
  print('  |- COM: ' + (comport if comport != None else 'None'))

  return { 'product': product, 'comport': comport }
  

old_devices = enumerate_usb_devices()
print('Listening...')

# for item in old_devices:
#   info(item)
#   # dump(item)

while True:
  new_devices, added, removed = check_new_usb_devices(old_devices)
  old_devices = new_devices

  for item in added:
    print('|- Added:')
    info = show_usb_info(item)
    dump(info)

  time.sleep(0.5)