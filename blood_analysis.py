# blood_analysis.py

def HDL_interface():
    # Input should be HDL=66
    print("HDL Interface")
    print("Please input the results in the following format: ")
    print("   HDL=## where ## is the numeric result")
    HDL_input = input("Result: ")
    HDL_result = HDL_input.split('=')
    if verify_entry(HDL_result):
        HDL_status = HDL_analysis(int(HDL_result[1]))
        print("HDL status is {}".format(HDL_status))
    else:
        print('Bad Entry')

def HDL_analysis(HDL_result):
    if HDL_result >= 60:
        return "Good"
    elif 40 <= HDL_result < 60:
        return "Borderline"
    else:
        return "Bad"

def verify_entry(HDL_result):
    if HDL_result[0] != "HDL":
        return False
    if not HDL_result[1].isnumeric():
        return False
    return True

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
    LDL_status=TotChol_analysis(int(TC_result[1]))
    print("Total Cholesterol status is {}".format(LDL_status))
    
def TotChol_analysis(TC_result):
    if TC_result < 200:
        return "Normal"
    elif 200 <= TC_result < 239:
        return "Borderline high"
    elif TC_result >= 239:
        return "High"

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