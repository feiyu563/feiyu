#coding:utf-8
'''
Created on 2014年11月21日

@author: Administrator
'''

def Filteradd(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):
            
            before_result = before_func(request,kargs=None)
            if(before_result != None):
                return before_result;
            
            main_result = main_func(request,kargs=None)
            if(main_result != None):
                return main_result;
            
            after_result = after_func(request,kargs=None)
            if(after_result != None):
                return after_result;
            
        return wrapper
    return outer