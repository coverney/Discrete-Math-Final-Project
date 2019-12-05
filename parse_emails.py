import io
import pickle

# Read throrugh text file line by line
# Each line has the ID number of the sender, separated by a space from the number ID of the receiver

def parse_emails(filename):
    with open(filename) as fp:
        line = fp.readline()
        copurchases = {}
        cnt = 1

        while line:
            if cnt % 1000 == 0:
                print(cnt)
            line = fp.readline()
            cnt += 1
            data = line.split()
            if len(data) < 2:
                break

            sender = data[0]
            receiver = data[1]
            if sender == receiver:
                continue
            if sender in copurchases:
                if receiver in copurchases[sender]:
                    continue
                copurchases[sender].extend([receiver])
            else:
                copurchases[sender] = [receiver]
            if receiver in copurchases:
                if sender in copurchases[receiver]:
                    continue
                copurchases[receiver].extend([sender])
            else:
                copurchases[receiver] = [sender]

        return copurchases

if __name__ == '__main__':
    copurchases = parse_emails('./email-Eu-core.txt')
    print(copurchases['3'])
    # Pickle the copurchases dictionary to save the data and run faster later
    file_Name = "copurchases-emails-12-05"
    # open the file for writing
    picklefile = open(file_Name,'wb')
    # this writes the object a to the
    pickle.dump(copurchases, picklefile)
    # here we close the fileObject
    picklefile.close()

    print("Done")
