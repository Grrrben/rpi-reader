# SLX Rpi reader

## Connecting a 12 key keypad

_This information is based on the Storm 720 TFX 12 key keypad. However, other keypad's should work in a similar way_

Contact connections, as viewed from the rear of the keypad:
```
[8 7 6 5 4 3 2 1]
```

Row/col key locations:

```
   1   2   3
A [1] [2] [3]
B [4] [5] [6]
C [7] [8] [9]
D [*] [0] [#]
```

Detailed wiring setup to connect the keypad to the Raspberry Pi:

| Connection Pin| Row/Col       | RPI pin |
| ------------- | -------------:| -------:|
| 1             | A             | BCM 4   |
| 2             | B             | BCM 14  |
| 3             | 1             | BCM 18  |
| 4             | 2             | BCM 27  |
| 5             | 3             | BCM 22  |
| 6             | -             | -       |
| 7             | D             | BCM 17  |
| 8             | C             | BCM 15  |

## Connectiong a RFID-RC522 chip reader

Connect the RC522 module to the RPI using the following wiring schema:

| Board pin name | Board pin | Physical RPi pin | RPi pin name |
|----------------|-----------|------------------|--------------|
| SDA            | 1         | 24               | GPIO8, CE0   |
| SCK            | 2         | 23               | GPIO11, SCKL |
| MOSI           | 3         | 19               | GPIO10, MOSI |
| MISO           | 4         | 21               | GPIO9, MISO  |
| IRQ            | 5         | 12               | GPIO18       |
| GND            | 6         | 6, 9, 20, 25     | Ground       |
| RST            | 7         | 15               | GPIO22       |
| 3.3V           | 8         | 1,17             | 3V3          |

More information in the [pi-rc522](https://github.com/ondryaso/pi-rc522/blob/master/README.md) repository.