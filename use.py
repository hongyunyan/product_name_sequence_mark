#将测试结果转换为便于查看的文件格式,通过逗号隔开每个提取出来的名词.这边是适用于test集原本标注的都为O的

file = open("/home/sophiahong/Desktop/product_name_sequence_mark/data_path_save/1517901636/results/label_test",'r')
file2 = open("/home/sophiahong/Desktop/product_name_sequence_mark/data_path_save/1517901636/results/label_test_r",'w')
data = file.readlines()
word = []
goodWord = []
ColorWord = []
temp = []
Color = []
i = 0
for row in data:
    i += 1
    if (len(row)!=1):
        word.append(row[0])
        if (row[4]=='B'):
            if (row[6]=='P'):
                if (len(Color)!=0):
                    ColorWord.append(Color)
                Color=[]
                Color.append(row[0])
            else:
                if (len(temp)!=0):
                    goodWord.append(temp)
                    print(temp)
                temp = []
                temp.append(row[0])
        elif (row[4]=='I'):
            if (row[6]=='P'):
                Color.append(row[0])
            else:
                temp.append(row[0])

    else:
        if (len(temp)!=0):
            goodWord.append(temp)
            print(temp)
            temp=[]
        if (len(Color)!=0):
            ColorWord.append(Color)
            Color=[]
        for w in word:
            file2.write(w)
        file2.write(",")
        for item in goodWord:
            for ww in item:
                file2.write(ww)
            file2.write(",")
        for it in ColorWord:
            for www in it:
                file2.write(www)
            file2.write(",")
        file2.write("\n")

        word=[]
        goodWord=[]
        Color=[]
        ColorWord=[]
file2.close()