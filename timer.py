"""@Authors: Charles, Jordan, Shelby, Robert, Jon"""
# Start a mission clock when the user enters the Death Star. 
# The user has 10 minutes to complete the mission before the Death Star blows up. 
# If the user does not complete the mission in time, they lose.

# import time
# t = 600
# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end='\r')  # Overwrite the line each second
#         time.sleep(1)
#         t -= 1

#     print("Fire in the hole!!")

# import time

# start_time = time.time()

# # Main program logic...
# for i in range(10):
#     print(f"Elapsed: {time.time() - start_time:.2f} seconds")
#     time.sleep(1)   