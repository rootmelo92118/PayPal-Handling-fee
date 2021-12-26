import numpy as np

fixedExpense = {
    "AUD": ["澳幣（澳大利亞）", 0.3],
    "BRL": ["巴西里拉（巴西）", 0.6],
    "CAD": ["加幣（加拿大）", 0.3],
    "CZK": ["捷克克朗（捷克）", 10],
    "DKK": ["丹麥克朗（丹麥）", 2.6],
    "EUR": ["歐元（歐盟）", 0.35],
    "HKD": ["港幣（中華人民共和國香港別行政區）", 2.35],
    "HUF": ["匈牙利福林（匈牙利）", 90],
    "ILS": ["以色列謝克爾（以色列）", 1.2],
    "JPY": ["日圓（日本）", 40],
    "MYR": ["馬來西亞令吉（馬來西亞）", 2],
    "MXN": ["墨西哥披索（墨西哥）", 4],
    "TWD": ["新台幣（中華民國台灣省）", 10],
    "NZD": ["紐西蘭幣（紐西蘭）", 0.45],
    "NOK": ["挪威克朗（挪威）", 2.8],
    "PHP": ["菲律賓披索（菲律賓）", 15],
    "PLN": ["波蘭茲羅提（波蘭）", 1.35],
    "RUB": ["俄羅斯盧布（俄羅斯）", 10],
    "SGD": ["新加坡幣（新加坡）", 0.5],
    "SEK": ["瑞典克朗（瑞典）", 3.25],
    "CHF": ["瑞士法郎（瑞士）", 0.55],
    "THB": ["泰銖（泰國）", 11],
    "GBP": ["英鎊（英國）", 0.2],
    "USD": ["美元（美國）ㄉ", 0.3]
}

def round_v2(num, decimal):
    num = np.round(num, decimal)
    num = float(num)
    return num

def calculator(currency):
    while True:
        inputData = input(str(currency) + "付款金額（切換貨幣請輸入exit）: ")
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
                    print(inputData + " - " + inputData + " × 4.4% - " + str(fixedExpense[currency][1]) + " = " + str(parameter2) + " \n標準化數據: 0 " + currency + "\n")
                else:
                    print(inputData + " - " + inputData + " × 4.4% - " + str(fixedExpense[currency][1]) + " = " + str(parameter2) + " \n標準化數據: " + str(round_v2(parameter2, 2)) + " " + currency + "\n")
            except Exception as e:
                print(e)
                print("輸入錯誤，請重新輸入\n")

while True:
    for i in fixedExpense:
        print(str(i) + " " + fixedExpense[i][0])
    inputData = input("請輸入幣別（退出請輸入exit）: ")
    if inputData.lower() == "exit":
        break
    else:
        if inputData.upper() in fixedExpense:
            calculator(inputData.upper())
        else:
            print("輸入錯誤，請重新輸入\n")
    