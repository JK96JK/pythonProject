def sort1(my_list):
    return sorted(my_list)
def my_sort(my_list):
    sorted_list2=[]
    for i in my_list:
        if sorted_list2==[]:
            sorted_list2.append(i)
        else:
            for j in sorted_list2:
                k=sorted_list2.index(j)
                h=[i]
                if i in sorted_list2:
                    continue
                else:
                    if i<j:
                        if sorted_list2.index(j)==0:
                            sorted_list2=h+sorted_list2[k:]
                        else:
                            sorted_list2=sorted_list2[:k]+h+sorted_list2[k:]
                    else:
                        if k==len(sorted_list2)-1:
                            sorted_list2=sorted_list2[:(k+1)]+h
                        else:
                            sorted_list2=sorted_list2[:k]+h+sorted_list2[(k+1):]

    return sorted_list2

sorted_list1=sort1(my_list)
sorted_list2=my_sort(my_list)