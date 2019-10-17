# -*- coding: utf-8 -*-
# made for wujie
# batch process to reorganize files
#
# Copyright@ lilei 2019-10-16
#
import os
import shutil
import time
from collections import deque

def decide_year(date):
# return year(2017001->2017)
    ts = time.strptime(date, "%Y%j")
    year = time.strftime("%Y", ts)
    return year

def decide_month(date):
# return year-month(2017001->2017-01)
    ts = time.strptime(date, "%Y%j")
    month = time.strftime("%Y-%m", ts)
    return month

def decide_mday(date):
# return monthday(2017001->2017001(0101))
    ts = time.strptime(date, "%Y%j")
    monthday = time.strftime("%Y%j(%m%d)", ts)
    return monthday

def mk_dir(target_root_addr, date):
    target_folder = target_root_addr + '\\' + decide_year(date)+ '\\' + decide_month(date)+ '\\' + decide_mday(date)
    if os.path.exists(target_folder) == False:
        os.makedirs(target_folder)
    return

def reorganize_files(src_root_addr, target_root_addr):
# make dirs and reorganize file acccording to file name
# src_root_addr: source folder
# target_root_addr: target folder
    files = os.listdir(src_root_addr) # all files under src_root_addr
    for file in files:
            if file[-3:] == 'hdf':
                date = (file[10: 17])
                mk_dir(target_root_addr, date)
                src_addr = src_root_addr + '\\' + file
                target_addr = target_root_addr + '\\' + decide_year(date) + '\\' + decide_month(date) + '\\' + decide_mday(date) + '\\'+ file
                shutil.copyfile(src_addr, target_addr)

            # In case you want to remove the source file.
            #   os.remove(src_addr)
    return

def broad_search_file(file_que, target_addr):
# search all the files in root_dir and move them into target_addr
    while len(file_que) != 0:
        file = file_que.popleft()
        if os.path.isfile(file):
            shutil.move(file, target_addr)
        else:
            temp_files = os.listdir(file)
            for temp_file in temp_files:
                file_que.append(os.path.join(file, temp_file))
    return

if __name__=="__main__":
# src_root: source folder
# target_root: target folder
    src_root = r'E:\xfmovie'  # Change
    target_root = r'E:\New folder' # Change
    file_que = deque()
    file_que.append(src_root)
    broad_search_file(file_que, target_root)