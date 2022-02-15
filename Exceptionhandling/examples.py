# try:
#     a=10/0
#     print(a)
# except ZeroDivisionError:
#     print('Division by zero is not allowed')

# try:
#     a=50
#     b='c'
#     print(a/b)
# except TypeError:
#     print('divide by char is not allowed')

#
#
# list=[2,0,'v',20,'s',0,500,10,15,'m',0]
# for numbers in list:
#     try:
#         a=10/numbers
#         print(a)
#     except ZeroDivisionError:
#         print('number cannot be divide by zero')
#     except TypeError:
#         print('number cannot be divide by character')


# def add(a,b):
#     try:
#         c=a+b
#         print('after adding:',c)
#     except TypeError:
#         print('yu cannot add character and number')
#     finally :
#         print('suucess')
# add(1,'v')


def sub(x,y):
    try:
        z=x-y
        print('sub will perform')
    except TypeError:
        print('u cant sub number and character')
    else:
        print(z)
sub(4,'a')


