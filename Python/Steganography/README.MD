# Description :

This script allows you to hide / display a message in an image, it modifies the LSB (Least Significant Bit) of the red color in each pixel

# Prerequisites :

```shell
pip3 install Pillow
pip3 install argparse
```

# How to use it :

**To hide message in image :**

```shell
python3 stegno.py -e -i "path/montagne.jpg" -m "hidden image" -o h_img.png
```

**To display the hidden message :**

```shell
python3 stegno.py -d -i h_img.png
```

**help :**

```shell
python3 stegno.py -h
```

## Proof :

### Before encoding the image :

![montagne](montagne.jpg)

### After encoding the image :

![hidden img](img/hidden_img.png)

**Running the script**

![proove](img/proove.jpg)
