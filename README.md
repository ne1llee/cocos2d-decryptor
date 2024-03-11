# What is it?

Just frida script which lets you to obtain source code of Cocos2D game from Android device.

# How to run?

1. Run frida server on your Android device.
2. Edit `.py` and `.js` files regarding to comments on top.
3. Run `.py` script.
4. Wait until game fully loads to obtain ALL sources (may take some time with running decryptor).

# forward

adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043