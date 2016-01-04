__author__ = 'Marko Arsenovic'

from PIL import Image
import cv2
import numpy as np

#FIRST ROW
images = map(Image.open, ['jp_0001.jpg', 'jp_0003.jpg', 'jp_0004.jpg', 'jp_0005.jpg', 'jp_0007.jpg']) # \

widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test1.jpg')



#SECOND ROW

images = map(Image.open,['jp_0008.jpg', 'jp_0009.jpg', 'jp_0011.jpg', 'jp_0013.jpg', 'jp_0015.jpg'])

widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test2.jpg')

#MERGE TWO ROWS

img1 = cv2.imread('test1.jpg')
img2 = cv2.imread('test2.jpg')
vis = np.concatenate((img1, img2), axis=0)
cv2.imwrite('out.jpg', vis)