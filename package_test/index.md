# System Information


## Embedded board
Raspberry Pi 4 Model B
8GB RAM

## OS
Raspberry OS 64-bit
    '''bash
    $ lsb_release -a
    No LSB modules are available.
    Distributor ID:	Debian
    Description:	Debian GNU/Linux 12 (bookworm)
    Release:	12
    Codename:	bookworm
    '''

    '''bash
    $ uname -a
    Linux raspberrypi 6.6.20+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.6.20-1+rpt1 (2024-03-07) aarch64 GNU/Linux
    '''

## Network Infra
HostName    : raspberrypi
UID         : chana
IP          : 203.250.35.75
Port        : 22

## python version
pyhton3.11.2

Tested in Python version 3.9.0, but an error occurred in which the camera module could not be loaded.
so proceeded with 3.11.2, which is the default python version of Raspberry Pi OS.
