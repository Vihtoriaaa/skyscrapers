from skyscrapers import check_skyscrapers

if __name__ == "__main__":
    if(check_skyscrapers("skyscrapers/check.txt")) == True:
        print('Everything works fine!')
    else:
        print('Something goes wrong!')