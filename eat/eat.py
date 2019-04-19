# -*- coding: utf-8 -*-
import time

def check(ans):
    if ans < 0 or 4 < ans:
        print('回答は半角数字（1・2・3）で入力してください')
        exit()

print('\n今はどんな気分？ 半角数字で入力してください：')
q1 = int(input('''\
  1 : がっつり食べたい
  2 : あっさり済ませたい
  3 : 食べなくても良い
  あなたの回答：'''))
check(q1)

print('---')

print('そうなんですね。\nでは、冷蔵庫・冷凍庫の中には何かありますか？')
q2 = int(input('''\
  1 : 野菜もお肉もお魚もたっぷり
  2 : ほぼ空っぽ
  3 : 料理したくない
  あなたの回答：'''))
check(q2)

print('---')

print('分かりました。\nところで最近、お腹の調子はどうですか？')
q3 = int(input('''\
  1 : いい感じ
  2 : よろしくない
  3 : 気にしない
  あなたの回答：'''))
check(q3)

print('---')

print('そうなんですね。\n最後に、食費は気にしますか？')
q4 = int(input('''\
  1 : 質素にしておく
  2 : ゴージャスにする
  3 : 面倒なので金で解決
  あなたの回答：'''))
check(q4)

print('---')

for i in range(3):
    time.sleep(0.5)
    print('\r+ AI集計中 +', end='')
    time.sleep(0.5)
    print('\rx AI集計中 x', end='')
time.sleep(0.8)
print('\rわかりました！\n今のあなたにオススメなのは…')
time.sleep(1.4)

if q1 == 3:
    print('水です。グイッといっときましょう\n')
elif q2 == 2 and q3 == 2:
    print('忍耐です。目についた食材を切って炒め、醤油や酒で味付けしましょう\n')
elif (q2 == 3 and q3 == 3) or q4 == 3:
    print('デリバリーしましょう。ピザやハンバーガーで今日はパーティ！\n')
else:
    print('ルーチンワークです。目についた食材を適当に煮込んでスープにしましょう\n')
