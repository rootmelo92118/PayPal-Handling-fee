import numpy as np

fixedExpense = {
    "AUD": ["澳币（澳大利亚）", 0.3],
    "BRL": ["巴西里拉（巴西）", 0.6],
    "CAD": ["加币（加拿大）", 0.3],
    "CZK": ["捷克克朗（捷克）", 10],
    "DKK": ["丹麦克朗（丹麦）", 2.6],
    "EUR": ["欧元（欧盟）", 0.35],
    "HKD": ["港币（中华人民共和国香港特别行政区）", 2.35],
    "HUF": ["匈牙利福林（匈牙利）", 90],
    "ILS": ["以色列谢克尔（以色列）", 1.2],
    "JPY": ["日圆（日本）", 40],
    "MYR": ["马来西亚令吉（马来西亚）", 2],
    "MXN": ["墨西哥披索（墨西哥）", 4],
    "TWD": ["新台币（中华民国台湾省）", 10],
    "NZD": ["新西兰币（新西兰）", 0.45],
    "NOK": ["挪威克朗（挪威）", 2.8],
    "PHP": ["菲律宾披索（菲律宾）", 15],
    "PLN": ["波兰兹罗提（波兰）", 1.35],
    "RUB": ["俄罗斯卢布（俄罗斯）", 10],
    "SGD": ["新加坡币（新加坡）", 0.5],
    "SEK": ["瑞典克朗（瑞典）", 3.25],
    "CHF": ["瑞士法郎（瑞士）", 0.55],
    "THB": ["泰铢（泰国）", 11],
    "GBP": ["英镑（英国）", 0.2],
    "USD": ["美元（美国）", 0.3]
}

def round_v2(num, decimal):
    num = np.round(num, decimal)
    num = float(num)
    return num

def calculator(currency):
    while True:
        inputData = input(str(currency) + "付款金额（切换货币请输入exit）: ")
        if inputData.lower() == "exit":
            break
        else:
            try:
                if "." in inputData:
                    sender = float(inputData)
                else:
                    sender = int(inputData)
                parameter1 = sender / 100 * 4.4
                parameter2 = sender - parameter1 - fixedExpense[currency][1]
                if parameter2 < 0:
                    print(inputData + " - " + inputData + " × 4.4% - " + str(fixedExpense[currency][1]) + " = " + str(parameter2) + " \n标准化数据: 0 " + currency + "\n")
                else:
                    print(inputData + " - " + inputData + " × 4.4% - " + str(fixedExpense[currency][1]) + " = " + str(parameter2) + " \n标准化数据: " + str(round_v2(parameter2, 2)) + " " + currency + "\n")
            except Exception as e:
                print(e)
                print("输入错误，请重新输入\n")

while True:
    for i in fixedExpense:
        print(str(i) + " " + fixedExpense[i][0])
    inputData = input("请输入币别（退出请输入exit）: ")
    if inputData.lower() == "exit":
        break
    else:
        if inputData.upper() in fixedExpense:
            calculator(inputData.upper())
        else:
            print("输入错误，请重新输入\n")
    