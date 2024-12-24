def main():

    print("Welcome to the tip calculator!")
    total_bill = input("What's the total bill? $")
    total_bill_float = float(total_bill)
    #print(f'Bill $'+ total_bill)
    tip_percentage = input("How much tip would you like to give? 10, 12 or 15%? ")
    tip_percentage_float = float(tip_percentage)
    #print(f'Tip '+ tip_percentage +'%')

    #P% of N
    # P/100 × N
    # Or
    #(P × N)/100
    # Where, P is the percent,  N is the number % is equal to 1/100

    total_tip = (tip_percentage_float * total_bill_float ) / 100
    total_tip_round = round(total_tip)
    total_tip_round_to_string = str(total_tip_round)
    #print(f'Tip $'+total_tip_round_to_string)

    total_bill_plus_tip = (total_bill_float + total_tip_round )
    total_bill_plus_tip_to_string = str(total_bill_plus_tip)

    print(f'Total $'+ total_bill_plus_tip_to_string)

    

    
if __name__=="__main__":
        main()

