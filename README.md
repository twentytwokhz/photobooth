# photobooth

<b>Raspberry Pi Photobooth</b>

This is a Raspberry Pi project written in Python.

It is based on [gphoto2](https://github.com/gphoto/gphoto2), [ImageMagick](https://github.com/ImageMagick/ImageMagick) and [Facebook Python SDK](https://github.com/mobolic/facebook-sdk)

<b>Requirements:</b>

1. A Raspberry Pi 2 Model B or newer
2. A MicroUSB cable with a power adapter that can provide minimum 1000mA
3. Wifi USB Stick LAN connection (optional)
4. Wired LAN connection
5. HDMI Display (optional)
6. USB Keyboard
7. Compatible DSLR/camera connected through USB

This project is intended to be used as a mean of taking photos (at a specified interval and for a specified time period) from a connected camera and uploading these images to a Facebook page, Facebook profile or on Google Drive.

Optionally the code will generate animated GIFs.

<b>Example usage:</b>

<code>python photobooth.py 5 60</code>

Takes a photo every 5 seconds for a period of 60 seconds. After that it will create a gif from the photos named result.gif
