# _tall_enough_to_ride

minimum_height : int = 50 # arbitrary units :)

def main():
    height = float(input("How tall are you? "))
    if height >= minimum_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()