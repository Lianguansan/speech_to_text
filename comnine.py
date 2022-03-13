import itertools
import numpy as np

#list = [15,16,15,17,18,19,20,21,22,23]
list = [3,11,4,5,5,2,8,10,5,6,9,3,8,8,7,5,12,9,13,5,7,4,8,1,8,9,11,10,10,9,8,3,8,9,7]
#print(len(list)) #長さを調べる
#print(list[1]) #一個の要素をアクセスできる
#print(list.index(list[2])) ,#listのインデックスをアクセス
#print(np.arange(35)+1) #番号を作成
i = 0
id = -1
for pair in itertools.combinations(np.arange(35), 5):
    #print(pair) #インデクスの組み合わせ(5個の数字の組み合わせ)
    #print(type(pair))
    #print(np.array(pair)+1) #tuple をndarray に変換してから、要素変更できる
    #print(pair[2]) #組み合わせの中のインデクスの一つ
    #print(list[pair[2]]) #そのインデクスに対応する要素
    sum = 0
    i_even = 0
    i_small = 0
    for k in range(5):
        print(pair[k]+1)
        sum = sum + list[pair[k]]
        if (pair[k]+1) % 2 == 0:
            i_even = i_even + 1
        if (pair[k]+1) < 18:
            i_small = i_small + 1

    print('sum',sum)
    #print(pair[1],'sum:',sum(pair))
    #print(np.array(pair) + 1, 'sum:', sum)
    if sum== 40 and i_small == 0 and i_even == 2 :
        i = i + 1
        with open('sample.txt', 'a') as f:
            print(np.array(pair)+1,'sum:',sum, file = f)

    #id = id +1
    #if id == 0:
    #    break
print('total:',i)
