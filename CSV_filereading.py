# importing csv module
import csv
  
# csv file name
filename = "healthcare-dataset-stroke-data.csv"

male_stroke = []
female_stroke = []
female_non_stroke = []
male_non_stroke = []
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:

        rows.append(row)
        
        if row[9] != "N/A":

            if row[11] == '1':

                if row[1] == "Male":

                    male_stroke.append(float(row[9]))
                
                else:

                    female_stroke.append(float(row[9]))
            
            else:
                
                if row[1] == "Male":

                    male_non_stroke.append(float(row[9]))
                
                else:

                    female_non_stroke.append(float(row[9]))

  
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
  
#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col),
    print('\n')


print(male_stroke)
print("Average of male_stroke := ", sum(male_stroke)/ len(male_stroke))
print("Average of male_non_stroke := ", sum(male_non_stroke)/ len(male_non_stroke))
print("Average of female_stroke := ", sum(female_stroke)/ len(female_stroke))
print("Average of female_non_stroke := ", sum(female_non_stroke)/ len(female_non_stroke))