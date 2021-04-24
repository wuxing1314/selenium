def addSeq(n):
    start, end = 1, 2
    stop = (n+1) / 2
    mysum = start + end
    while start < stop:
        if mysum == n:
            print (start, end)
            mysum -= start
            start += 1
            end += 1
            mysum += end
        elif mysum < n:
            end += 1
            mysum += end
        else:
            mysum -= start
            start += 1


if __name__ == '__main__':

    addSeq(100)
