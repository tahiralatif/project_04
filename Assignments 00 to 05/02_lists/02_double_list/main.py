# double list

def main():
    numbers = [1, 2, 3, 4, 5]

    for i in range(len(numbers)):
        elem_at_index = [i] 
        numbers[i] = elem_at_index *2
        print(numbers[i])
       
        
if __name__ == "__main__":
    main()        