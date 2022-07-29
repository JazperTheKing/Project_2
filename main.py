
import api, cash_on_hand, overheads, profit_loss

def main():

    forex = api.api_function()
    overheads.overhead_function(forex)
    cash_on_hand.cash_on_hand_function(forex)
    profit_loss.profit_loss_function(forex)

main()
