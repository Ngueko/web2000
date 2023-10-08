def main():
    start_value = int(input("Enter start value: "))
    stop_value = int(input("Enter stop value: "))
    increment_value = int(input("Enter increment value: "))
    
    while start_value <= stop_value:
        print(start_value)
        start_value += increment_value

if __name__ == "__main__":
    main()