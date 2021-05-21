#!/usr/bin/env python3
'''This Example opens an Image and transform the image into grayscale, halftone, dithering, and primary colors.
You need PILLOW (Python Imaging Library fork) and Python 3.5
    -Isai B. Cicourel'''

# Imported PIL Library 
from PIL import Image

# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Print Image Hex for https://studio.code.org/s/pixelation/lessons/3/levels/1
def print_image_hex(image):
  # Get size
  width, height = image.size
  # Print header 
  print(format(width, "02X"), format(height, "02X"), format(24, "02X")) 
  for j in range(height):
    for i in range(width):
      # Get Pixel
      pixel = image.getpixel((i, j))
      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]
      print(format(pixel[0],"02X"), format(pixel[1], "02X"), format(pixel[2], "02X") , end="", sep="")
      print("") # uncomment to print by pixel
    #print("") # uncomment to print by line

# Print Image Hex for https://salmanarif.bitbucket.io/visual/
def print_image_dcd(image):
  # Get size
  width, height = image.size
  # Print header 
  print("image\tdcd\t", end="")
  for j in range(height):
    for i in range(width):
      # Get Pixel
      pixel = image.getpixel((i, j))
      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]
      print("0x", format(pixel[0],"02X"), format(pixel[1], "02X"), format(pixel[2], "02X"), end=", ", sep="")
  print("")

# Print Image Hex for https://salmanarif.bitbucket.io/visual/
def print_image_dcb(image):
  # Get size
  width, height = image.size
  # Print header 
  print("image\tdcd\t", end="")
  for j in range(height):
    for i in range(width):
      # Get Pixel
      pixel = image.getpixel((i, j))
      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]
      print("0x", format(pixel[2],"02X"),", 0x",  format(pixel[1], "02X"),", 0x", format(pixel[0], "02X"), end=", ", sep="")
  print("") 
  
# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Create a Grayscale version of the image
def convert_grayscale(image):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to grayscale
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = image.getpixel((i, j))

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      gray = (red+(green<<1)+blue)>>2

      # Set Pixel in new image
      pixels[i, j] = (int(gray), int(gray), int(gray))

  # Return new image
  return new

# Create a Grayscale version of the image
def convert_bw(image,threshold):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to grayscale
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = image.getpixel((i, j))

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      gray = (red+(green<<1)+blue)>>2

      # Set pixel HIGH or LOW
      if gray > threshold:
        gray = 255
      else:
        gray = 000

      # Set Pixel in new image
      pixels[i, j] = (int(gray), int(gray), int(gray))

  # Return new image
  return new

# Main
if __name__ == "__main__":
  # Load Image (JPEG/JPG needs libjpeg to load)
  original = open_image('LD30x20.png')
  width, height = original.size
  # DCD for visUAL - color
  #print_image_dcd(original)
  #print("buffer\tfill\t", width*height*4)
  # DCD for visUAL - grayscale
  new = convert_grayscale(original)
  #print_image_hex(new)
  # DCD for visUAL - black and white
  #new = convert_bw(original,87)
  #print_image_dcd(new)
  # DCU for visUAL - grayscale desalinhado
  #print_image_dcb(original)
  print_image_dcb(new)