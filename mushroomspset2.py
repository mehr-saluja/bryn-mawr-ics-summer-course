mushrooms = []
check = True
small = 0
medium = 0
large = 0
while check == True:
    option = input("Enter a mushroom weight, or type STOP to end: ")
    if option == "STOP":
        check = False
        print(f"The weights you entered were", mushrooms)
        for each in mushrooms:
            if each < 100:
                small= small + 1
            elif each >= 100 and each < 1000:
                medium = medium + 1
            elif each >= 1000:
                large = large + 1
        print("There were", small, "small mushrooms")
        print("There were", medium, "medium mushrooms")
        print("There were", large, "large mushrooms")
    else:
            weight = int(option)
            if weight <= 0:
                print("Weight must be bigger than 0")
            else:
                mushrooms.append(weight)
              

# The program collects mushroom weights and categorizes them into small, medium, and large based on their weight.