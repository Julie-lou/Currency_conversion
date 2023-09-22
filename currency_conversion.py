

def currency_conversion(currency,amount):
    if type(amount)==int or type(amount) ==float:
        if  currency =="USD" or currency =="usd":
            return float(amount)*4000
        elif currency =="Yuan" or currency =="yuan":
            return float(amount)* 643
        elif currency =="BATH" or currency =="batH":
            return float(amount)* 123
        elif currency !="USD" or "Yuan" or "Bath":
            return("not found")
    if type(amount) == str:
        return ("invalid amount")
    