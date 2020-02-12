# Battery alarm

## What?

This script will start sending notifications if battery level goes under `THRESHOLD` (20%) and 
it will continue doing so until you plugin the laptop into the electricity.

## Why?

I use i3wm, so notifications like this are not automatically done.

## Requirements

```
apt install acpi python3
```

## Installation

Rename user with your own, rename uid 1000 if needed with your own.

Install to systemd and run

```
sudo cp battery-alarm.* /etc/systemd/system
sudo systemctl enable battery-alarm.service
sudo systemctl enable battery-alarm.timer
sudo systemctl start battery-alarm.service
```
