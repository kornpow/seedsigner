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
pip install -r requirements-emulator.txt
```

## Build the executable
```
cd src
pyinstaller --onefile  --paths="/home/skorn/venvs/seedsigner_gui-2/lib/python3.8/site-packages/cv2/cv2.abi3.so" main.py
```

```
docker run -v "$(pwd):/src/" ubuntu:18.04 sleep 1000
```

In docker container
```
apt update && apt install -y python3 python3-dev python3-pip git software-properties-common python3.7-tk
 pip3 install -U pip setuptools wheel

 add-apt-repository ppa:deadsnakes/ppa
 apt-get update
 apt install python3.7 python3.7-dev

 pyinstaller main.spec
```

## Run executable
```
cd src/dist/main
NOTAPI=true ./main
```

## AppImage
https://github.com/AppImage/AppImageKit/wiki/Bundling-Python-apps
https://github.com/niess/python-appimage/blob/master/docs/src/apps.md

TODO:
Download Base App Image
```bash
    wget https://github.com/niess/python-appimage/releases/download/python3.8/python3.8.13-cp38-cp38-manylinux1_x86_64.AppImage
    chmod +x python3.8.13-cp38-cp38-manylinux1_x86_64.AppImage
    ln -s python3.8.13-cp38-cp38-manylinux1_x86_64.AppImage app38
```
Download all deps locally
 - https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from
 - pip install git+file:///path/to/your/git/repo
Successful install in appimage

## Run the emulator
```
cd seedsigner/src
NOTAPI=true python3 main.py
```