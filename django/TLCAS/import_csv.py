import csv
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TLCAS.settings")
django.setup()

from papers.models import PaperInfo, ConferenceInfo

def import_data(dataset_name):
    with open('../../dataset/' + dataset_name + '.csv') as f:
           reader = csv.reader(f)
           for row in reader:
              if row[1] != 'year':  #where year is first column's name
                _, created = ConferenceInfo.objects.get_or_create(
                    name=row[8],
                    year=row[1],
                )
                _, created = PaperInfo.objects.get_or_create(
                    year = row[1],
                    conference_name = row[8],
    				paper_title = row[2],
    				authors = row[3],
    				abstract = row[4],
    				read_link = row[5],
    				pdf_link = row[6],
    				affiliations=row[7],
                    )

if __name__ == "__main__":
	#import_data('AAAI')
	import_data('ICML')