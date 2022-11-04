class Book:

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.check_out = False
    
    def check_out_status(self, book_title, status):
        if book_title == self.title:
            self.check_out = status
    
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