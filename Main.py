List_1 = [10,501,22,37,100,999,87,351]
odd_list=[]
even_list=[]

for n in List_1:
    if n%2 != 0:
        odd_list.append(n)
    
    else:
        even_list.append(n)
print ("Odd list is: ",odd_list)
print ("Even list is: ",even_list)
------------------------------------------------------------------
List_2 = [10, 501, 22, 37, 100, 999, 87, 351]
prime_list = []

for n in List_2:
    if n > 1:
        for i in range(2, n):
            if n % i == 0:  
                break
        else:  
            prime_list.append(n)

print("prime list is:",prime_list,
      "count of prime numbers in the list is:",len(prime_list))
--------------------------------------------------------------------------
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
New_num = []
for num in numbers:
    my_happy = set()
    List = num

    while num != 1 and num not in my_happy:
        my_happy.add(List)
        List = sum(int(digit)**2 for digit in str(List))
    if List ==1:
        New_num.append(num)
        Count=len(New_num)
print(f"The happy numbers in the list are:{New_num}and the count of happy numbers are:{Count}")
--------------------------------------------------------------------------
number = [257645,84674386,845748]
first_and_last =[]
for n in number:
    n2 = n
    str_value = str(n2)
    first_num = int(str_value[0])
    last_num = int(str_value[-1])
    sum_of_first_and_last = (first_num)+(last_num)
    first_and_last.append(sum_of_first_and_last)
print(f"sum of first and last digit is:{first_and_last}")
---------------------------------------------------------------------------
coins = [1, 2, 5, 10]

ways = []

for c1 in range(11): 
    for c2 in range(6):  
        for c5 in range(3):  
            for c10 in range(2):  
                if (c1*1 + c2*2 + c5*5 + c10*10) == 10:
                    ways.append((c1, c2, c5, c10))

for w in ways:
    print(f"1Rs={w[0]}, 2Rs={w[1]}, 5Rs={w[2]}, 10Rs={w[3]}")

print("Total ways:", len(ways))

---------------------------------------------------------------------------------
List4 = [10,20,30,40]
List5 = [30,40,50]
unique_value1=set(List4)
unique_value2=set(List5)
Duplicate_value = unique_value1 & unique_value2
Duplicate_value = list(Duplicate_value)
print(Duplicate_value)
-------------------------------------------------------------------------------------
Lists = [4, 5, 9, 4, 7, 5, 9, 8]

first_non_repeat = 0
for x in Lists:
    if Lists.count(x) == 1:
        first_non_repeat = x
        break

print("First non-repeating element:", first_non_repeat)
----------------------------------------------------------------------------------------

nums = [4, 5, 6, 7, 0, 1, 2]
nums.sort()
sorted_min_value = nums[0]
print(sorted_min_value)
------------------------------------------------------------------------------------------
list = [10, 20, 30, 9]
Expected_value = 59

triplet_count = False   
n = len(list)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if list[i] + list[j] + list[k] == Expected_value:
                print("Triplet:", list[i], list[j], list[k])
                triplet_value = True   

if not triplet_value:   
    print("No triplet found")

--------------------------------------------------------------------------------------------

list = [4, 2, -3, 1, 6]
n = len(list)
found = False
new_list = []   

for i in range(n):
    total = 0
    temp = []   
    for j in range(i, n):
        total += list[j]
        temp.append(list[j])
        if total == 0:
            found = True
            new_list = temp[:]   
            break
    if found:
        break

if found:
    print("new_list with sum 0:", new_list)
else:
    print("No new_list with sum 0")
