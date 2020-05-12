import csv
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TLCAS.settings")
django.setup()

from papers.models import *

def import_data(dataset_name: str):
    '''
    @param dataset_name 将要导入的csv文件名，注意以.csv结尾
    @return None
    @brief 
           将某会议的所有论文信息整合成csv表格，保存在/papers/static/dataset/文件夹下
           
           表格内格式要求如下：
           |index|year|title|author|abstract|link|pdf|affiliation|name|
           即
           |索引信息记录，不记录在数据库|论文年份|论文题目|作者(逗号分隔)|摘要|在线阅读链接|pdf链接|所属机构|会议名称|

           脚本根据这个表头结构读取csv内容导入数据库，link和affliation没有记录的话，csv中保留表头，该列全部置空
    '''
    with open('papers/static/dataset/' + dataset_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) # 跳过表头
        for row in reader:
            curr_conf, created = ConferenceInfo.objects.get_or_create(
                name=row[8],
                year=int(row[1])
            )

            curr_paper, created = PaperInfo.objects.get_or_create(
                conference=curr_conf,
                paper_title=row[2],
                authors=row[3],
                abstract=row[4],
                pdf_link=row[6]
            )

            if len(row[7].strip()) > 0:
                curr_paper.affiliations = row[7].strip()
            if len(row[5].strip()) > 0:
                curr_paper.read_link = row[5].strip()
            curr_paper.save()

if __name__ == "__main__":
    # import_data('AAAI.csv')
	# import_data('ICML.csv')
    pass