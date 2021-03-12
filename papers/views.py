from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
import random

from papers.models import PaperInfo, ConferenceInfo
from userinfo.models import PaperViewHistory

import gensim
import pandas as pd
from gensim.models.doc2vec import Doc2Vec
import os, math

# 分页函数 https://blog.csdn.net/weixin_44951273/article/details/100889972?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param


class MyPaginator(Paginator):   # 继承Paginator
    def __init__(self, object_list, per_page, show_count=2, orphans=0, allow_empty_first_page=True):  # show_count代表要展示的当前页之前或之后的页码数，默认展示3页
        super().__init__(object_list, per_page, orphans, allow_empty_first_page)  # 继承父类的属性和方法
        self.show_count = show_count
        self.has_previous_more = True  # 定义show_count之前是否还有更多页码
        self.has_next_more = True   # 定义show_count之后是否还有更多页码
    #  覆写page方法

    def page(self, number):
        self.number = int(number)
        #  判断当前页之前是否还有show_count显示的页码数
        if self.number <= self.show_count + 2:
            self.has_previous_more = False
            self.previous_range = range(1, self.number)
        else:
            self.previous_range = range(self.number - self.show_count, self.number)
        #  判断当前页之后是否还有show_count显示的页码数
        if self.number >= self.num_pages - self.show_count - 1:
            self.has_next_more = False
            self.next_range = range(self.number + 1, self.num_pages + 1)
        else:
            self.next_range = range(self.number + 1, self.number + self.show_count + 1)
        return super().page(number)


# Create your views here.
# 论文首页，应该是论文列表加上搜索框
def index(request):
    papers_list = PaperInfo.objects.all()
    papers = []
    # 随机取五份论文，之后会修改为根据个人兴趣推荐
    if request.user.is_authenticated:
        recommend_dic = get_weights(request.user)
        recommend_result = recommend(recommend_dic, 10)
        for element in recommend_result:
            papers.append(papers_list[int(element[0])])
    else:
        papers = random.sample(list(papers_list), 10)
    context = {"papers": papers}
    return render(request, 'papers/index.html', context)

# 论文详情页


def detail(request, paper_id):
    paper = get_object_or_404(PaperInfo, pk=paper_id)
    if request.user.is_authenticated:
        # 添加论文浏览记录
        paperView = PaperViewHistory.objects.filter(user=request.user, paper=paper)
        if paperView.count():
            first_view = paperView.first()
            first_view.view_time = timezone.now()
            first_view.already_deleted = False
            first_view.view_times += 1
            first_view.save()
        else:
            PaperViewHistory.objects.create(user=request.user, paper=paper)

    return render(request, 'papers/detail.html', {'paper': paper})
    # return HttpResponse("The paper id is " + paper_id)

# 搜索页


def search(request, searchword, pindex):
    q = request.GET.get('q')
    error_msg = ''
    if(searchword and q == None):
        q = searchword
    searchword = q
    papers_list = PaperInfo.objects.all()
    paginator = MyPaginator(papers_list, 10)
    int(pindex)
    page = paginator.page(pindex)
    context = {"page": page, "paginator": paginator, "searchword": searchword}
    if not q:
        error_msg = "请输入关键词"
        context['error_msg'] = error_msg
        return render(request, 'papers/result.html', context)
    papers_list = PaperInfo.objects.filter(Q(paper_title__icontains=q) | Q(abstract__icontains=q))
    # papers_list = PaperInfo.objects.filter(Q(paper_title__icontains=q) | Q(abstract__icontains=q)) # 这是在摘要中查询
    paginator = MyPaginator(papers_list, 10)
    page = paginator.page(pindex)
    context = {"page": page, "paginator": paginator, "error_msg": error_msg,  "searchword": searchword}
    return render(request, 'papers/result.html', context)



def recommend(weights, nums): # weights 是序号与权值的字典, nums表示最终列表的元素数量, 返回列表的第一个元素是序号, 第二个元素是权重
    model = Doc2Vec.load('./papers/static/doc2vec_recommendation/doc2vec_model.model')
    papers_list = PaperInfo.objects.all()
    recommend_dic = {}
    for key in weights:
        inferred_vector_dm = model.infer_vector(papers_list[key].abstract.split(','))
        sims = model.docvecs.most_similar([inferred_vector_dm], topn=nums+1)
        for tsim in sims:
            if tsim[0] not in recommend_dic:
                recommend_dic[tsim[0]] = 0
            recommend_dic[tsim[0]] = recommend_dic[tsim[0]] + tsim[1]*weights[key]
    recommend_list = sorted(recommend_dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    for pap in recommend_list:
        if pap[0] in weights.keys(): #bug待修
            print(pap[0])
            recommend_list.remove(pap)
    return recommend_list[0:nums]

def get_weights(user):
    print(user)
    viewlist = PaperViewHistory.objects.filter(user=user, already_deleted=False).order_by("-view_times")
    viewdict = {}
    for view_record in viewlist:
        viewdict[view_record.paper.pk-1] = 1 + math.log(view_record.view_times, 10)
    return viewdict