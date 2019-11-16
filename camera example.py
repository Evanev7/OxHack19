from SimpleCV import Image, Camera

camera = Camera()
img = camera.getImage()
img.save("filename.jpg")
