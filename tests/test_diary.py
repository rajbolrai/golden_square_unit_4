from lib.Diary import * 


""" 
Check to see if the title and content is of type string
return invalid type error
"""

"""
Given a title and content
format will return a string with the corrected format
"""
def test_diary_format():
    diary_entry = DiaryEntry("Friday", "Ready to relax")
    assert diary_entry.format() == "Friday: Ready to relax"


"""
Given a title and content
format will return a string with the corrected format
"""
def test_given_valid_entry_output_correct_word_count():
    diary_entry = DiaryEntry("Thursday", "I was trying my hardest to 4' it's go-go-go go-go to-do let's stay locked in.?")
    words_to_read = diary_entry.count_words()
    assert words_to_read == "1 min"
    
    assert diary_entry.count_words() == 15

""" Given their wpm 
return the time taken to read the contents at the given wpm in minutes"""