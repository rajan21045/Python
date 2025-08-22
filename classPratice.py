# # # # break
# # # num = 0
# # # for i in range(10):
# # #     num+=1
# # #     if num == 8:
# # #         break
# # #     print("The Num has", num)
# # # print("End of the program.")

# # # # continue
# # # n =0
# # # for i in range(10):
# # #     n+=1
# # #     if n == 8:
# # #         continue
# # #     print("The Odd Number is", n)
# # # print("End of the program.")

# # # #match case
# # # day = int(input("Enter a number between 1 and 7: "))
# # # match day:
# # #     case 1:
# # #         print("Sunday")
# # #     case 2:
# # #         print("Monday")
# # #     case 3:
# # #         print("Tuesday")
# # #     case 4:
# # #         print("Wednesday")
# # #     case 5:
# # #         print("Thrusday")
# # #     case 6:
# # #         print("Friday")
# # #     case 7:
# # #         print("Saturday")
# # #     case _:
# # #         print("Invalid input, please enter a number between 1 and 7.")
# # # print("End of the program.")



# # # wap to find the even number from 1 to 50 using either break or continue
# # # for i in range(1, 51):
# # #     if i % 2 != 0:
# # #         continue
# # #     print(i)
# # # print("End of the program.")

# # # tuple

# # t = (1, 'c', "lumbini", 9+7)
# # print(t)
# # print(type(t))



# # l = list(t)
# # print(l)
# # print(type(l))
# # l.append("String")
# # print(l)
# # t1 = tuple(l)
# # print(t1)
# # t2 = t1 + (5, 6, 'ict', "Campus")
# # print(t2)


# word_list = ["apple", "anana", "cherry", "ate"]
# new_list = []
# for word in word_list:
#     if len(word) > 3 and word[0] =='a':
#         new_list.append(word)
# print(new_list)
# new_list.sort()
# print(new_list)

# # # pyramid

# # for i in range(1, 6):
# #     for j in range(1, i+1):
# #         print("*", end="")
# #     print("\r")    

# n = int(input("Enter a number: "))
# for i in range(1,11):
#         print(f"{n} * {i}: ", n*i)
# print("\r")

# # triangle 
# n =5
# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
#     for k in range(1, 2*i):
#         print("*", end=" ")
#     print(" ")

# dictionary
d = {
    "Faculty": "ICT",
    "Campus": "Lumbini",
    "Location": "Gaindakot, Nawalparasi",
    "Year": 2023,
}
print(d)
print(type(d))