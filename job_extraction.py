from requests import get
from bs4 import BeautifulSoup

sites = []

base_url = 'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term='
search_term = 'python'

response = get(f'{base_url}{search_term}')

if response.status_code != 200:
    print('cannot access to website')
else: 
    jobs_on_remo = []
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('section',class_='jobs')
    for job_section in jobs:
        print(job_section)
        print('--------------------------------------------------------')
    #     job_post = job_section.find_all('li')
#         job_post.pop(-1)
#         for post in job_post:
#             anchors = post.find_all('a')
#             anchor = anchors[1]
#             link = anchor['href']
#             company_info = anchor.find_all('span', class_='company')
#             name, time, region = company_info
#             title = anchor.find('span', class_='title')
#             job_data = {
#                 'link' : f'https://weworkremotely.com{link}',
#                 'name' : name.string,
#                 'time' : time.string,
#                 'region' : region.string,
#                 'position' : title.string
#             }
#             jobs_on_remo.append(job_data)
# for i in jobs_on_remo:
#     print(i)
#     print('----------------seperator--------------------')
#     print('----------------seperator--------------------')
#     print('----------------seperator--------------------')


