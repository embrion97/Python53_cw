import random

#n = int(input())
#a = 0
#while n>0:
#    print(a)
#    a+=1


# n = int(input())
# a = 0
# while a<=n:
#     if a%2 == 0:
#         print(a)
#         a = a+1
#     else:
#         a = a + 1


# n = int(input("a"))
# a = 0
# while a<=n:
#     print("privet")
#     a = a+1

# x1 = int(input())
# x2 = int(input())
# if x1 > x2:
#     x1,x2 = x2,x1
# if x1%2:
#     x1+=1
# while x1 <= x2:
#     print(x1)
#     x1 = x1 + 2



# n = int(input("число"))
# a = 0
# while n != 0:
#     n = n//10
#     a = a + 1
#
# print(a)

# x = None
# a = 0
# while x != 0:
#     x = int(input("chislo"))
#     a = a + x
# print(a)
counter = 101
z = 0
play = 0
while z != 1:
    x = random.randint(0,100)
    counter_play = 0
    play = play + 1
    while True > 0:
        a = int(input("chislo"))
        if a == x:
            counter_play = counter_play + 1
            if counter_play < counter:
                counter = counter_play
            print("otgadal")
            print("будешь играть еще раз?1 - da, 2 - net")
            quesch = int(input())
            if quesch == 2:
                z = 1
                print(f"Ваш лучший результат {counter} в {play} играх")
            elif quesch == 1:
                print(counter_play)
            break

        elif a < x:
            counter_play = counter_play + 1
            print("a men'she x")
            print()
        else:
            counter_play = counter_play + 1
            print("a bol'she x")


