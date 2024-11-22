def trading_strategy(currency_pair, current_price, moving_avg, figure, position_size):
    # Constants
    long_entry_offset = 10
    short_entry_offset = -10
    stop_loss_offset = 20
    target_profit = stop_loss_offset

    # Initialize position
    position = None
    entry_price = 0
    stop_loss = 0
    target_exit = 0

    # Long Position Rules
    if current_price < moving_avg:
        entry_price = figure + long_entry_offset
        if current_price >= entry_price:
            position = 'long'
            stop_loss = figure - stop_loss_offset
            target_exit = entry_price + target_profit

    # Short Position Rules
    if current_price > moving_avg:
        entry_price = figure + short_entry_offset
        if current_price <= entry_price:
            position = 'short'
            stop_loss = figure + stop_loss_offset
            target_exit = entry_price - target_profit

    # Position Management
    if position == 'long' and current_price > entry_price:
        if current_price >= target_exit:
            position_size /= 2  # Close half the position
            stop_loss = entry_price  # Move stop to breakeven
        if current_price > entry_price:
            stop_loss = max(stop_loss, current_price - target_profit)  # Trail stop

    if position == 'short' and current_price < entry_price:
        if current_price <= target_exit:
            position_size /= 2  # Close half the position
            stop_loss = entry_price  # Move stop to breakeven
        if current_price < entry_price:
            stop_loss = min(stop_loss, current_price + target_profit)  # Trail stop

    return position, entry_price, stop_loss, target_exit, position_size
