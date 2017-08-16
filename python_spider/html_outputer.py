# _*_ coding:utf-8 _*_  
"""
@file: html_outputer.py 
@time: 2017/08/16 
"""


class HtmlOutputer(object):
    # 初始化
    def __init__(self):
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 输出数据
    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")

        fout.write("<head>")
        fout.write("<meta charset= 'UTF-8'>")
        fout.write("</head>")

        fout.write("<body>")
        fout.write("<table>")

        # ASCII
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")

        fout.close()
