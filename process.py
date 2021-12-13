log_file = open("um-server-01.txt") # opening the txt file with the open method passing in the file and saving it to a variable named log_file.


def sales_reports(log_file):  #Defining a function named sales_reports setting log_file as our parameter.
    for line in log_file:     #Looping over the file, naming 'line' as our iterator.
        line = line.rstrip()  #Calling .rstrip on each line removing any white-space.
        day = line[0:3]  # Using slice notation where we are starting at index of 0 and ending at 3.
        if day == "Mon": #if statement, checking to see if day is equal to 'Mon'.
            print(line) #Printing out each line thats equal to 'Mon'.


sales_reports(log_file)  #calling our function and passing in log_file.
