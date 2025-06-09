from lib.grammar_stats import *
import pytest

"""
Given invalid type in this case a int
raise type error
"""
def test_given_invalid_type_output_type_error():
    with pytest.raises(TypeError) as err:
        obj_grammar_stat = GrammarStats()
        obj_grammar_stat.check(123)
    error_message = str(err.value)
    assert error_message == "Error: only string accepted"


"""
Given empty string 
raise error
"""
def test_given_empty_string_output_error():
    with pytest.raises(Exception) as err:
        obj_grammar_stat = GrammarStats()
        obj_grammar_stat.check('')
    error_message = str(err.value)
    assert error_message == "Error: cannot accept empty sentence"

"""
Given a sentence that starts with a capitalised first letter and ends with a full-stop
output True
"""
def test_given_sentence_that_begins_with_capital_letter_and_ends_with_full_stop_output_true():
    obj_grammar_stat = GrammarStats()
    b_valid_grammar = obj_grammar_stat.check("Hello, welcome to the world of earthir.")
    assert b_valid_grammar == True
    
"""
Given a sentence that starts with a capitalised first letter, but does not end with a valid ending punctuation mark
output False
"""
def test_given_sentence_that_begins_with_capital_letter_and_does_not_end_correct_punctuation_mark_output_false():
    obj_grammar_stat = GrammarStats()
    b_valid_grammar = obj_grammar_stat.check("How long are you here for")
    assert b_valid_grammar == False

"""
Given a sentence that starts with a lowercase first letter and ends with a valid ending punctuation mark
output False
"""
def test_given_sentence_that_begins_with_lowercase_letter_and_ends_with_correct_punctuation_mark_output_false():
    obj_grammar_stat = GrammarStats()
    b_valid_grammar = obj_grammar_stat.check("how long are you here for?")
    assert b_valid_grammar == False

""" 
Given 0 checks
raise an error division by zero
"""
def test_given_zero_checks_output_zero():
    obj_grammar_stat = GrammarStats()
    with pytest.raises(ZeroDivisionError) as err:
        obj_grammar_stat.percentage_good()
    error_message = str(err.value)
    assert error_message == "Error: cannot get percentage without checking first"
    

""" 
Given 5 checks with 3 passing and 2 failing
return 60 percent pass percentage
"""
def test_given_3_passing_and_2_failing_checks_output_60_percentage():
    obj_grammar_stat = GrammarStats()
    obj_grammar_stat.check("Hello, how was your travel?")
    obj_grammar_stat.check("Glad to hear that")
    obj_grammar_stat.check("And welcome to erithnir.")
    obj_grammar_stat.check("Good luck!")
    obj_grammar_stat.check("Hunter")
    percentage = obj_grammar_stat.percentage_good()
    assert percentage == 60
    
""" 
Given 9 checks with 3 passing and 6 failing
return 33 percent pass percentage
"""
def test_given_3_passing_and_6_failing_checks_output_33_percentage():
    obj_grammar_stat = GrammarStats()
    obj_grammar_stat.check("Hello, how was your travel?")
    obj_grammar_stat.check("Glad to hear that")
    obj_grammar_stat.check("And welcome to erithnir.")
    obj_grammar_stat.check("Good luck!")
    obj_grammar_stat.check("Hunter")
    obj_grammar_stat.check("Hunter")
    obj_grammar_stat.check("Hunter")
    obj_grammar_stat.check("Hunter")
    obj_grammar_stat.check("hunter")
    
    percentage = obj_grammar_stat.percentage_good()
    assert percentage == 33
    