# -*- coding: utf-8 -*-
# お寿司を流すプログラムです
import utility

osushi_lane = ['__', '__', '__', '__', '__']
lane_count = int(len(osushi_lane))

osushi_count = int(input('\nお寿司は何皿食べる？（1〜3）：'))

if osushi_count <= 0:
    print('おっ食べないのかい？\n')
elif osushi_count > 3:
    print('お客さん、焦り過ぎだよ〜\n1度に3皿までの注文でよろしくね\n')
else:
    print('あいよ、ちょっと待ってな')
    # お寿司が流れてくるプログラム
    utility.repeat(osushi_lane, lane_count, osushi_count)
    # レーンを綺麗にしてお茶を出します
    l = str(''.join(osushi_lane))
    print('( ^▽^) 🍵 [' + l + '](^_^ )お茶どうぞ\n')
