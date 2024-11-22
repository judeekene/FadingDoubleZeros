# FadingDoubleZeros
From the Book
DAY TRADING AND SWING TRADING THE CURRENCY MARKET
Technical and Fundamental Strategies to Profit from Market Moves
Third Edition
Kathy Lien

Strategy Rules
Long:
1. Identify a currency pair that is trading below its intraday 20-period simple
moving average on a 15-minute chart.
2. Enter a long position 10 to 15 pips above the figure.
3. Place an initial protective stop 20 pips below the figure.
a. When the position is profitable by the amount risked, close half of the
position and move your stop on the remaining portion of the trade to
breakeven.
b. Trail your stop as the price moves in your favor.
Short:
1. Identify a currency pair that is trading above its intraday 20-period simple
moving average on a 15-minute chart.
2. Short the currency pair 10 to 15 pips below the figure.
3. Place an initial protective stop 20 pips above the round number.
4. When the position is profitable by the amount that you risked, close half of the
position and move your stop on the remaining portion of the trade to breakeven.
Trail your stop as the price moves in your favor.

Fading Double Zeros Strategy
A Python skeleton implementation (This algorithm was generated with the assistance of Microsoft Copilot, an AI companion developed by Microsoft, to implement a trading strategy based on specific rules for entering and managing long and short positions.). It can be improved and tested by adding a data feed and relating to it using the on ticks (IB broker provide Python APIs for automated trading (have not got access to it yet though)). Accessing the price of the identified currency, computing the 15-minute moving average, and rounding the price to 2 dp which becomes the figure. Computing the position size by risk or by fixed position. Handling pips correctly by assessing the Pipsize, sending the positions to the market, updating the position and closing the position.
