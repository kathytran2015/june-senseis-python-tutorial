def terminator2():
    print("I will be back")
# terminator2()
# for i in range(10):
#     terminator2()
def dating_age_calc(your_age, your_partners_age):
    # return your_age//2+7, your_age*2-7
    lower_bound = your_age//2+7
    upper_bound = your_age*2-7
    time_you_have_to_wait = 0
    if your_partners_age > upper_bound:
        print("Maybe not")
    elif your_partners_age < lower_bound:
        print("Kirby's calling the police")
        while your_partners_age < lower_bound:
            time_you_have_to_wait += 1
            your_partners_age += 1
            your_age += 1
            lower_bound = your_age//2+7
        print(f"You gotta wait {time_you_have_to_wait}")
    else:
        print("Yay...")
dating_age_calc(24, 17)
