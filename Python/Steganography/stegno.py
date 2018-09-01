"""
@Author : AJDAINI Hatim
@GitHub : https://github.com/Hajdaini
"""

from PIL import Image
import argparse, time
from argparse import RawTextHelpFormatter


def encode_image(msg, src_img, dest_img):
    msg = ascii_to_binary(msg)
    listed_msg = list(msg[2:])  # remove the '0b' from the beginning of the string

    try:
        encoded_image = Image.open(src_img)
        print("the image" + src_img + " exist we will now hide the text in the image ...\n")
    except Exception as e:
        print(e)
        exit(1)

    red_channel = encoded_image.split()[0]  # get only red values
    green_channel = encoded_image.split()[1]  # get only green values
    blue_channel = encoded_image.split()[2]  # get only blue values

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    total_size_image = x_size * y_size  # total number of pixels
    total_size_text = len(ascii_to_binary(msg[2:]))  # number of bits in the message

    if total_size_text > total_size_image:
        print("Size of the text is bigger than the size of the image, which means that end data encoded may be lost")

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    counter = 0
    for i in range(x_size):
        for j in range(y_size):
            before_last_bit = bin(red_channel.getpixel((i, j)))[:-2]
            try:
                if len(bin(red_channel.getpixel((i, j)))) <= 4:
                    res = bin(red_channel.getpixel((i, j)))[:-1] + '1' + listed_msg[
                        counter] + '1'  # For example this will transform 0b10 to 0b1X1 while X is the bit (0 or 1) message
                else:
                    res = before_last_bit + listed_msg[counter] + '1'
                pixels[i, j] = (int(res, 2), green_channel.getpixel((i, j)), blue_channel.getpixel((i, j)))
            except:
                last_bit = bin(red_channel.getpixel((i, j)))[:-1]
                pixels[i, j] = (int(last_bit + '0', 2), green_channel.getpixel((i, j)), blue_channel.getpixel((i, j)))
            counter += 1
    save_image_handle(decoded_image, dest_img)


def save_image_handle(decoded_image, dest_img):
    if 'png' not in dest_image:
        try:
            dest_image_png = "".join(dest_img.split(".")[:1]) + ".png"
            decoded_image.save(dest_image_png)
            print("Sorry I can only save png image because JPEG format compresses the image data, which means that data encoded may be lost")
            print("BUTT I will save it as png image for you :)\n")
            print("The message has been hidden successfully !")
        except Exception as e:
            print(e)
    else:
        try:
            decoded_image.save(dest_img)
            print("The message has been hidden successfully !")
        except Exception as e:
            print(e)


def decode_image(src_image):
    encoded_image = Image.open(src_image)
    red_channel = encoded_image.split()[0]  # get only red values

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    phrase = []
    test = []
    for i in range(x_size):
        for j in range(y_size):
            last_bit = bin(red_channel.getpixel((i, j)))[-1]
            if last_bit == '1':
                before_last_bit = bin(red_channel.getpixel((i, j)))[-2]
                test.append(bin(red_channel.getpixel((i, j))))
                phrase.append(before_last_bit)
    print(binary_to_ascii("0b" + "".join(phrase)))


def binary_to_ascii(bin):
    n = int(str(bin), 2)
    return (n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())


def ascii_to_binary(ascii):
    return bin(int.from_bytes(str(ascii).encode(), 'big'))


description = r"""Hide your message in an Image.

EXAMPLES :

    ENCODE :

        python stegno -e -i "C:\Users\usrname\Desktop\input.png" -m "your message" -o "name_of_your_image"
    
    DECODE :
        python stegno -d "/home/username/input.png"

-----------------------------------------------
Author : AJDAINI Hatim
Github : https://github.com/Hajdaini
-----------------------------------------------
"""

parser = argparse.ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)
parser.add_argument("-i", help="[REQUIRED] path of your source image")
parser.add_argument("-m", help="[REQUIRED] your hidden message")
parser.add_argument("-o", help="[REQUIRED] path of your destination image")
parser.add_argument("-e", help="""[OPTIONAL] encode the message""", action="store_true")
parser.add_argument("-d", help="""[OPTIONAL] decode the message""", action="store_true")

args = parser.parse_args()

src_image = args.i
message = args.m
dest_image = args.o
encode_mode = args.e
decode_mode = args.d

if encode_mode:
    time_start = time.time()
    encode_image(message, src_image, dest_image)
    print('Finish in {} s'.format(round(time.time() - time_start, 3)))
elif decode_mode:
    decode_image(src_image)
else:
    print("No decode or encode mode.\nPlease run the help option")
