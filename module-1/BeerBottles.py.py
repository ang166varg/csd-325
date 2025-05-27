#1.3 Assignment     CSD325  Angela Vargas   05/26
print("Welcome to the Reverse Beer Bottle on the Wall ! ")
def countdown(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            bottles -= 1
            print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            bottles -= 1
            print(f"Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")

# Main Program
def main():
    bottles = int(input("Enter number of bottles:"))
    countdown(bottles)
    print("Time to buy more bottles of beer.")

if __name__ == "__main__":
    main()