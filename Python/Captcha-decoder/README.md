
# Captcha-decoder

## Description :

This script can decode weak captchas. It is intended to deter you fom using such weak systems by showing you that is possible to hijack them in a short period of time by using some basic programming knowledges. **I did this for learning purposes and encourage you to do the same!**

## Prerequisites before running the script :

 1. Install python 3
 2. Install tesseract (https://github.com/tesseract-ocr/tesseract/wiki/Downloads)
	 - if you are in windows make sur that the path is correct in the captcha.py file ***pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'***
 3. Install PIL and pytesseract :

	```shell
	 sudo apt-get -y install python3-pip
	 pip3 install  Pillow
 	 pip3 install pytesseract 
	```

## How to use it :

Just change the variable ***CAPTCHA_NAME*** by your image name.

If the output is not correct then change the variable ***ZOOM*** or ***CONTRAST***
If you want to test it before, then I put in the images directory differents images with different level of difficulty :

**level 1 :**

![level1](images/level1.png)

**level 2 :**

![level2](images/level2.png)

**level 3 :**

![level3](images/level3.png)

**level 4 :**

![level4](images/level4.png)

**level 5 :**

![level5](images/level5.png)
