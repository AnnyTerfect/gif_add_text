# -*- coding: utf-8 -*-
import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import sys
from fire import Fire

class gif_add_text:
	def __init__(self, filename,
					   fontpath,
					   fontsize):
		gif = imageio.read(filename)

		seq = []
		seq_len = gif.get_length()
		for index in range(seq_len):
			seq.append(gif.get_data(index))
		self.seq = seq
		self.duration = gif.get_meta_data()['duration']
		self.font = ImageFont.truetype(fontpath, fontsize)

	def resize(self, newsize):
		if newsize:
			newsize = newsize[1], newsize[0]
			for index, img in enumerate(self.seq):
				h, w, c = img.shape
				new_img = 255 + np.zeros(newsize + (c,), dtype='uint8')
				new_img[: h, :w, :c] = img
				self.seq[index] = new_img

	def add_text(self, text, pos, color, time_start=0):
		seq_len = len(self.seq)
		for i in range(time_start, seq_len):
			img = Image.fromarray(self.seq[i])
			draw = ImageDraw.Draw(img)
			draw.text(pos, text, font=self.font, fill=color)
			#写入文字
			self.seq[i] = np.asarray(img)
			#转成np数组

	def save(self, filename):
		imageio.mimsave(filename, self.seq, duration=self.duration / 1000.0)

def main(
	gif='sorry.gif',
	new_gif='new_sorry.gif',
	text='哈哈',
	font='微软雅黑.ttf',
	newsize=None,
	font_size=40,
	pos=(90, 20),
	color=(255, 255, 255),
	time_start=0
):
	app = gif_add_text(gif, font, font_size)
	app.resize(newsize)
	app.add_text(text, pos, color, time_start)
	app.save(new_gif)

if __name__ == '__main__':
	Fire(main)