async def to_times(data):
    data = [i for i in range(96) if data[i]]
    st = "".join([f"{i}{'_' if i!=95 and i+1 in data else ''}" if i in data else ' ' for i in range(96)])
    return list(map(lambda x:f"{15*int(x[0])//60}:{15*int(x[0])%60}-{15*(int(x[-1])+1)//60}:{15*(int(x[-1])+1)%60}", map(lambda x:x.split("_"),st.split())))


# lst = [i for i in range(96)]
# lst.remove(1)
# lst.remove(2)
# lst = [1 if i in lst else 0 for i in range(96)]
# print(lst)
# to_times(lst)