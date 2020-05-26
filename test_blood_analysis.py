def test_HDL_analysis ():
    from blood_analysis import HDL_analysis
    answer = HDL_analysis(70)
    expected = "Good"
    assert answer == expected #if assert true, test will pass or else test will fail

def test_HDL_analysis_borderline():
    from blood_analysis import HDL_analysis
    answer = HDL_analysis(45)
    expected = "Borderline"
    assert answer == expected

def test_HDL_analysis_bad():
    from blood_analysis import HDL_analysis
    answer = HDL_analysis(20)
    expected = "Bad"
    assert answer == expected

def test_LDL_analysis():
    from blood_analysis import LDL_analysis
    answer = LDL_analysis(120)
    expected = "Normal"
    assert answer == expected

def test_line_generation():
    from blood_analysis import line_generation
    answer = line_generation((1,1), (3,3), 2)
    expected = 2
    assert answer == expected


def test_slope():
    from blood_analysis import slope
    m, b = slope((1,1),(4,4))
    assert m == 1
    assert b == 0