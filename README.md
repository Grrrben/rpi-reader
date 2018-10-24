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
A [ ] [ ] [ ]
B [ ] [ ] [ ]
C [ ] [ ] [ ]
D [ ] [ ] [ ]
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