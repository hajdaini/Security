# Description :
This script allows to hide / display a message in an image, it modifies the LSB (Least Significant Bit) of the red color of each pixel

# Prerequisites

```
pip3 install Pillow
pip3 install argparse
```

# How to use it :

To hide message in image :
```
python stegno.py -e -i "path/montagne.jpg" -m "hidden image" -o lol.png
```

To display the hidden message :
```
python stegno.py -d -i hidden_img.png
```

## Proof
<img src="img/proove.jpg" width=400>
