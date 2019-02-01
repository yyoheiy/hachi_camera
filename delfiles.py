import os,time
from dateutil.relativedelta import relativedelta
from datetime import datetime


def del_file(path):
    files=[]
    dirc=os.listdir(path)

    for file in dirc:
        files.append([file,os.path.getctime(path+file)]) #get filename and date
    today=datetime.now()
    pday=today-relativedelta(months=2) #2months before
    e_today=int(time.mktime(today.timetuple())) #epoch of today
    e_pday=int(time.mktime(pday.timetuple())) #epoch of pday
    for f,t in files:
         
        if t<e_pday:
            print(f)

            os.remove(path+f)

if __name__=="__main__":
    filepath="C:/Users/yyohe/Desktop/売掛_1809/"
    del_file(filepath)
