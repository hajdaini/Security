# Description :
This script allows you to hide / display a message in an image, it modifies the LSB (Least Significant Bit) of the red color of each pixel

# Prerequisites :

```
pip3 install Pillow
pip3 install argparse
```

# How to use it :

**To hide message in image :**
```
python stegno.py -e -i "path/montagne.jpg" -m "hidden image" -o lol.png
```

**To display the hidden message :**
```
python stegno.py -d -i hidden_img.png
```

**help :**
```
python stegno.py -h
```

## Proof :

### Before encoding the image :
<img src="montagne.jpg">

### After encoding the image :
<img src="img/hidden_img.png">

**Running the script**
<br>
<br>
<img src="img/proove.jpg">
