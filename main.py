import threading 
from threading import*

import time

#dictionary for storing key value data
dict={}

def create(key,value,timeout=0):
    if key in dict:
        print("error: this key already exists")
    else:
        if(key.isalpha()):
            #checking the size of file and JSON object
            if len(dict)<(1024*1020*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    dict[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

def read(key):
    if key not in dict:
         print("error: given key does not exist in database")
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("error: time_to_live",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

def delete(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dict[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del dict[key]
            print("key is successfully deleted")                         


def modify(key,value):
    b=dict[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dict:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dict[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in dict:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dict[key]=l            

create("chennai",24)
read("chennai")