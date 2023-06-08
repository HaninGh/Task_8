class Subject:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"Subject({self.name}, {self.mark})"

subject = Subject("math", 90)

print(subject)