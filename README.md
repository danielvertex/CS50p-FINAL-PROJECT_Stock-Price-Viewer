# TICKER INFORMATION
#### Video Demo:  https://youtu.be/z2xsYft5r74
#### Description: This program can graphically provide a 30-day period of adjusted closing price of two stocks as a png image and textual ticker information.
## USAGE
The way to choose the desired option is with up and down arrows.
## MENU
### Option 1
#### 1. Compare graphically a period of 30 days of adjusted closing price of two actions
In this option I decided to use regular expressions in order to continue in the program until the user enters the date as requested, this way I could separate in groups the entered data and request it in an organized way to yfinance. It also has verification of the tickers entered because there are many that may be similar, have no information or do not exist.
At the end it generates an image with png extension

### Option 2
#### 2. Business Summary
You must enter a ticker for which it will print the company's, full name, sector and a summary. If the ticker does not exist it will ask for one again. If it exists but has no summary information it will tell you.

## APPROACH
I chose that i wanted to use graphs and request data to a third party to process it. then i wanted to make it a bit more graphical and implement a small menu. The regular expression came in hand to verify the data the user enters.
This project helped me to understand and as a first approach to how to start a project, also to value the importance of reading a lot of documentation, and to take into account alternatives because you can make multiple approaches to the same problem, in addition to implement the knowledge acquired throughout the course.
### Functions
#### main()
Here in addition to the main part of the program you will find option 1 of the program
#### menu()
The menu is located here and returns the user's selection.
#### menu_option2()
it handles theoption 2 of the menu and also calls ticker_validation to validate
#### ticker_validation()
It is in charge of validating the entered ticker and handling possible errors, such as if the ticker does not exist.
#### date_verification()
Regular expressions and datetime are used here to validate the date entered and also to handle possible errors, such as dates that have not yet passed, dates that are too old, or dates that do not exist. This funCtion calls the funCtion **date_process()**.
#### date_process()
Takes the date entered and standardizes it. Thus in main, option 1 you can set the 30-day period to do your processing.
