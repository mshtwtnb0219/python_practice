age = 18 #年齢　コメントは#で記載する

if age < 20:
    print("あああ")
else :
    print("いいい")
    
print(45 + 18)
print(30 - 12)
print(15 * 6)
print(30 / 3)
print(45 % 8)
print("わたな" + "まさ")


#5章
user_name = 'あいうえお'
#変数はスネークケースがいい??

# 変数の中身を出力する際はf {変数名}
print(f"{user_name}")

#6章
# 配列には4種類ある　リスト(list) タプル(tuple) セット(set) ディクショナリ(dictionary)

#リスト
user_list = ["要素1","要素2","要素3","要素4","要素5"]
#リスト　取り出し
print(user_list[1])
#リスト　全て取り出し
print(user_list)
#リスト　追加　削除
user_list.append("要素6")
user_list.pop(2) #要素番号を削除する



#タプル 要素の追加・変更・削除が行えない配列
user_tapule = ("あああ","いいい","ううう")
#要素の取り出し
print(user_tapule[1])

#セット　順番　重複の2概念を持たない配列　集合とも呼ばれる
user_set = {2,1,3,4,4,5,5,6,7}
print(user_set)
#追加・削除
user_set.add(11)
user_set.remove(1)
print(user_set)


#7章 連想配列（ディクショナリ
user_dictionary = {1:"トレイ",2:"風呂",3:"便器"}
print(user_dictionary[1])
#削除
user_dictionary.pop(2)









