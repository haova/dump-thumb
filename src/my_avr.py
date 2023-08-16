import subprocess
import re
from datetime import datetime

def avr_old_test(comport):
  try:
    res = subprocess.run(f"avrdude -c arduino -P {comport} -p m328 -b 57600", shell=True, text=True, capture_output=True)
    x = re.search(r"\(probably (.*)\)", res.stderr)

    if x == None:
      return False
    return x[1]
  except subprocess.CalledProcessError:
    return False

def avr_old_dump(comport):
  device = avr_old_test(comport)
  if device == False:
    return False

  try:
    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    fullcommand = f"avrdude -c arduino -P {comport} -p {device} -b 57600 -U flash:r:outputs/{now}-arduino.bin:r"
    print("|- ...run command: " + fullcommand)
    subprocess.run(fullcommand, shell=True, check=True)
    return True
  except subprocess.CalledProcessError:
    return False

def avr_test(comport):
  try:
    res = subprocess.run(f"avrdude -c arduino -P {comport} -p m328", shell=True, text=True, capture_output=True)
    x = re.search(r"\(probably (.*)\)", res.stderr)

    if x == None:
      return False
    return x[1]
  except subprocess.CalledProcessError:
    return False

def avr_dump(comport):
  device = avr_test(comport)
  if device == False:
    return False

  try:
    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    fullcommand = f"avrdude -c arduino -P {comport} -p {device} -U flash:r:outputs/{now}-arduino.bin:r"
    print("|- ...run command: " + fullcommand)
    subprocess.run(fullcommand, shell=True, check=True)
    return True
  except subprocess.CalledProcessError:
    return False
