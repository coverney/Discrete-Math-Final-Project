import io
import pickle

# Read throrugh text file line by line
# Each line has the ID number of the sender, separated by a space from the number ID of the receiver

def parse_emails(filename):
    with open(filename) as fp:
        line = fp.readline()
        departments = {}
        cnt = 1

        while line:
            if cnt % 1000 == 0:
                print(cnt)
            line = fp.readline()
            cnt += 1
            data = line.split()
            if len(data) < 2:
                break
            person = data[0]
            dept = data[1]
            departments[person] = dept

        return departments

if __name__ == '__main__':
    departments = parse_emails('./email-Eu-core-department-labels.txt')
    print(departments['3'])
    # Pickle the copurchases dictionary to save the data and run faster later
    file_Name = "email-departments-12-05"
    # open the file for writing
    picklefile = open(file_Name,'wb')
    # this writes the object a to the
    pickle.dump(departments, picklefile)
    # here we close the fileObject
    picklefile.close()

    print("Done")
