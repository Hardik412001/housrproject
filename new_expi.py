def is_possible(target_weight, packets):
    dp = [False] * (target_weight + 1)
    dp[0] = True

    for packet in packets:
        for weight in range(packet, target_weight + 1):
            dp[weight] = dp[weight] or dp[weight - packet]


    return dp[target_weight]


if __name__ == '__main__':

    given_packets = [600, 900, 2000]

    user_input = int(input("Enter the weight in grams: "))
    if user_input < 0:
        print("Give Positive Value")
    else:
        result = is_possible(user_input, given_packets)

        if result:
            print("possible")
        else:
            print("Not Possible:")
