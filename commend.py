##insert i e: Insert integer  at position .
##print: Print the list.
##remove e: Delete the first occurrence of integer .
##append e: Insert integer  at the end of the list.
##sort: Sort the list.
##pop: Pop the last element from the list.
##reverse: Reverse the list.

#input
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print


N = int(input())

lis = []

for i in range(N):
    s = input().split()
    commend = s[0]
    argument = s[1:]
    if commend !="print":
        commend += "("+ ",".join(argument) +")"
        eval("lis."+commend)
    else:
        print(lis)
        