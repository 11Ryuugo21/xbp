from os import name
from re import A
from select import select
ok = 0
name=input("あなたのお名前は？")
while(True):
    print("あなたは神奈川大学に入学した。"
    "このゲームは道用先生の好感度を上げるゲームだ。"
    "いくつかの選択肢を答えて好感度を上げ、単位取得を目指そう！")
    "いくつかの選択肢を答えて好感度を上げ、単位取得を目指そう！")
    select=int(input("あなたはプログラム科目を取ろうとしている。"
    "道用先生の担当はXBPプログラムだが、あなたは何を取る？"
    "1.企業と何かを作りたい！マネジメントプログラム"
    "2.やっぱりこれでしょ。XBPプログラム"
    "3.留学したい!IBCプログラム"))

    if select==2:
        print("やったね。道用先生からの好感度2up!")
        ok=ok+2
        break
    elif select==1:
        print("残念。道用先生からの好感度1down")
        ok=ok-1
        break
    elif select==3:
        print("残念。道用先生からの好感度1down")
        ok=ok-1
        break
while(True):
    select=int(input("道用先生のメガネがいつもと変わってる！さあなんて言う？"
    "1.個性的ですね！"
    "2.悪くないですね！"
    "3.めっっっっっちゃ似合ってます！！！"))

    if select==3:
        print("やったね。先生すごく嬉しそう。道用先生からの好感度3up!")
        ok=ok+3
        break
    elif select==1:
        print("残念。なんか先生戸惑ってる。道用先生からの好感度1down")
        ok=ok-1
        break
    elif select==2:
        print("残念。先生、怪訝そうな顔してる。道用先生からの好感度3down")
        ok=ok-3
        break
while(True):   
    select=int(input("XBPの授業での発表。先生が挙手を求めてる。誰も手を挙げそうにない。どうする？"
    "1.ここはやっぱり自分が！！手を挙げる。"
    "2.えーーーーーー。誰かやらないかな、と周りに視線を送る。"
    "3.うーーーーーーーーーんめんどいし、、、、寝ーようっ⭐️"))

    if select==1:
        print("やったね。先生めちゃめちゃ嬉しそう。しかも発表も褒められた!道用先生からの好感度5up!")
        ok=ok+5
        break
    elif select==2:
        print("残念。キョロキョロしてて先生にあてられた!道用先生からの好感度2down")
        ok=ok-2
        break
    elif select==3:
        print("残念。いびきをかいて寝てるのがバレて説教!道用先生からの好感度5down")
        ok=ok-5
        break
while(True):
    print("さあ！道用先生の好感度はどうなったかな？あなたの好感度は10点満点中の", ok,"点です") 
    break