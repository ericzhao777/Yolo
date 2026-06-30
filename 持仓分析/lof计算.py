def multi_stop_loss(prices, shares, loss_rate=0.02):
    # 计算加权成本价  
    total_cost = sum(p*s for p,s in zip(prices, shares))
    avg_price = total_cost / sum(shares)
    return round(avg_price * (1 - loss_rate), 2)

# 示例：10元买300股，9元补200股
print(multi_stop_loss([1050.5,1018.27], [3.8062,1.9641]))
