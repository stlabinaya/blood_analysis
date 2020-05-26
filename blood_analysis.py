# blood_analysis.py


def HDL_interface():
    # Input should be HDL=66
    print("HDL Interface")
    print("Please input the results in the following format: ")
    print("   HDL=## where ## is the numeric result")
    HDL_input = input("Result: ")
    HDL_result = HDL_input.split('=')
    HDL_status = HDL_analysis(int(HDL_result[1]))
    print("HDL status is {}".format(HDL_status))


def HDL_analysis(HDL_result):
    if HDL_result >= 60:
        return "Good"
    elif 40 <= HDL_result < 60:
        return "Borderline"
    else:
        return "Bad"


def LDL_interface():
    # Input should be LDL=130
    print("LDL Interface")
    print("Please input the results in the following format: ")
    print("   LDL=### where ### is the numeric result")
    LDL_input = input("Result: ")
    LDL_result = LDL_input.split('=')
    LDL_status = LDL_analysis(int(LDL_result[1]))
    print("LDL status is {}".format(LDL_status))


def LDL_analysis(LDL_result):
    if LDL_result >= 190:
        return "Very High"
    elif 160 <= LDL_result <= 189:
        return "High"
    elif 130 <= LDL_result <= 159:
        return "Borderline High"
    else:
        return "Normal"


def TotChol_interface():
    # Input should be TC=###
    print("Total Cholesterol Interface")
    print("Please input the results in the following format: ")
    print("   TC=### where ### is the numeric result")
    TC_input = input("Result: ")
    TC_result = TC_input.split("=")
    LDL_status = TotChol_analysis(int(TC_result[1]))
    print("Total Cholesterol status is {}".format(LDL_status))


def TotChol_analysis(TC_result):
    if TC_result < 200:
        return "Normal"
    elif 200 <= TC_result < 239:
        return "Borderline high"
    elif TC_result >= 239:
        return "High"


def slope(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    m = (y2 - y1) / (x2 - x1)
    b = (y1 - m) * x1
    return m, b


def newPoint(m, b, x):
    y = m * x + b
    return y

def line_generation(p1, p2, x):
    return newPoint(slope(p1, p2)[0], slope(p1, p2)[1], x)


def interface():
    print("My Blood Analysis Calculator")
    keep_running = True
    while keep_running:
        print("\nOptions: ")
        print("1-HDL analysis")
        print("2-LDL analysis")
        print("3-Total Cholesterol analysis")
        print("9-Quit")
        choice = input("Choose an option: ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            HDL_interface()
        elif choice == '2':
            LDL_interface()
        elif choice == '3':
            TotChol_interface()


if __name__ == "__main__":
    interface()
