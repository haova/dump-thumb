import subprocess
from datetime import datetime

def flashrom_dump():
  try:
    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    fullcommand = f"sudo flashrom --programmer ch341a_spi -r outputs/{now}-ch341a.bin"
    print("|- ...run command: " + fullcommand)
    subprocess.run(fullcommand, shell=True, check=True)
    return True
  except subprocess.CalledProcessError:
    return False