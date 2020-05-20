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

def interface():
    print("My Blood Analysis Calculator")
    keep_running = True
    while keep_running:
        print("\nOptions: ")
        print("1-HDL analysis")
        print("9-Quit")
        choice = input("Choose an option: ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            HDL_interface()

if __name__ == "__main__":
    interface()