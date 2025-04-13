# 06_seconds_in_yearS

Days_in_year = 365
hours_in_day = 24   
minutes_in_hour = 60
seconds_in_minute = 60

def main():
    """Calculate the number of seconds in a year."""   
    print("welcome to the seconds in a year calculator\n")        

    second_in_year = Days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
    print("There are", second_in_year, "seconds in a year") 
if __name__ == "__main__":
    main()       