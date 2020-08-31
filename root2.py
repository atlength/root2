def jisuan(x,y):
    print ('The value of root of 2 approximately is:  %f' % (y/x-1))
    x,y=y,x+2*y
    return x,y


def main():
    a = 2
    b = 5
    for i in range(10):
        print('Steps {}: Got result {}/{}'.format(i,b-a,a))
        a,b = jisuan(a,b)


if __name__ == '__main__':
    main()