# https://github.com/anelachan/sentimentanalysis
from sentiment import *
import os
# 'geometric', 'harmonic', 'average'
file_list=['1.txt','2.txt','3.txt','4.txt','5.txt']
r=[]
for each in file_list:
    d = {}

    f = open(each, "r")
    content = (f.read())
    f.close()
    main_content = os.linesep.join([s for s in content.splitlines() if s])
    main_content_after_removing_new_line=main_content.replace('\n', '')
    # print(type(main_content_after_removing_new_line))
    s = SentimentAnalysis(filename='SentiWordNet.txt',weighting='geometric')

    a=s.score(main_content_after_removing_new_line.decode('utf-8').strip())
    d['score']=a
    fileName=each.split('.')[0]
    d['fileName']=fileName
    r.append(d)
    # a=s.score('i  love you')

print(r)