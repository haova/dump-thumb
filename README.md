# Dump Thumb

## Install

Install `avrdude`, `flashrom`

```bash
sudo apt-get install avrdude
sudo apt-get install avrdude
```

Clone repository:

```bash
git clone https://github.com/haova/dump-thumb.git
```

Setup code:

```bash
cd dump-thumb
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

```bash
python -m venv venv
python src/main.py
```

## Exception handle

If something was wrong with Rust, run this command before install packages.

```bash
export CRYPTOGRAPHY_DONT_BUILD_RUST=1
```
