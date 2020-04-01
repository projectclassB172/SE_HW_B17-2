for chicken in range(0, 30):
    rabbit = 30 - chicken
    chickLeg = 2 * chicken
    rabLeg = 4 * rabbit

    if (chickLeg + rabLeg == 90):
        print("鸡{0} 兔{1}".format(str(chicken), str(rabbit)))
