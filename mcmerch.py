import sys 

def parseArguments():
    arguments = {
        "price": int(sys.argv[1]), #first argument that you enter as input when running the code in terminal sys,arg[2] would be second input entered as input into terminal command
        "quantity": 1,
        "province": "ON"
        }
    return arguments #allow for scalability and can add more features

#can scale parArguments without affecting taxRate and vice versa
#consider scalability (can you scale feature up) and extensibility (can you add multiple features)

def taxRate(province):
    tax = {
        "ON": 0.13
    }
    return tax[province] #return whatever tax of province is


def mcmerchCalculator():
    arguments = parseArguments()
    tax = taxRate(arguments['province'])
    print(round(arguments['price'] * arguments['quantity'] * (1 + tax),2))



mcmerchCalculator()
