from datetime import datetime,timedelta
def get_date_list(n,strf = '%A %d %b %Y'):
    t = datetime.now()
    lst = (t+timedelta(days=i) for i in range(n))
    return map(lambda x: datetime.strftime(x,strf),lst)

# for i in get_date_list(7):
#     print(i)
#     id='1057678575478087540' 
