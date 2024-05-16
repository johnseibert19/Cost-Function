def main():

    file_path = "NorfolkCosts.txt"
    fp = "SeibertCosts.txt"
    
    norfolkCostArray = []
    seibertCostArray = []

    with open(file_path, "r") as file:
        for line in file:
            norfolkCostArray.append(line.strip())
    
    with open(fp, "r") as file:
        for line in file:
            seibertCostArray.append(line.strip())
            
    for i in range(len(norfolkCostArray)):
        if (norfolkCostArray[i] != seibertCostArray[i]):
            print("Costs differ at index " + i)
        else:
            if i == len(norfolkCostArray) - 1:
                print("All good!")

if __name__ == "__main__":
    main()