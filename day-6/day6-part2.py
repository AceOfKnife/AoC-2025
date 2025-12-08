def main():
    
    numbers = []

    with open("day6-test.txt") as mathHomework:
        print(len(mathHomework))
        for line in mathHomework:
            print(line.split(" "))
        
if __name__=="__main__":
    main()