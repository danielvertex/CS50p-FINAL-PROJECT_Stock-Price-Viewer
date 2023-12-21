import matplotlib.pyplot as plt
import re
import yfinance as yf
from datetime import date, timedelta, datetime
from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style, init


def main():
    init(autoreset=True)

    while True:
        selection = menu()
        if selection == ("1. Compare graphically a period of 30 days of adjusted closing price of two actions"):
            gi_date = input(
                "Type the year and the month you want YYYY-MM:\n")
            result, start_date = date_verification(gi_date)
            if result:
                ti_input = input("Insert the symbol of the first action:\n")
                success, ti_info, ti_input = ticker_validation(ti_input)

                while not success:
                    ti_input = input("Invalid ticker, try again: ")
                    success, ti_info, ti_input = ticker_validation(ti_input)

                try:
                    input2 = input("Insert the symbol of the second action:\n")
                    success2, ti_info2, input2 = ticker_validation(input2)

                    while not success2:
                        input2 = input("Invalid ticker, try again: ")
                        success2, ti_info2, input2 = ticker_validation(input2)
                    try:
                        end_date = start_date + timedelta(days=30)


                        tick1 = yf.Ticker(ti_input)
                        tick2 = yf.Ticker(input2)

                        info1 = tick1.info
                        info2 = tick2.info
                        plt.clf()
                        try:
                            lb1 = info1["shortName"]
                        except KeyError:
                            print(
                                Fore.RED + f"No data found, ticker ({ti_input}) may be delisted")
                            
                        try:
                            lb2 = info2["shortName"]
                        except KeyError:
                            print(
                                Fore.RED + f"No data found, ticker ({input2}) may be delisted")

                        try:
                            history = tick1.history(
                                start=start_date, end=end_date, raise_errors=True)
                            plt.plot(history.index,
                                     history["Close"], label=lb1)
                            ticker1 = 1
                            plt.legend(loc="upper left")
                            plt.xlabel("Date")
                            plt.xticks(rotation=45)
                            plt.ylabel("Price (USD)")
                        except (Exception, ValueError):
                            print(
                                Fore.YELLOW + f"there are not aviable data for the ticker {ti_input} in the time solicitated")
                            ticker1 = 0

                        try:
                            history2 = tick2.history(
                                start=start_date, end=end_date, raise_errors=True)
                            plt.plot(history2.index,
                                     history2["Close"], label=lb2)
                            ticker2 = 1
                            plt.legend(loc="upper left")
                            plt.xlabel("Date")
                            plt.xticks(rotation=45)
                            plt.ylabel("Price (USD)")
                        except (Exception, ValueError):
                            print(
                                Fore.YELLOW + f"there are not aviable data for the ticker {input2} in the time solicitated")
                            ticker2 = 0

                        #only hasthe second asked ticker
                        if ticker1 == 1 and ticker2 == 0:
                            plt.title(
                                f"{ti_info["shortName"]} ({ti_info["symbol"]})")
                            plt.savefig(
                                "result.png", bbox_inches="tight")
                            print(
                                Back.GREEN + "Image genereted with 1 ticker 😐\nImage saved as \033[1;4mresult.png\033\n ")
                        #only has the first ticker
                        elif ticker1 == 0 and ticker2 == 1:
                            plt.title(
                                f"{ti_info2['shortName']} ({ti_info2['symbol']})")
                            plt.savefig(
                                "result.png", bbox_inches="tight")
                            print(
                                Back.GREEN + "Image genereted with 1 ticker 😐\nImage saved as \033[1;4mresult.png\033\n ")
                        #no ticker
                        elif ticker1 == 0 and ticker1 == 0:

                            print(Back.YELLOW + "No image generated ☹️")

                        else:
                            plt.legend(loc="upper left")
                            plt.xlabel("Date")
                            plt.xticks(rotation=45)
                            plt.ylabel("Price (USD)")
                            plt.title(f"{ti_info['shortName']} ({ti_info['symbol']}) and {
                                ti_info2['shortName']} ({ti_info2['symbol']})")
                            plt.savefig(
                                "result.png", bbox_inches="tight")
                            print(
                                Back.GREEN + "Image succesfully genereted with 2 tickers😃\nImage saved as \033[1;4mresult.png\033 ")

                    except KeyError:
                        print(
                            Fore.YELLOW + "One or both tickers do not have summary information")

                except KeyError:
                    print(Fore.YELLOW +
                          "One or both tickers do not have summary information")

        if selection == "2. Business Summary":
            menu_option2()

        elif selection == "Exit":
            print("Bye bye ✌️")
            break


def menu():
    options = [
        "1. Compare graphically a period of 30 days of adjusted closing price of two actions",
        "2. Business Summary",
        "Exit",
    ]
    terminal_menu = TerminalMenu(options, title="Menu:")
    menu_entry_index = terminal_menu.show()
    sele = options[menu_entry_index]
    return sele


def menu_option2():
    ti_input = input("Insert the symbol of action:\n")
    success, ti_info, ti_input = ticker_validation(ti_input)

    while not success:
        ti_input = input("Invalid ticker, try again: ")
        success, ti_info = ticker_validation(ti_input)
    try:
        print(Fore.BLUE + f"{ti_info['longName']}")
        print("\033[1;4mSector:\033[0m", ti_info["sector"])
        print("\033[1;4mSummary:\033[0m", ti_info["longBusinessSummary"])

    except KeyError:
        print(Fore.YELLOW + "The ticker does not has summary information")


def ticker_validation(tic):
    while True:
        try:
            info = yf.Ticker(tic).info
            return True, info, tic
        except (ValueError, KeyError) as e:
            if "No data found, symbol may be delisted" in str(e):
                tic = input("Invalid ticker, try again: ")
            else:
                tic = input("Invalid ticker, try again: ")
        except Exception:
            tic = input(f"The ticker probably does not exist, try other: \n")


def date_verification(d):
    while True:
        today_d = datetime.today().strftime("%Y")
        mistak = 0
        try:
            while True:
                if match := re.search(r"(\d\d\d\d)-(\d\d)", d, re.IGNORECASE):
                    if int(today_d) < int(match.group(1)):
                        mistak = 1
                        raise ValueError

                    start_date = date_process(match.group(1), match.group(2))
                    # print(match.group(1))
                    return True, start_date
                else:
                    raise ValueError
        except ValueError:
            if mistak == 1:
                d = input("Ivalid Year or month. Tipe a valid date.\n")
            else:
                d = input("Ivalid date format. Please use YYYY-MM:\n")


def date_process(year_str, month_str):
    year = int(year_str)
    month = int(month_str)
    day = 1
    start_date = date(year, month, day)
    return start_date


if __name__ == "__main__":
    main()
