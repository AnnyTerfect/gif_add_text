# gif_add_text
To add text to a gif

<p>
app = gif_add_text()<br>
#建立gif_add_text类实例<br>
app.choose_font('微软雅黑.ttf', 20)<br>
#设置字体和字体大小<br>
app.load_gif('temp.gif')<br>
#载入gif文件<br>
app.add_text('你好', (0, 0), (255, 0, 0))<br>
#添加文字<br>
app.save('new.gif')<br>
#保存为新文件<br>
</p>
