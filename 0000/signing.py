from PIL import Image, ImageFont, ImageDraw, ImageFilter

text = "Q. C. Jiang"
img = Image.open("CollegeMapfullsize.jpg")
w_img, h_img=img.size

#filtering
#for i in range(1,10):
#    img = img.filter(ImageFilter.SMOOTH)
#    img.save(str(i)+'.jpg')

#watermark the image
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("msyh.ttf", w_img/40)
w_font, h_font = draw.textsize(text, font)
draw.text((w_img-w_font, 0), text, fill="red", font=font)

#save to 'manipulated.jpg'
img.save('manipulated.jpg')
