import string
import re

class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        if type(title) != str or type(contents) != str:
            raise TypeError("Error: invalid type. Expected String")
        
        self._title = title
        self._contents = contents
        self._content_words = []
        self.curr_word_count = 0
        

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        formatted_entry = f"{self._title}: {self._contents}"
        return formatted_entry

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        # title_only_words = [i.strip(string.punctuation) for i in self._title.split() if i.strip(string.punctuation).isalpha()]
        # contents_only_words = [i.strip(string.punctuation) for i in self._contents.split() if i.strip(string.punctuation).isalpha()]
        title_words = re.findall(r"\b[a-zA-Z']+(?:-[a-zA-Z']+)*\b", self._title)
        content_words = re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?(?:-[a-zA-Z'.?!]+)*(?:[?!.]+)?(?!\w)", self._contents)
        self._content_words = content_words
        print(self._content_words)
        return len(title_words) + len(content_words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        
        time_taken_to_read = round(self.count_words()/wpm,2)
        return f"{time_taken_to_read} mins"
        

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        string_to_return = ""
        self.count_words()
        word_count = len(self._content_words)
        
        for i in range(wpm * minutes):
            if self.curr_word_count == word_count:
                self.curr_word_count = 0
                break
            string_to_return += self._content_words[self.curr_word_count] + " "
            self.curr_word_count += 1
        return string_to_return.strip()