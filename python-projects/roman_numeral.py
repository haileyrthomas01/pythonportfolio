numeral_input = input("Please enter the roman numerals you want to convert: ")

def roman_to_int(numeral):
    finalAns = 0

    for i in numeral:
        if i == "M":
            finalAns += 1000
        elif i == "D":
            finalAns += 500
        elif i == "C":
            finalAns += 100
        elif i == "L":
            finalAns += 50
        elif i == "X":
            finalAns += 10
        elif i == "V":
            finalAns += 5
        elif i == "I":
            finalAns += 1
        if "CM" in numeral:
            finalAns += 900
            numeral = numeral.replace("CM", "")
        if "CD" in numeral:
            finalAns += 400
            numeral = numeral.replace("CD", "")
        if "XC" in numeral:
            finalAns += 90
            numeral = numeral.replace("XC", "")
        if "XL" in numeral:
            finalAns += 40
            numeral = numeral.replace("XL", "")
        if "IX" in numeral:
            finalAns += 9
            numeral = numeral.replace("IX", "")
        if "IV" in numeral:
            finalAns += 4
            numeral = numeral.replace("IV", "")

    print("The roman numerals you entered translates to: " + str(finalAns) + ".")

roman_to_int(numeral_input)