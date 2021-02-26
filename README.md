# TLCAS
top_level_conference_analysis_system
这是一个AI领域七个顶级会议(CCF-A)的论文分析系统，我们希望通过这个系统，能找到该领域的学术研究趋势，并帮助研究者更敏锐地发现新的学术热点。

## Tasklist
- [x] 获取各顶会的相关资料。
- [x] 下载各会议的从2013-2019年论文文件。
- [x] 获取各会议论文的标题，摘要，作者并制作成数据集。
- [x] 开始制作网站，使用django作为后端开发框架
  - [x] 建立models
  - [x] 将数据集批量导入models中
- [x] 首页，搜索页，详情页
- [x] 用户资料页
- [ ] 用户收藏论文，最近观看论文
- [ ] 用户论文推荐系统

## BUILD
>由于本地配置的python3环境不同，如果以下命令执行失败，可以尝试将`python3`替换为`python`，`pip3`替换为`pip`重试，
1. `git pull origin master`
2. `pip3 install -r requirements` 或 `python3 -m pip install -r requirements`
3. `python3 manage.py collectstatic`
4. `python3 manage.py migrate`
5. `python3 manage.py runserver`

## UPDATE
### 2020/10/20

1. 所有的`base.html/nav.html/footer.html`以userinfo/templates/下的为准	-hx

2. 修复部分papers下的bug   -hx

3. 提供站内通知功能

   ```python
   from userinfo.inbox import views as inbox_views
   
   ### 在合适的地方调用即可发送站内通知
   ### user: UserInfomation的对象实例，可以是request.user
   ### title, content都是str
   inbox_views.send_inbox(user, title, content) 
   ```

   
