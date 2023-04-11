#ejemplo1:
def main():
    height= int(input("Height:"))
    pyramidn(height)
def pyramidn(n):
    for i in range(n):
        print("#" * i)
        
if__name_ == "_main_":
main() 

#ejemplo:2
def main():
    height= int(input("Height:"))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print(i, end="")
        print("#" * i)

if __name__ == "__main__":
     main()



