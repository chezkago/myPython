#1/29/26 Activity
#Obtains minutes and remaining seconds from seconds 
total_seconds = int(input("Input seconds: "))

minutes = total_seconds // 60                   #Calculating Minutes

remaining_seconds = total_seconds % 60          #Calculating Seconds

print(minutes, "minutes", remaining_seconds, "seconds")

print(f"{minutes} minutes and {remaining_seconds} seconds") #Another way to print 