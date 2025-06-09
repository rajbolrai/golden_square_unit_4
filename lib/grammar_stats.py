class GrammarStats:
    def __init__(self):
        self._percentage = 0
        self._pass_check = 0
        self._fail_check = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if type(text) != str:
            raise TypeError("Error: only string accepted")
        elif text == '':
            raise Exception("Error: cannot accept empty sentence")
        
        if text[0].isupper() and text[-1] in ['.', '?', '!']:
            self._pass_check += 1
            return True
        self._fail_check +=1
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        curr_check_count = self._pass_check + self._fail_check
        if curr_check_count == 0:
            raise ZeroDivisionError("Error: cannot get percentage without checking first")
        curr_percentage = int((self._pass_check/curr_check_count) * 100)
        return curr_percentage
