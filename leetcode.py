from typing import *
from sys import *
from builtins import *
from marshal  import *
from time import *
from zipimport import *
from encodings import *
from abc import *
from stat import *
from genericpath import *
from posixpath import * 
from site import *
from types import *
from enum import *
from sre_constants import *
from sre_parse import *
from sre_compile import * 
from itertools import *
from keyword import *
from operator import *
from reprlib import * 
from collections import *
from functools import *
from copyreg import *
from re import * 
from string import *
from math import *
from datetime import *
from heapq import *
from bisect import * 
from weakref import *
from copy import *
from warnings import *
from random import *
from numbers import *
from decimal import *
from fractions import *
from statistics import *
from json import * 
from gettext import *
from argparse import *
from errno import *
from fnmatch import *
from zlib import *
from shutil import *
from signal import *
from threading import *
from contextlib import *
from select import *
from selectors import *
from subprocess import * 
from platform import *
from uuid import *
from sysconfig import *
from struct import * 
from zoneinfo import *
from array import *
import typing 
import sys 
import builtins 
import marshal  
import time 
import zipimport 
import encodings 
import abc 
import stat 
import genericpath 
import posixpath  
import site 
import types 
import enum 
import sre_constants 
import sre_parse 
import sre_compile  
import itertools 
import keyword 
import operator 
import reprlib  
import collections 
import functools 
import copyreg 
import re  
import string 
import math 
import datetime 
import heapq 
import bisect  
import weakref 
import copy 
import warnings 
import random 
import numbers 
import decimal 
import fractions 
import statistics 
import json  
import gettext 
import argparse 
import locale 
import errno 
import fnmatch 
import zlib 
import shutil 
import signal 
import threading 
import contextlib 
import select 
import selectors 
import subprocess  
import platform 
import uuid 
import sysconfig 
import struct  
import zoneinfo 
import array 
###code begin###

#1. 两数之和
#https://leetcode.cn/problems/two-sum/
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
        
#         return []
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
###code end###

if __name__ == '__main__':
    dirs = dir()
    if "Solution" in dirs:
        funcname = dir(Solution)[-1]
        solu = Solution()
        func = getattr(solu,funcname)
        param_cnt = func.__code__.co_argcount-1
        with open("in.txt","r") as infile:
            lines = infile.readlines()
        sample_cnt = len(lines) // param_cnt
        ind = 0
        for _ in range(sample_cnt):
            params = []
            for _ in range(param_cnt):
                params.append(eval(lines[ind]))
                ind += 1
            ans = func(*params)
            print(ans)
    else:
        with open("in.txt","r") as infile:
            lines = infile.readlines()
        if len(lines) == 2:
            funcnames = eval(lines[0])
            funcparams = eval(lines[1])
            classname = funcnames[0]
            classparam = funcparams[0]
            funcnames = funcnames[1:]
            funcparams = funcparams[1:]
            strparam = ",".join(map(str,classparam))
            code = "sol = "
            code += str(classname)
            code += "("+strparam+")\n"
            code += "ans = [None]\n"
            for fun,par in zip(funcnames,funcparams):
                strparam = ",".join(map(str,par))
                code+="ans.append(sol."+str(fun)+"("+strparam+"))\n"
            code += "print(ans)"
            exec(code)