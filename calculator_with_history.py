
HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE,'r')
    lines = file.readlines()
    if len(lines) == 0:
       print("No history found")
    else : 
       for line in reversed(lines):
           print(line.strip())
    file.close()


def clear_history():
    file = open(HISTORY_FILE,'w')
    file.close()
    print("History cleared")


def save_to_history(expression,result):
    file = open(HISTORY_FILE,'a')
    file.write(expression + " = " + str(result) + "\n")
    file.close()

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
       print("Invalid input. Use format value operator value2 . e.g : 8 + 8 ")
       return
    
    num = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
       result = num + num2
    elif op == "-":
        if num > num2 : 
           result = num2 - num 
        else:
           result = num - num2
    elif op == "*":
        result = num * num2
    elif op == "/":
        if num2 == 0:
           print("Number can not divide by 0")
           return
        result = num / num2
    

    if int(result) == result:
        result = int(result)
    print("Result :",result)
    save_to_history(user_input,result)


def main():
    print("---- Simple Calculator ---- ")
    while True :
        user_input = input("Enter Calculator (+,-,*,/) along with values  or type (history ,clear ,exit) : ").strip()
        if user_input == "history":
             show_history()
        elif user_input == "clear":
             clear_history()
        elif user_input == "exit":
            print("Good Bye")
            break 
        else:
            calculator(user_input)

main()
        