
from lxml import etree

html = '''
    <!DOCTYPE html>
	<html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <div>
                <ul>
                    <li class="class1"><a href="class1.html">1</a></li>
                    <li class="class2"><a href="class2.html">2</a></li>
                    <li class="class3"><a href="class3.html">3</a></li>
                    <li class="class4"><a href="class4.html">4</a></li>
                    <li class="class5"><a href="class5.html">5</a></li>
                    <li>
                        <ul>
                            <li class="class1"><a href="class6.html">6</a></li>
                            <li class="class7"><a href="class7.html">7</a></li>
                            <li class="class8"><a href="class8.html">8</a></li>
                        </ul>
                    </li>
                </ul>
            <div>
        </body>
	</html>
'''

html = etree.HTML(html)

a = html.xpath('/html')
# print(a)

a1 = html.xpath('//ul')

# /html/body/div[1]/div[4]/div[1]/div[1]/ul/li[1]/a
# //*[@id="screening"]/div[2]/ul/li[6]/ul/li[1]/a/img
# print(a1)
# for i in a1:
    # print(i)
    # print(i.xpath('.'))
    # print(i.xpath('..'))

a2 = html.xpath('//ul/li[@class="class2"]')

a3 = html.xpath('//ul/li/a/text()')
print(a3)

a4 = html.xpath('//ul/li/a/@href')
print(a4)




