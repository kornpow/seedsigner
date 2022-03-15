# Emulator Setup

## Boot into Tails
- Burn USB Stick and boot into Tails
- On Bootup enable Administration Password
- Connect to Internet and connect to Tor
- In terminal, continue on with tails setup

## Tails Setup
## Apt Install
```
sudo apt install python3-tk python3-venv
```
After installing packages, choose to have them saved in encrypted persistence.
Reboot, re-enter Tails, but dont enable the internet

## Clone this repo
```
git clone https://github.com/kornpow/seedsigner.git
```
or download usable binary package

## Create/Enter virtualenv
```
mkvirtualenv seedsigner-gui
```

## Pip installs
```
pip install -r requirements.txt
```



## Run the emulator
```
cd seedsigner/src
NOTAPI=true python3 main.py
```