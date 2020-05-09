def add_homework():
    homework = input("add homework:- ")
    file = open('play.txt', 'a')
    file.write(f'{homework}\n')

def list_homework():
    file = open('play.txt', 'r+') 
    read = file.read()
    print(read)
def turncate():
    import random
    num = random.randint(100000,999999)
    file = open("play.txt", 'w+')
    print(num)
    ent = input("enter the number shown above that you want to delete your homework:- ")
    if ent == num:
        file.truncate(0)




input_ = input(">>> ")

if input_ == 'add':
    add_homework()
    file.close()
    print("homework added")
elif input_ == 'list':
    list_homework()
    file.close()
elif input_ == 'del':
    turncate()
    print("contents of file deleted")
    file.close()
    
