#ランダムな整数を生成するためにrandomモジュールをインポート
import random


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

# 8章 if分
num =50

if num < 50:
    print("aaa")
elif num < 30:
    print("sss")
else:
    print("aaaaaaa")
    

#ランダムな整数の生成
num = random.randrange(0,3)
print("------------------------")


# 9章　繰り返し
for i in range(1,10):
    print(i)
print("------------------------")
    
while num != 0:
    num = random.randrange(0,3)
    print(num)
print("------------------------")

#11章
user_names = ["あああ","いいい","ううう"]

for user_name in user_names:
    print(user_name)
    
    
data = {1:"あああ",2:"いいい"}

#.items()：辞書からキーと値をセットで取り出す関数
for key ,value in data.items():
    print(f"{key} {value}") 

# 配列からの取り出し
list = ["りんご","ごりら","らっぱ"]
for i,j in enumerate(list):
    print(f"{i} {j}")
    
# 12章　関数
def hello():
    print("お願いします")

hello()
hello()


#　戻り値のヒント
def double(num) -> int:
    return num * 2


# 15章クラス
class Product:
    def __init__(self):
        #属性を定義
        self.name = ""
    def set_name(self,name):
        self.name = name
        

#インスタンス化
pc = Product()

#属性にアクセスする
pc.name = "インテル"
print(pc.name)

pc.set_name("ああ")
print(pc.name)



