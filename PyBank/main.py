# Import the correct modules to be able to work in CSV file
import os
import csv

#select the csv file origin
csvpath = os.path.join('.','Resources','budget_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    print(f"Header:{csv_header}")
    
    # Create 2 variables to store months and total profit_losses
    months = []
    profit_losses = []

    # Read each row of data after the header
    for row in csvreader:
        # Add number of months, which is located in first row
        months.append(row[0])
    
        #Add net_total, which is located in second row
        profit_losses.append(int(row[1]))

    #Print statement in command prompt to validate its funtionality.
    print("Financial Analysis")

    print("________________________________________________")
    #to make sure I count unique values
    total_months=len(set(months))
    # To print results in cmd prompt to confirm its functionality  
    print(f"Total months:{total_months}")
   
   #to sum all profit / losses of the period
    total_prof_loss = sum(profit_losses)
    # To print results in cmd prompt to confirm its functionality  
    print(f"Total profit Losses: ${total_prof_loss}")

    # Set variance to loop through the data, excluding first row
    i = 0
    total_var_month = []
    #calculate variance month by month
    for i in range(len(profit_losses)-1):

        #Add value of variance by month
        var_month = float(profit_losses[i+1])-float(profit_losses[i])

        #Store the total variance for the period        
        total_var_month.append(var_month)
        ave_var_month = sum(total_var_month)/len(total_var_month) 

     # To print results in cmd prompt to confirm its functionality   
    print(f"Average change: $ {round(ave_var_month,2)}")

     
    #calculate min and max value
    max_value = max(total_var_month)
    max_val_index = (total_var_month.index(max_value)+1)
    # To print results in cmd prompt to confirm its functionality  
    print(f"Greatest Increase in Profits: {months[max_val_index]}, {int(max_value)}")

    #calculate min value 
    min_value = min (total_var_month)
    min_val_index = int((total_var_month.index(min_value)+1))
    # To print results in cmd prompt to confirm its functionality  
    print(f"Greatest Decrease in Profits: {months[min_val_index]}, {int(min_value)}")
    breakpoint()

# Set variable for output txt file
output_txt = os.path.join(".","analysis","analysis.txt")
 #Open the output file (reference: https://www.geeksforgeeks.org/reading-writing-text-files-python/)
with open(output_txt,'w') as txtfile:
    #  write the same items printed by command prompt but in the txt file
    txtfile.write(f"Financial Analysis\n")
    txtfile.write("_______________________________________________________\n")
    
    txtfile.write(f"Total months:{total_months}\n")

    txtfile.write(f"Total profit Losses: ${total_prof_loss}\n")

    txtfile.write(f"Average change: $ {round(ave_var_month,2)}\n")

    txtfile.write(f"Greatest Increase in Profits: {months[max_val_index]}, {int(max_value)}\n")

    txtfile.write(f"Greatest Decrease in Profits: {months[min_val_index]}, {int(min_value)}\n")

