#ProcessData.py
#Name:antonio perez
#Date:april 5
#Assignment:lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')
  


  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data [0]
    last = data [1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idNum)
    major_year = makeMajor(major, year)

    output = last + "," + first + "," + student_id + major_year + "\n"
    outFile.write(output)

    #student_id = makeID(data[0], data[1], data[3])
    print(student_id)



  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, Last, idNum):
  #print(first, last, idNum)
  idLen = len (idNum)

  while len(last) < 5:
    last = last + "X"





  userID = first[0] + last + idNum[ idLen - 3: ]
  #print(userID)
  return userID
def makeMajoryear(major, year):
  majorPart = major[0:3]
  if year == "Freshman":
    yearPart == "FR"
  elif year == "Sophmore":
    yearPart == "SO"
  elif year == "Junior":
    yearPart == "JR"
  elif year == "Senior":
    yearPart == "SR"
  return majorPart + "," + yearPart 
  

if __name__ == '__main__':
  main()
