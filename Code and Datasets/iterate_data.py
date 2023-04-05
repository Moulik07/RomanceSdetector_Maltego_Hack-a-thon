import csv

with open('ipqs1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    x1 = 0
    x2=0
    x3=0
    x4=0
    for row in csv_reader:
        if line_count == 0 :
            # print(f'Column names are {", ".join(row)} \n')
            line_count += 1
        elif line_count == 1 :
            line_count += 1 
        else:
            print(f'For email address {row[1]} ipqs validation: {row[2]} ,Deliverability: {row[3]},being common: {row[4]} ,and leakability: {row[5]} ')
            if(row[2]=='TRUE'):
                x1=1
            else:
                x1=0

            if(row[3]=='high' ):
                x2=1
            elif(row[3]=='medium'):
                x3=2
            else:
                x2=1

            if(row[4]=='TRUE'):
                x3=1
            else:
                x3=0

            if(row[5]=='TRUE'):
                x4=1
            else:
                x4=0

            print('Percentage of email vulnurability is :'  ,(x1+(x2/3)+x3+x4)*100/4, '%' )
            line_count += 1
        print('\n')
    print(f'Processed {line_count} lines.')