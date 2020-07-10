# raspberrypi-sound-sensor

## Setup

### Parts used:
* Pi - Raspberry Pi 3B v1.2
* OS - 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64 GNU/Linux - Debain 10 (buster)
* Sound sensor - LK sensor - http://www.linkerkit.de/index.php?title=LK-Ger%C3%A4uscheSen

### Connections

1. SIG -> GPIO9 (pin21) - SPI0_MISO
2. VCC -> 5V (pin2) - Power
3. GND -> Ground (pin14)

### Log sound

1. Start the script on the Pi
```
pi@raspberrypi:~/raspberrypi-sound-sensor $ ./sound_sense.py 
('max is: ', 768)
('max is: ', 864)
('max is: ', 768)
('max is: ', 512)
('max is: ', 992)
('max is: ', 658)
('max is: ', 896)
('max is: ', 768)
('max is: ', 648)
...
```
