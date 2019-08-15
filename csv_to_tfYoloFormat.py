#!/usr/bin/env python3
#coding=utf-8

#============================#
#Program:csv_to_tfYoloFormat.py
#将.csv格式的文件转换为yolov3_tensorflow中需要的格式
#Date:2019.08.15
#Author:liheng
#Version:V1.0
#============================#

__author__ = 'liheng'

def main():
    # inputFile = "./data/train_labels.csv"
    # outputFile = "./data/train_yoloTF.txt"
    inputFile = "./data/test_labels.csv"
    outputFile = "./data/test_yoloTF.txt"

    with open(inputFile,mode='r') as inFile,open(outputFile,mode='w') as outFile:
        inFile.readline()#去除首行
        for line in inFile:#读取一行
            content = line.split(',')
            newContent = "./images/{0} {1},{2},{3},{4},0\n".format(content[0],content[4],content[5],content[6],content[7].rstrip())
            outFile.write(newContent)

if __name__ == "__main__":
    main()
