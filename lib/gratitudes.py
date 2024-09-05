class Gratitudes():
    def __init__(self):        
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        string = ""
        for i in self.gratitudes[:-1]:
            string += i + ", "
        string += f"and {self.gratitudes[-1]}"
        return f"I am grateful for: {string}."