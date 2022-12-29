import data
import re
import pandas as pd

dates1 = []
descriptions1 = []
amounts1= []
dates2 = []
descriptions2 = []
amounts2= []

websites = []
email = []
phone_numbers = []
max_amount = 0
min_amount = 0
minner = ''
maxxer = ''

def dateValidator(inp: str):
    date_pattern = r"^(0?[1-9]|1[0-2])[^\w\d\r\n:](0?[1-9]|[12]\d|30|31)[^\w\d\r\n:](\d{4}|\d{2})$"
    return re.search(date_pattern, inp)

def currencyValidator(inp: str):
    currency_pattern = r"^(\$|\-)*?([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(.[0-9][0-9])?$"
    return re.search(currency_pattern, inp)

def websiteValidator(inp: str):
    website_pattern = r"^((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+(&[a-zA-Z0-9_]+=\w+)*)?\/?$"
    return re.search(website_pattern, inp)

def phoneValidator(inp: str):
    phone_pattern = r"(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}"
    return re.search(phone_pattern, inp)

def emailValidator(inp: str):
    email_pattern = r"/^\S+@\S+\.\S+$/"
    return re.search(email_pattern, inp)
    
f = data.a
flag = 0
l = []
for i in f:
    if(flag == 0):
        if(dateValidator(i)):
            temp = i.split('/')
            l.append(i)
            desc = ""
            flag = 1
            val = 1
        elif(websiteValidator(i)):
            websites.append(i)
        elif(phoneValidator(i)):
            phone_numbers.append(re.search(r"(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}", i).group())
        elif(emailValidator(i)):
            email.append(i)

    elif(flag == 1):
        if(currencyValidator(i) and val != 1):
            val = 0
            flag = 0
            l.append(desc)
            desc = ''
            l.append(i)
            if(l[2][0] == "-"):
                print("withdrawal: ",l)
                dates2.append(l[0])
                descriptions2.append(l[1])
                amounts2.append(l[2])
                newStr = re.sub(r'[^0-9]', '', i)
                if int(newStr) > min_amount:
                    min_amount = int(newStr)
                    minner = i
                
            else:
                print("deposit: ",l)
                dates1.append(l[0])
                descriptions1.append(l[1])
                amounts1.append(l[2])
                newStr = re.sub(r'[^0-9]', '', i)
                if int(newStr) > max_amount:
                    max_amount = int(newStr)
                    maxxer = i
                
            l = []
            flag = 0
        else:
            val += 1
            desc = desc + i + " "


df1 = pd.DataFrame({'Date': dates1,'Description': descriptions1, 'Amount Deposited': amounts1 })
df2 = pd.DataFrame({'Date': dates2,'Description': descriptions2, 'Amount Withdrawn': amounts2 })
df3 = pd.DataFrame({'Keys': ["Website", "Email", "Phone numbers", "Max Amount", "Min Amount"],'Value': [','.join(websites),','.join(email), ','.join(phone_numbers), maxxer, minner] })
with pd.ExcelWriter("task2Output.xlsx") as writer:
    df1.to_excel(writer, sheet_name='Deposits', index=False)
    df2.to_excel(writer, sheet_name='Withdrawals', index=False)
    df3.to_excel(writer, sheet_name='Insight', index=False)