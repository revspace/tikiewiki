# Praatpaal wikipedia sample randomizer

## Dependencies

```
sudo apt install -y python3-pygame python3-rpi.gpio
```

## Samples

Samples downloaden, het zijn er veeeeeeeeeel! (~ 3400). 
```
curl -s "https://nl.wikipedia.org/wiki/Wikipedia:Lijst_van_ingesproken_artikelen" | hq a attr href | grep --color=never ".ogg$" | grep --color=never upload | sed  's#^//#https://#' > wikipedias.txt
aria2c -x 10 -i wikipedias.txt
```

Benodigd:

* [hq](https://github.com/coderobe/hq)
* [aria2](https://github.com/aria2/aria2)
