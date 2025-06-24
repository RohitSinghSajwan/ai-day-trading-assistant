def check_profit(entry_price, current_price, target_pct=10):
    gain_pct = ((current_price - entry_price) / entry_price) * 100
    hit_target = gain_pct >= target_pct
    return gain_pct, hit_target
