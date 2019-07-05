# contains main function and calling
from die import Die

def main():
    d1 = Die(6)
    d2 = Die(20)
    count = 0
    while(count<3):
        a = d1.roll()
        b = d2.roll()
        print("6-sided Die:", a, "20-sided Die:",b,"Total:", a+b)
        count+=1
main()
