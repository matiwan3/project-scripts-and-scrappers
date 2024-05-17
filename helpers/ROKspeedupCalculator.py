# Action speed ups
def calcSpeedUps():
    minute_speed_ups_1 = int(input("[+] Total amount of 1 minute speed ups: ")) # 1 min speed up
    minute_speed_ups_5 = int(input("[+] Total amount of 5 minute speed ups: ")) # 5 min speed up
    minute_speed_ups_10 = int(input("[+] Total amount of 10 minute speed ups: ")) # 10 min speed up
    minute_speed_ups_15 = int(input("[+] Total amount of 15 minute speed ups: ")) # 15 min speed up
    minute_speed_ups_30 = int(input("[+] Total amount of 30 minute speed ups: ")) # 30 min speed up
    minute_speed_ups_60 = int(input("[+] Total amount of 60 minute speed ups: ")) # 1h speed up
    hours_speed_ups_3 = int(input("[+] Total amount of 3 hours speed ups: ")) # 3h speed up
    hours_speed_ups_8 = int(input("[+] Total amount of 8 hours speed ups: ")) # 8h speed up
    hours_speed_ups_15 = int(input("[+] Total amount of 15 hours speed ups: ")) # 15h speedup
    hours_speed_ups_24 = int(input("[+] Total amount of 24 hours speed ups: ")) # 24h speedup
    days_speed_ups_3 = int(input("[+] Total amount of 3 days speed ups: ")) # 3 days speedup
    days_speed_ups_7 = int(input("[+] Total amount of 7 days speed ups: ")) # 7 days speedup
    total_min_speedups = minute_speed_ups_1 + minute_speed_ups_5*5 + minute_speed_ups_10*10 + minute_speed_ups_15*15 + minute_speed_ups_30*30 + minute_speed_ups_60*60 + hours_speed_ups_3*180 + hours_speed_ups_8*480 + hours_speed_ups_15*900 + hours_speed_ups_24*1440 + days_speed_ups_3*4320 + days_speed_ups_7*10080
    return total_min_speedups

def main():
    print("[*] TOTAL SPEED UP TIME CALCULATOR")
    total_result  = 0
    calcTimes = int(input("[+] Enter a number for how many boost types you want to loop (1,2,3..): "))
    for _ in range(calcTimes):
        total_result += calcSpeedUps()
    
    total_mins_speedup = total_result 
    total_hours_speedup = total_result  / 60
    total_days_speedup = total_hours_speedup / 24
    
    print(f"Total speed ups time: {total_mins_speedup} minutes | {total_hours_speedup:.2f} hours | {total_days_speedup:.2f} days")
    
if __name__ == "__main__":
    main()
    