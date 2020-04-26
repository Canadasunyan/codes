# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:48:43 2019

@author: ROG
"""
import threading
import time
from queue import Queue
# =============================================================================
#描述器：class套着另一个class
# =============================================================================
#     描述器协议
#     descr.__get__(self, obj, type=None) -> value
# 
#     descr.__set__(self, obj, value) -> None
# 
#     descr.__delete__(self, obj) -> None
# =============================================================================

class Teen: 
#不使用初始值时建立class
    def __get__(self,instance,owner): #只有get时为非数据描述符，查找顺序不一样
        return self.owner
    def __set__(self,instance,OwnerName):        #instance.owner='Mr. Sun'
        self.owner=OwnerName
    def __delete__(self,instance):
        del self.owner

class TeenPet:             #属性描述符 
    owner=Teen()             #属性是一个class
    def info(self,*args,price=100,**kwargs):
        self.price=price
        guests_count=len(args)
        print('He will sleep with Guest No.',end='')
        for value in args:
            print(value,end='')
            guests_count-=1
            if guests_count>=2:
                print(', ',end='')
            elif guests_count==1:
                print(' and ',end='')
            else:
                print('.')
        for key,value in kwargs.items():
            def transform(x):
                return x.replace('_',' ')
            print('The',transform(key), 'of the boy is',value)
            self.__dict__[str(key)]=value
          
#tim.info(1,2,4,type='cute',penis_length=14)           #keyword 在数值后面，不能写成x=0  
#kwargs={'Tom':16,'Jack':14}
#info(0,1,2,Tom=16,Jack=14) 
    
# =============================================================================

        



class Boy:       
# =============================================================================
    def __init__(self, name='Tom', age=16, role='bottom',info={'penis_length':14,'weight':60}):
        self.name=name
        self.age=age   #访问时使用 boy1._boy__age 
        self.role=role
        self.__boytype = None    #"假"名字，不能与装饰器名字相同
        self.info=info
    def __repr__(self):          #print实例对象
        return ('We have captured a boy named '+self.name+'!')
    def say_hi(self):
        print('Hi everyone, my name is %s.' % self.name)
    def intro(self,txt,sep='>_<'):
        buffer=''
        while True:
            while sep in buffer:
                pos=buffer.index(sep)
                yield buffer[:pos]
                buffer=buffer[pos+len(sep):]
            chunk=txt.read(200)     
            if not chunk:
                yield buffer
                break
            buffer+=chunk
        return 'I have told you everything I know!'
                
        
    def get_age(self,rank=1):
        def report(self,rank):
            print('The cute boy named',self.name,'ranks',rank,'and is',self.age,'years old')
            return self.age
        return report(self,rank)
    def __del__(self):          #仅实例不操作会被回收，调用__del__方法,删除不用的实例
        #print('You just killed the previous sweet little boy',self.name,'!')
        del self
 
# =============================================================================
 
    def __getattr__(self,item):       #查不到某属性时使用
        return self.info[item]
#    def __getattribute__(self,item):      #最先调用
#        return 'attribute'  

# =============================================================================

    @property      #函数模式变为属性模式 = def get_boytype(self) / getter()
    def boytype(self):
        #self.__boytype='cute'      #设置默认属性参数
        return self.__boytype       
    @boytype.setter                 #设置boy1.boytype='' 
    def boytype(self,character):    #设置默认参数没有用
        self.__boytype=character
        print('Now his character is {}'.format(character))
    @boytype.deleter
    def boytype(self):             # del boy1.boytype
        print('His character infomation has been deleted!')
        del self.__boytype
        
# =============================================================================
      
    def jerk(self,n=5):
        try:
            assert isinstance(n,int)==True and n>=0 ,'Not a valid integer!'
        except AssertionError as ae:
            print('Fuck you!')
            raise ae
        else:       
            rank=n+1
            if n<=1:
                raise Exception('At least 2 boys must jerk off!')
            print(n,'boys are masturbating.')
            while n-1:
                yield ('Boy '+str(rank-n)+' jerks off.')
                n-=1
            if n==1:
                yield ('The last boy has jerked off!')
            return 'The masturbation has stopped, and they feel comfortable!'
# =============================================================================
#    def jerk_off(self,n):
#        assert isinstance(n,int)==True and n>=0,'Not a valid integer!'     
#        rank=n+1
#        if n<=1:
#            raise Exception('At least 2 boys must jerk off!')
#        print(n,'boys are masturbating.')
#        while n-1:
#            yield ('Boy '+str(rank-n)+' jerks off.')
#            n-=1
#        if n==1:
#            yield ('The last boy has jerked off!')
#            return 'They feel comfortable!'
# =============================================================================

class Bestboy:#(object):
    instance=None
#单例模式：所有的实例为同一个地址, 其子类也只能有一个实例对象
# __new__在对象生成之前，控制对象生成过程，不return一个类，则无init.new只执行一次
#为对象分配内存
    def __new__(cls,*args,**kwargs):
        
#1. 创建对象时new最先自动调用
        #print('There can only be one best boy!')
        if cls.instance is None:           
#2. 为对象分配内存空间
            cls.instance = super().__new__(cls)        # new是静态方法需要传参数
#3. 返回对象引用，作为初始化方法init的第一个参数    
        return cls.instance  
    def __init__(self,role='a good boy'):
        self.role=role

# =============================================================================      

class DuckMetaclass(type):
       
    def __new__(cls, name, bases, attrs):
        def p(self):
            print( 'I give my daddy a handjob every day ^ω^')
        attrs['blow'] = lambda self, freq=2: print('I am blowed by daddy %d times a day >_<' % freq)
        attrs['handjob']=p
        return type.__new__(cls, name, bases, attrs)
      
class Duck(Boy,Bestboy,metaclass=DuckMetaclass):             #继承顺序：左>右
    
    def __init__(self,name='Mike',age=18,price=1000):
        self.price=price
        self.name=name
        self.age=age
        self.virgin='He \'s still an innocent virgin ≧△≦'
        super().__init__(name,age)            #解决构造方法同名时调用父类方法的问题
    def __call__(self, new_price,age=0):                 # 对实例对象操作: boy2(a,b)
        if age==0:            
            self.age=self.age+1
        else:
            self.age=age
        self.price = new_price
        print('The price of the boy has changed to {},because he is now {} years old'.format(self.price, self.age))
    #duck.mro() / duck.__mro__
    def fuck(self):                          #子类的函数名会覆盖父类函数名
        print ('This cute duck has been fucked ˙０˙')
        self.virgin= 'He\'s not a virgin any more ⊙﹏⊙'
        #return datetime.now(boy1).year-self.birthday.year
    def say_hi(self,sextype='bottom'):
        "The cute twink is introducing himself." #文档，print(boy2.say_hi.__doc__)
        super().say_hi()        
        print('I am also a duck who likes to be the %s.' % sextype)

# =============================================================================
#meteclass


# =============================================================================
# 
# =============================================================================
#查找更改实例对象属性
def attributes(x):
    return x.__dict__
def set_attr(x):    
    x.__dict__.update({'name':'new name', 'age':x.age+1})
    print(x.__dict__)
    
# =============================================================================
def take_off_clothes(i):
    global name_list
    print(name_list[i],'has taken his clothes off!')
def enqueue(queue):
    global name_list
    while True:
        for i in range(len(name_list)):
            queue.put(str(name_list[i]+'has been queueing to jerk off'),timeout=2)
    print('All cute boys are waiting in queue!')
def jerk_one_by_one(queue,name):
    x=queue.get()
    print(x)
    print('has jerked off!')
    
    
# =============================================================================

# =============================================================================

if __name__=="__main__":
#     boy1=Boy(name='Jim')                            
#     boy1.name='Mike'
#     set_attr(boy1)
#     boy2=Duck()
#     tim=TeenPet()
#     tim.info(1,2,4,type='cute',penis_length=14)
#     f=open('E:/text.txt')
#     teen1=Teen()
#     teen1.age=17
#     tom=TeenPet()
#     tom.owner='Me'
#     print(tom.owner)
    def sex_moan(self):
        print('Fuck me, Daddy! Ah,ah,ah!＞０＜')   
    moaner=type('moaner',(),{'moan':sex_moan}) #(object,)   #moaner是一个类的名字
# =============================================================================
#     jerk_boy=boy1.jerk(5)
#     print(jerk_boy.__next__())   # or next(jerk_boy)
#     print(boy1.boytype)
# =============================================================================
    name_list=['Albert','Bob','Chris','David','Ellen','Frank','Gary','Henry']
    masturbate_queue=Queue(maxsize=100)
    enqueue(masturbate_queue)
# =============================================================================
#     for i in range(len(name_list)):
#         thread1=threading.Thread(target=take_off_clothes,args=[i])
#         thread1.start()
# =============================================================================
#    for i in range(len(name_list)):
#        masturbate_queue.put(name_list[i],'has jerked off')
#    print('enqueue')
    for i in range(len(name_list)):
        thread2=threading.Thread(target=jerk_one_by_one,args=(masturbate_queue,name_list[i],))
        thread2.start()
        
        
        
    masturbate_queue.task_done()
    masturbate_queue.join()
    print('fuck you')
    
         
     
     
     
     
     
     
     
     
     
     
     
     
     