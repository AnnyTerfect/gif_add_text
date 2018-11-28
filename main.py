# -*- coding: utf-8 -*-
import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np

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
	app = gif_add_text()
	app.choose_font('微软雅黑.ttf', 20)
	app.load_gif('temp.gif')
	app.add_text('你好', (0, 0), (255, 0, 0))
	app.save('new.gif')