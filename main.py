import pandas as pd
import numpy as np
import seaborn as sns
import re
import warnings
warnings.filterwarnings('ignore')

test = pd.read_csv('D:/data/movie/movies_test.csv')
train = pd.read_csv('D:/data/movie/movies_train.csv')
submission = pd.read_csv('D:/data/movie/submission.csv')

# print(train.head(3))
# print(test.head(3))
# print(submission.head(3))

#배급사 전처리
train['distributor']= train.distributor.str.replace("(주)","")
train['distributor']= train.distributor.str.replace("(","")
train['distributor']= train.distributor.str.replace(")","")
test['distributor']= test.distributor.str.replace("(주)","")
test['distributor']= test.distributor.str.replace("(","")
test['distributor']= test.distributor.str.replace(")","")
# print(train.head(3))
# print(test.head(3))
pd.set_option("display.max_rows",None,"display.max_columns",None)
# print(train['distributor'].unique()) #배급사 이름만 출력
train['distributor'] = [re.sub(r'[^0-9a-zA-Z가-힣]','',x) for x in train.distributor] #한글 숫자 영어 만가능
test['distributor'] = [re.sub(r'[^0-9a-zA-Z가-힣]','',x) for x in test.distributor]

def get_dis(x):
    if 'CJ' in x or 'CGV' in x:
        return 'CJ'
    elif '쇼박스' in x:
        return '쇼박스'
    elif 'SK' in x:
        return 'SK'
    elif '리틀빅픽' in x:
        return '리틀빅픽쳐스'
    elif '스폰지' in x:
        return '스폰지'
    elif '싸이더스' in x:
        return '싸이더스'
    elif '에이원' in x:
        return '에이원'
    elif '마인스' in x:
        return '마인스'
    elif '마운틴픽' in x:
        return '마운틴픽처스'
    elif '디씨드' in x:
        return '디씨드'
    elif '드림팩트' in x:
        return '드림팩트'
    elif '메가박스' in x:
        return '메가박스'
    elif '마운틴' in x:
        return '마운틴'
    else:
        return x

train['distributor'] = train.distributor.apply(get_dis)
test['distributor'] = test.distributor.apply(get_dis)

#장르별 영화 관객수 평균값으로 랭크 인코딩