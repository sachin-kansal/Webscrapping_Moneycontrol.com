from webscrapping import Moneycontrol

def main():
    print("Welcome to Webscrapping Moneycontrol website")
    print("Home page url -->", Moneycontrol.url)
    #Moneycontrol.companylist()
    c_name=input("\nPlease enter the name of stock from above list:")

    i=True
    while i==True:
        if c_name not in Moneycontrol.extractingurl().keys():
            print("please check the value belongs to the list and is correct")
            c_name=input("\nPlease enter the name of stock from above list:")
        else:
            Moneycontrol.get_scrapped_data(c_name)
            c_name=input("\nPlease enter the name of stock from above list:")
            
        if c_name=="Exit":
            i=False
if __name__=="__main__":
    Moneycontrol.companylist()
    main()