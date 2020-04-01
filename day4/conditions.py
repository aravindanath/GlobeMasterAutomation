# age  = 18
#
# if age >=18 :
#     print('YOU CAN VOTE')
# else:
#     print("You cant vote")
#


env = "RTT"

if env is "Staging":
    print("Excuting on staging env")
elif env is "UAT":
    print("Excuting on UAT env")
elif env is "QA":
    print("Excuting on UAT env")
else:
    print("Select rite env!")


print("Out of condition")

