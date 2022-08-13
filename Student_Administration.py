import csv
def write_into_csv(info_list):
    with open('student.info.csv', 'a', newline ='') as Csv_File:
         writer = csv.writer(Csv_File)
         if Csv_File.tell() == 0:
             writer.writerow(["Name","Age","Roll_Number","Email_id"])
         writer.writerow(info_list)
if __name__ == "__main__":
    condition = True
    student_num = 1
    while (condition):
        student_info = input("Enter Student information for student_no-{} in the following format (Name-Age-Roll_Number-Email_id) : ".format(student_num))
        student_info_list = student_info.split('-')
        print('\nThe Entered Information is: \n Name : {}\n Age : {}\n Roll_Number : {}\n Email_id : {}'.format( student_info_list [0],
        student_info_list [1], student_info_list [2], student_info_list [3]))
        choice_check = input("Is Entered Information Correct (Yes/No) : ")
        if choice_check == 'Yes':
            write_into_csv(student_info_list)
            condition_check = input("Enter (Yes/No) If You Want To Enter Information For Another Student : ")
            if condition_check == 'Yes':
                condition = True
                student_num = student_num + 1
            elif condition_check == 'No':
                condition = False
        elif choice_check == 'No':
            print(" Enter the Student Information Again! ")




