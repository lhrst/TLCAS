from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import PaperInfo, ConferenceInfo

#分页函数 https://blog.csdn.net/weixin_44951273/article/details/100889972?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param
class MyPaginator(Paginator): # 继承Paginator
    def __init__(self,object_list, per_page, show_count=3, orphans=0, allow_empty_first_page=True): # show_count代表要展示的当前页之前或之后的页码数，默认展示3页
        super().__init__(object_list, per_page, orphans, allow_empty_first_page) #继承父类的属性和方法
        self.show_count = show_count
        self.has_previous_more = True #定义show_count之前是否还有更多页码
        self.has_next_more = True #定义show_count之后是否还有更多页码
    
    #覆写page方法
    def page(self, number):
        self.number = int(number)
        print("number is " + number)
        #判断当前页之前是否还有show_count显示的页码数
        if self.number <= self.show_count + 2:
            self.has_previous_more = False
            self.previous_range = range(1,self.number)
        else:
            print("has_previous_more is Ture")
            self.previous_range = range(self.number - self.show_count, self.number)
        #判断当前页之后是否还有show_count显示的页码数
        if self.number >= self.num_pages - self.show_count - 1:
            self.has_next_more = False
            self.next_range = range(self.number + 1, self.num_pages + 1)
        else:
            self.next_range = range(self.number + 1, self.number + self.show_count + 1)
        return super().page(number)


# Create your views here.
# 论文首页，应该是论文列表加上搜索框
def index(request, pindex):
    papers_list = PaperInfo.objects.all()
    paginator = MyPaginator(papers_list, 10)
    if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        pindex = 1
    else:
        int(pindex)
    page = paginator.page(pindex)
    print(page.number)
    context = {"page": page,"paginator":paginator}
    return render(request, 'papers/index.html', context)

# 论文详情页
def detail(request, paper_id):
    paper = get_object_or_404(PaperInfo, pk=paper_id)
    return render(request, 'papers/detail.html', {'paper': paper})
    # return HttpResponse("The paper id is " + paper_id)

