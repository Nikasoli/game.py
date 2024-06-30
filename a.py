lst4=[]
    result=pk.execute('select grade from std')
    for i in result:
        lst4.append(*i)
    dx=pd.DataFrame(lst4)
    d=dx.describe()
    L3.config(text=d)