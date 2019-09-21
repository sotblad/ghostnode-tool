# MUEnode Tool

[![Build Status Travis CI](hhttps://github.com/sotblad/muenode-tool.svg?branch=master)](https://github.com/sotblad/muenode-tool) [![Build status AppVeyor](https://ci.appveyor.com/api/projects/status/kkcf324yn6dn6woj/branch/master?svg=true)](https://ci.appveyor.com/project/sotblad/muenode-tool/branch/master)

The main purpose of the application is to give MUEnode (MUE masternode) operators the ability to send the "start MUEnode" command through an easy to use a graphical user interface if the MUEnode collateral is controlled by a hardware wallet such as Trezor or Ledger.

MUEnode Tool is based on [Dash Masternode Tool (DMT)](https://github.com/Bertrand256/dash-masternode-tool) by Bertrand256. MUenodes and Dash masternodes are very similar, so most of the [original DMT documentation](README-DMT.md) still applies to MUEnode Tool as well.

## Feature list

* Sending the "start MUEnode" command if the collateral is controlled by a hardware wallet
* Transferring MUEnode earnings safely, without touching the 500000 MUE funding transaction
* Signing messages with a hardware wallet
* Initialization/recovery of hardware wallets seeds
* Updating of hardware wallets firmware (Trezor)
* Support for MUE Testnet

## Supported hardware wallets

- Trezor (model One and T)
- Ledger Nano S

## Note on binary Linux builds

Binary Linux builds are known to be not reliable due to ABI incompatibility between different Linux distributions. You might want to build MUEnode Tool yourself if provided binary does not work for your distribution:
```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install libudev-dev libusb-1.0-0-dev libfox-1.6-dev autotools-dev autoconf automake libtool libpython3-all-dev python3-pip git
sudo pip3 install virtualenv
virtualenv -p python3 venv
. venv/bin/activate
pip install --upgrade setuptools
git clone https://github.com/sotblad/muenode-tool/
cd muenode-tool/
pip install -r requirements.txt
pyinstaller muenode-tool.spec
```

MUEnode Tool requires Python 3.6. Use [pyenv](https://github.com/pyenv/pyenv) if you distribution comes with older python version. Run following command before installing Python with pyenv:
```
export PYTHON_CONFIGURE_OPTS="--enable-shared --disable-static"
```
