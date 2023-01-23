# -*- coding: utf-8 -*-
#
# python csv2viz.py -csv1=keiza_org.csv -csv2=keizai_base.csv -csv3=keizai_cnn.csv -csv4=keizai_cnn.csv
# python csv2viz.py -csv1 BS16_ORG.csv -csv2 BS16_BASE.csv -csv3 BS16_CNN.csv -csv4 BS16_CNN_Threhold.csv -out BS16T
#

import pandas as pd
import random
import os
import argparse
import numpy as np
import time
import plotly as py
import plotly.figure_factory as ff

def main(cfg):
    # type  score q-start q-end m-start m-end m-id none none
    # audio 0.266 15.995 38.486 2.291 24.782 07000002 (none) N/A
    #pd.DataFrame({'A': [1, 2, 3]})
    df1 = pd.read_csv(cfg.csv1, header=None, delim_whitespace=True)
    df2 = pd.read_csv(cfg.csv2, header=None, delim_whitespace=True)
    df3 = pd.read_csv(cfg.csv3, header=None, delim_whitespace=True)
    df4 = pd.read_csv(cfg.csv4, header=None, delim_whitespace=True)
    df5 = pd.read_csv(cfg.csv5, header=None, delim_whitespace=True)
    df6 = pd.read_csv(cfg.csv6, header=None, delim_whitespace=True)
    df1.columns=["type", "score", "qs", "qe", "ms", "me", "id", "na1", "na2"]
    df2.columns=["type", "score", "qs", "qe", "ms", "me", "id", "na1", "na2"]
    df3.columns=["type", "score", "qs", "qe", "ms", "me", "id", "na1", "na2"]
    df4.columns=["type", "score", "qs", "qe", "ms", "me", "id", "na1", "na2"]
    df5.columns=["type", "score", "qs", "qe", "ms", "me", "id", "na1", "na2"]
    df6.columns=["type", "score", "qs", "qe", "ms", "me", "id", "na1", "na2"]
    # print("org", df1)
    # print("base", df2)
    # print("cnn", df3)
    # s = df1[["qs", "qe"]]
    # print(s)

    '''
    for index, row in df2.iterrows():
        print(index)
        print('------')
        print(type(row))
        print(row)
        print('------')
        print(row[0], row['type'], row.type)
        print(row[1], row['score'], row.score)
        print(row[2], row['qs'], row.qs)
        print(row[3], row['qe'], row.qe)
        print(row[4], row['ms'], row.ms)
        print(row[5], row['me'], row.me)
        print(row[6], row['id'], row.id)
        print('======\n')
    '''
    
    df = []
    # df.append(dict(Task="TEST", Start=100, Finish=120, Resource='Apple'))
    # df.append(dict(Task="TEST", Start=500, Finish=550, Resource='Banana'))
    for index, row in df1.iterrows():
        df.append(dict(Task="ORG", Score=row.score, Start=row.qs, Finish=row.qe, Resource=str(row.id)))
    for index, row in df2.iterrows():
        df.append(dict(Task="ORG45", Score=row.score, Start=row.qs, Finish=row.qe, Resource=str(row.id)))
    for index, row in df3.iterrows():
        df.append(dict(Task="BASE", Score=row.score, Start=row.qs, Finish=row.qe, Resource=str(row.id)))
    for index, row in df4.iterrows():
        df.append(dict(Task="BASE45", Score=row.score, Start=row.qs, Finish=row.qe, Resource=str(row.id)))
    for index, row in df5.iterrows():
        df.append(dict(Task="CNN", Score=row.score, Start=row.qs, Finish=row.qe, Resource=str(row.id)))
    for index, row in df6.iterrows():
        df.append(dict(Task="CNN45", Score=row.score, Start=row.qs, Finish=row.qe, Resource=str(row.id)))

    # ball_the_colors = list((x,y,z) for x in range(256) for y in range(256) for z in range(256))
    colors = []
    id_array = []
    for row in df:
        id_array.append(row["Resource"])
    id_lists = list(set(id_array))
    print(set(id_lists))

    r = lambda: random.randint(0,255)
    colors = ['#%02X%02X%02X' % (r(),r(),r())]
    for i in range(1, len(id_lists)):
        colors.append('#%02X%02X%02X' % (r(),r(),r()))

    print("colors", colors)
    title = cfg.out
    fig = ff.create_gantt(df, colors=colors, index_col='Resource', title=title, show_colorbar=True, group_tasks=True ,showgrid_x=True, showgrid_y=True, bar_width=0.4)
    addAnnot(df, fig)
    # https://plotly.github.io/plotly.py-docs/generated/plotly.figure_factory.create_gantt.html
    fig.update_layout(xaxis_type='linear')
    py.offline.plot(fig, filename = cfg.out + ".html")
    # fig.show()

def addAnnot(df, fig):
    for i in df:
        x_pos = (i['Finish'] - i['Start'])/2 + i['Start']
        for j in fig['data']:
            if(j['name'] == i['Resource']):
                y_pos = (j['y'][0] + j['y'][1] + j['y'][2] + j['y'][3])/4
                print(y_pos)
        fig['layout']['annotations'] += tuple([dict(x=x_pos,y=y_pos,text=i['Score'],font={'color':'black'})])
    py.offline.plot(fig, filename="ganttChart.html")

def config(config):
    print("csv1 : ", config.csv1)
    print("csv2 : ", config.csv2)
    print("csv3 : ", config.csv3)
    print("csv4 : ", config.csv4)
    print("csv5 : ", config.csv5)
    print("csv6 : ", config.csv6)
    print("out  : ", config.out)
    return config

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-csv1', required=True)
    parser.add_argument('-csv2', required=True)
    parser.add_argument('-csv3', required=True)
    parser.add_argument('-csv4', required=True)
    parser.add_argument('-csv5', required=True)
    parser.add_argument('-csv6', required=True)
    parser.add_argument('-out', required=True)


    main(config(parser.parse_args()))
