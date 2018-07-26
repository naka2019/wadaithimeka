# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math

# 順運動学の計算

class fk(object):
  # 各リンクの長さと関節角度の取得
  l1 = 0
  l2 = 0
  th1 = 0
  th2 = 0
  def __init__(self, l1_, l2_, th1_, th2_):
   self.l1 = l1_
   self.l2 = l2_
   self.th1 = th1_
   self.th2 = th2_
    # リンク1の手先
  def x1(self):
    return self.l1 * math.cos(self.th1)
  def y1(self):
    return self.l1 * math.sin(self.th1)

    # リンク2の手先
  def x2(self):
    return self.x1() + self.l2 * math.cos(self.th1 + self.th2)

  def y2(self):
    y2 = self.y1() + self.l2 * math.sin(self.th1 + self.th2)

    # 手先位置をNumPy配列に格納して返す
    return np.array([[0.0, self.x1(),self.x2()], [0.0, self.y1(),y2]])

 

def main():
    # リンク1, 2の長さ
    L = [0.5, 0.5]

    # 第1, 2の関節角度
    th = np.radians([90, 0])
    # 順運動学の計算
    p = fk(L[0],L[1], th[0],th[1])
    # グラフ描画位置の設定
    fig, ax = plt.subplots()
    plt.axis('equal')
    plt.subplots_adjust(left=0.1, bottom=0.15)
    plt.xlim([-1, 1])
    plt.ylim([-0.3, 1.3])
    # グラフ描画
    plt.grid()
    T = p.y2()
    print T[0]
    graph, = plt.plot(T[0], T[1])

    def update_th1(slider_val):
        # 関節1の角度を更新
        th[0] = np.radians([slider_val])

        # 順運動学の計算

        p = fk(L[0],L[1], th[0],th[1])

        # 手先位置を更新
        T = p.y2()
        print T[0]
        graph.set_data(T[0], T[1])
        graph.set_linestyle('-')
        graph.set_linewidth(5)
        graph.set_marker('o')
        graph.set_markerfacecolor('g')
        graph.set_markeredgecolor('g')
        graph.set_markersize(15)

        # グラフの再描画
        fig.canvas.draw_idle()

    def update_th2(slider_val):
        # 関節2の角度を更新
        th[1] = np.radians([slider_val])

        # 順運動学の計算
        p = fk(L[0],L[1], th[0],th[1])

        # 手先位置を更新
        T = p.y2()
        print T[0]
        graph.set_data(T[0], T[1])
        graph.set_linestyle('-')
        graph.set_linewidth(5)
        graph.set_marker('o')
        graph.set_markerfacecolor('g')
        graph.set_markeredgecolor('g')
        graph.set_markersize(15)

        # グラフの再描画
        fig.canvas.draw_idle()
    
    # スライダーの表示位置
    slider1_pos = plt.axes([0.1, 0.05, 0.8, 0.03])
    slider2_pos = plt.axes([0.1, 0.01, 0.8, 0.03])

    # SliderオブMoveジェクトのインスタンス作成
    threshold_slider1 = Slider(slider1_pos, 'th1', 0, 180)
    threshold_slider2 = Slider(slider2_pos, 'th2', 0, 180)

    # スライダーの値が変更された場合の処理を呼び出し
    threshold_slider1.on_changed(update_th1)
    threshold_slider2.on_changed(update_th2)
    graph.set_linestyle('-')
    graph.set_linewidth(5)
    graph.set_marker('o')
    graph.set_markerfacecolor('g')
    graph.set_markeredgecolor('g')
    graph.set_markersize(15)
    plt.grid()
    plt.show()
  

if __name__ == '__main__':
     main()
