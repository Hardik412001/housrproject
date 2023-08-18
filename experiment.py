def is_possible(target_weight, packets): # 1500 , [list]
    dp = [False] * (target_weight + 1)
    dp[0] = True

    for packet in packets: # 900
        for weight in range(packet, target_weight + 1): # 900,1501
            dp[weight] = dp[weight] or dp[weight - packet] # 900
            if dp[weight]:
                print("packet: ",packet,"\n","weight: ",weight)


    return dp[target_weight]

# dp[600] = True , dp[1200] = True, dp[900] = True , dp[]


# def find_combination(target_weight, packets): # 600,[list]
#     if not is_possible(target_weight, packets):
#         return "not possible"
#     else:
#         return "possible"

#     combination = []
#     while target_weight > 0:
#         for packet in packets:
#             if target_weight >= packet and is_possible(target_weight - packet, packets):
#                 combination.append(packet)
#                 target_weight -= packet
#                 break

#     return combination


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
