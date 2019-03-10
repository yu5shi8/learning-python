# -*- coding: utf-8 -*-
import time

# お寿司が流れてくる部分です
def repeat(osushi_lane, lane_count, osushi_count):
    repeat = lane_count + osushi_count
    while repeat > 0:
        l = ''.join(osushi_lane)
        print('( ・▽・)[' + str(l) + '](・_・;)', '\r', end='')
        time.sleep(0.8)

        # リストの先頭をひとつ削除します
        del osushi_lane[0]

        # お寿司の数だけ、リスト（osushi_lane）の末尾にお寿司を追加します
        if osushi_count > 0:
            osushi_lane.append('🍣 ')
            osushi_count -= 1

        # 流すお寿司がなくなったら、リスト（osushi_lane）の末尾にレーンを追加します
        else:
            osushi_lane.append('__')
            repeat -= 1
