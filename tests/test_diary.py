from lib.Diary import * 
import pytest

""" 
Check to see if the title and content is of type string
return invalid type error
"""
def test_type_of_tile_content_is_string():
    with pytest.raises(TypeError) as e:
        DiaryEntry(1,2)
    error_message = str(e.value)
    assert error_message == "Error: invalid type. Expected String"
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
    assert diary_entry.count_words() == 15

""" Given their wpm 
return the time taken to read the contents at the given wpm in minutes"""

def test_given_valid_entry_output_correct_word_per_minute():
    diary_entry = DiaryEntry("Thursday", 
                                "one two three four five six seven eight nine ten "
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                
                                + "one two three four five six seven eight nine ten "                                 
                                + "one two three four five six seven eight nine ten "                                
                                )
    word_per_minute = diary_entry.reading_time(100)
    assert word_per_minute == "2.01 mins"
    
    
def test_can_read_one_chunk():
    diary_entry = DiaryEntry("Thursday", """
                            "one two three four five six seven eight nine ten 
                            one two three four five six seven eight nine ten                                 
                            one two three four five six seven eight nine ten                                 
                            one two three four five six seven eight nine ten                                 
                            one two three four five six seven eight nine ten                                 
                            one two three four five six seven eight nine ten                                 
                            one two three four five six seven eight nine ten                                 
                            one two three four five six seven eight nine ten                                 
                            one two three four five six seven eight nine ten                             
                            one two three four five six seven eight nine ten """                      
                            )
    curr_reading_chunk = diary_entry.reading_chunk(5,5)
    #print(diary_entry._content_words)
    assert curr_reading_chunk == """one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five"""
    
    
def test_can_read_multiple_chunks():
    diary_entry = DiaryEntry("Thursday", """
                            "Welcome to my world. You will be greeted by the 
                            unexpected here and your mind will be challenged and expanded
                            in ways that you never thought possible. That is if
                            you are able to survive."""                      
                            )
    diary_entry.reading_chunk(5,2)
    diary_entry.reading_chunk(5,3)
    diary_entry.reading_chunk(5,3)
    curr_reading_chunk = diary_entry.reading_chunk(5,2)
    assert curr_reading_chunk == """Welcome to my world. You will be greeted by the"""