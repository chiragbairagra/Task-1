import csv

def write_csv(info_list):
    with open('student_info_csv','a',newline='') as csv_file:
        writer= csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name" , "Age" , "DOB" , "Contact Number" , "Email ID"])
        writer.writerow(info_list)
        
if __name__ == '__main__':
    condition=True
    while (condition):
        student_info= input("Enter student imformation in the format(Name Age DOB Contact_Number Email_ID): ")
        print(student_info)

        student_info_list = student_info.split(' ')
        print("Splitted information is: " + str(student_info_list))

        choice_check= input("Is the entered information correct? (yes/no): ")
        if choice_check == 'yes':
            write_csv(student_info_list)
            condition_check=input("Enter (yes/no) if you want to enter information for other student: ")
            if condition_check== 'yes':
                condition=True
            else:
                condition= False

        else:
            print("\nPlease enter the values again: ")

    
