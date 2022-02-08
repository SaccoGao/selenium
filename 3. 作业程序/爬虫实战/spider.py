from urllib import request  # 用于获取Html网页
import gzip
import re

class Spider():
    url = 'https://www.douyu.com/g_LOL'
    root_pattern = '<div class="DyListCover-info">([\s\S]*?)</div>'
    Name_pattern = '<div class="DyListCover-userName is-template">([\s\S]*?)$'
    Number_pattern = '</use></svg>([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(self.url)
        htmls = r.read()
        htmls = gzip.decompress(htmls).decode('utf-8') # 使用gzip解压文件
        # print(htmls)
        return htmls
        '''
        <div class="DyListCover-info" >包含主播姓名与直播人数</div>
        <span class="DyListCover-hot is-template">主播人气</span>
        <div class="DyListCover-userName is-template">主播姓名</div>
        '''

    def __analysis(self, htmls):
        root_html = re.findall(self.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(self.Name_pattern, html)
            number = re.findall(self.Number_pattern, html)
            anchor = {'name':name, 'number':number}
            if len(anchor['name']) == 0:
                continue
            else:
                anchors.append(anchor)
        return anchors

    def __sort(self, anchors):
        anchors = sorted(anchors, key = self.__sort_seed, reverse = True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('(\d*\.?\d*)',anchor['number'][0])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for anchor in anchors:
            anchor = str(anchor)
            print(anchor)

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = self.__sort(anchors)
        self.__show(anchors)

spider = Spider()
spider.go()