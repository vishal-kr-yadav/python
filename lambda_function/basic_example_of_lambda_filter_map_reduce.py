# if your interpreter is python3.X then to get all type of result use a list(result), elif in python2.X only result will give the required output
from functools import reduce
#lambda arguments : expression
def example1():
    add=lambda x,y:x+y
    print(add(2,3))

# map(function_object, iterable1, iterable2,...)
def example2():
    l1=[1,2,3]
    l2=[3,4,5]
    result=map(lambda x,y:x+y,l1,l2)
    print(list(result))
    #[4, 6, 8]

def example_map_1():
    d=[{"language":"python","info":"interpreted and compiled"},{"language":"java","info":"interpreted and compiled"}]
    result=map(lambda x:x["language"],d)
    print(list(result))
    #['python', 'java']

    boolean_result=map(lambda x:x["language"]=="python",d)
    print(list(boolean_result))
    #[True, False]

def example_map_2():
    dummy_list=[1,2,3]
    result=map(lambda x:x*2,dummy_list)
    print(list(result))

# filter(function_object, iterable)
def example_filter_lambda_1():
    dummy_list=[1,2,3,4]
    result=filter(lambda x:x%2==0,dummy_list)
    print(list(result))
    #[2, 4]


def example_filter_lambda_2():
    dummy_dict=[{"language":"python","info":"interpreted and compiled"},{"language":"java","info":"interpreted and compiled"}]

    result=filter(lambda x:x['language']=="python",dummy_dict)
    print(list(result))
    #[{'info': 'interpreted and compiled', 'language': 'python'}]

def example_reduce_lambda_1():
    dummy_list=[1,2,3,4]
    result=reduce(lambda x, y: x + y, [47, 11, 42, 13])
    print(result)
    #113

