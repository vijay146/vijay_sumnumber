from operator import itemgetter, attrgetter
sum_num_9 =[]

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            for l in range(1,10):
                n=i,j,k,l
                str(n)
                sum = 0
                summ = 0
                for m in n:
                    sum += int(m)
                print(sum)
                y =str(sum)
                for x in y:
                        summ += int(x)
                if (summ == 9):
                     num = (i,j,k,l)
                     sum_num_9.append(num)

print(sum_num_9)
num_9=sorted(sum_num_9, key=itemgetter(3,2,0,1), reverse=True)
print(num_9)

print((num_9[0]))

my_num = input("enter your number:")
my_number_tuple =[]
for t in my_num:
    u = int(t)
    my_number_tuple.append(u)
    my_number_tuples=tuple(my_number_tuple)
print(my_number_tuples)

result = "no"
for number_tuple in num_9:
 res = all(a == b for a, b in zip(number_tuple, my_number_tuples))
 if res == True:
     result = "present"

print(f"your entered number is  {result}")