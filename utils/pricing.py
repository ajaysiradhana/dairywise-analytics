def get_rate_by_fat(fat):
    fat = float(fat)

    if fat >= 7.0:
        return 60
    elif fat >= 6.5:
        return 58
    elif fat >= 6.0:
        return 55
    else:
        return 50