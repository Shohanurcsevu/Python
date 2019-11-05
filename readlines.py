

fo = open("a.txt", "r")


print("Name of the file: ", fo.name)
line = fo.readlines()


def namata(n):

  for i in range(1, 11):
     print(str(int(n))+'x'+str(int(i))+'=' + str(int(n)*int(i)))
     k=str(int(n)*int(i)) 
     file= open("b.txt", "a")
     file.write(f'{int(n)} x {int(i)} = {k}\n')
     file.close()

    
     
 
  return k
   



for j in range(len(line)):
  namata(line[j])
