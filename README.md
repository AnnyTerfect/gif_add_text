# gif_add_text
To add text to a gif

<p>
app = gif_add_text()<br>
app.choose_font('微软雅黑.ttf', 20)<br>
app.load_gif('temp.gif')<br>
app.add_text('你好', (0, 0), (255, 0, 0))<br>
app.save('new.gif')<br>
</p>
