# -*- coding: utf-8 -*-
import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import sys

class gif_add_text:
	def choose_font(self, fontpath, fontsize):
		self.font = ImageFont.truetype(fontpath, fontsize)
	#字体和字体大小配置

	def load_gif(self, filename):
		self.gif = imageio.read(filename)
		self.duration = self.gif.get_meta_data()['duration']
	#读取gif文件

	def add_text(self, text, pos, color):
		self.seq = []
		l = self.gif.get_length()
		for i in range(l):
			self.seq.append(self.gif.get_data(i))
			#从gif中获取位图序列

		for i in range(l):
			img = Image.fromarray(self.seq[i])
			draw = ImageDraw.Draw(img)
			draw.text(pos, unicode(text, 'utf-8'), font = self.font, fill = color)
			#写入文字
			self.seq[i] = np.asarray(img)
			#转成np数组

	def save(self, filename):
		imageio.mimsave(filename, self.seq, duration = self.duration / 1000.0)
		#保存图片

if __name__ == '__main__':
	if len(sys.argv) < 8:
		print('please input args follow the format bellow')
		print('python gif_add_text.py [fontpath] [fontsize] [gifpath] [text] [x,y] [r,g,b] [new_gif_path]')
		exit()
	font = sys.argv[1]
	fontsize = int(sys.argv[2])
	gif = sys.argv[3]
	text = sys.argv[4]
	x, y = sys.argv[5].replace('(', '').replace(')', '').split(',')
	x, y = int(x), int(y)
	r, g, b = sys.argv[6].replace('(', '').replace(')', '').split(',')
	r, g, b = int(r), int(g), int(b)
	new_gif = sys.argv[7]

	app = gif_add_text()
	app.choose_font(font, fontsize)
	app.load_gif(gif)
	app.add_text(text, (x, y), (r, g, b))
	app.save(new_gif)