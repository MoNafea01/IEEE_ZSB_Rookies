def sorter(listh):
    listh.sort()
    return listh
def firstlast(x1,target):
    try:
        sorter(x1)
        target1=x1.index(target)
        x1.reverse()
        target2=len(x1) - x1.index(target) - 1
        return target1,target2
    except ValueError as aa:
        print(aa)
    except AttributeError as bb:
        print(bb)