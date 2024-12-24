def main():

    print("Welcome to the Stop Loss Take Profit Calculator")
    entry_price = input("What's your entry price? $")
    float_entry_price = float(entry_price)
    round_float_entry_price = round(float_entry_price)
    string_entry_price = str(round_float_entry_price)
    risk_percentage =input("How much of your capital would you like to risk? 5, 6, 10, 15, 25 or 50%? ")
    profit_percentage =input("How much would you like to grow your capital on this trade? 5, 10, 15, 20, 60, 100, 300, 600 or 1000%? ")
    print(f"You're investing $"+ string_entry_price) 
    float_profit_percentage = float(profit_percentage)
    float_risk_percentage = float(risk_percentage)
    percentage = ( float_entry_price * float_risk_percentage ) / 100
    float_percentage = float(percentage)
    float_percentage_round = round(float_percentage)
    string_percentage = str(float_percentage_round)
    print(f"You're risking $"+ string_percentage)
    final_value = (float_entry_price - percentage)
    final_value_round = round(final_value)
    string_final_value = str(final_value_round)

    print(f"Stop loss at $"+ string_final_value)

    profit_percentage = ( float_entry_price * float_risk_percentage ) / 100

    take_profit = (float_entry_price + ( (float_entry_price * float_profit_percentage) / 100 ))
    take_profit_round = round(take_profit)
    string_take_profit = str(take_profit_round)
    print(f"Take profit at $"+ string_take_profit)

if __name__=="__main__":
        main()