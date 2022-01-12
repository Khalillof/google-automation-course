#!/usr/bin/env python3

""" sort list of items by ouccurnces and count them"""
def count_by_occurences(lst):
    tem_dic = {}

    for i in range(len(lst)):
        item = lst[i];
        if item in tem_dic:
          tem_dic[item] += 1
        else:
            tem_dic[item] = 1
    return tem_dic

""" Group number of items by occurences"""
def groupBy(lst):

   items=[]
   for _key, _value in count_by_occurences(lst).items():
       items.append([_key for i in range(_value)])
   return items


def main():

    _list = ['one', 'two', 'one', 'three', 'two', 'one', 'three', 'one']

    #GroupBy
    print('GroupBy list of lists : '+ str(groupBy(_list)))

    #sort list of items by ouccurnces
    print('count list of items by ouccurnces :' + str(count_by_occurences(_list)))

if __name__ == "__main__":
    main()
