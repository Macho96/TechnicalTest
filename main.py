#const
UI_MSG= "Enter some number\n"
ERROR_MSG = "The input need a number, try again"
RESULT_MSG = "Close Path Result: "
DIGITLIST_CLOSEPATH=[0,4,6,9]
#variables
user_inputNumber = 0
#function
def close_path(input_number):
  closepath_result = 0 #result of sum close path
  for digit in str(input_number): #iterate every digit in the number
    if int(digit) in DIGITLIST_CLOSEPATH: #check current digit in case list to add 1
      closepath_result += 1 
    elif int(digit) == 8: #check current digit are 8 to add 2
      closepath_result += 2
  return closepath_result
#execute function
while True:
  try:
    user_inputNumber = int(input(UI_MSG)) #validate that input is a number
    break
  except ValueError:
    print(ERROR_MSG) #print error message
print(RESULT_MSG+str(close_path(user_inputNumber)))#call function and print result