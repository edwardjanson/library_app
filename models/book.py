from datetime import datetime

class Book:

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = False
        self.check_out_logs = []
    
    def update_check_out(self, status):
        # Update the check-out status
        self.is_checked_out = True if "checked-out" in status else False

        # Record a new check-out log if the book is checked-out
        if self.is_checked_out:
            self.new_checkout_log()
    
    def hyphenate_title(self):
        # Replace all non alphanumerical characters with a hyphen
        hyphenated_title = [char.replace(char, "-") if not char.isalnum() else char for char in self.title]

        # Remove any starting, trailing, and consecutive hyphens
        index = 0
        while index != len(hyphenated_title):
            if hyphenated_title[0] == "-":
                hyphenated_title.pop(0)
                index -= 1
            elif hyphenated_title[-1] == "-":
                hyphenated_title.pop(-1)
                index -= 1
            elif index != 0 and hyphenated_title[index] == "-" and hyphenated_title[index - 1] == "-":
                print(hyphenated_title)
                hyphenated_title.pop(index)
                index -= 1
            else:
                index += 1

        return "".join(hyphenated_title)
    
    def new_checkout_log(self):
        # Add a new dated and timed check-out log
        date_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        self.check_out_logs.insert(0, date_time)

