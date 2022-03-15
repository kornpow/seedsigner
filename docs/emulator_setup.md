# Emulator Setup

## Boot into Tails
Burn USB Stick and boot into Tails

## Clone this repo
```
git clone https://github.com/kornpow/seedsigner.git
```

## Create/Enter virtualenv
```
mkvirtualenv seedsigner-gui
```

## Pip installs
```
pip install -r requirements.txt
```

## Install Tkinter
```
sudo apt install python3-tk
```

## Run the emulator
```
cd seedsigner/src
NOTAPI=true python3 main.py
```