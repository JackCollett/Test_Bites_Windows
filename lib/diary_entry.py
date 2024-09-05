class Diary():
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents
        self._read_so_far = 0

    def format(self):
        return f"{self._title}: {self._contents}"
    
    def count_words(self):
        return len(self._contents.split())
    
    def reading_time(self, wpm):
        words = self.count_words()
        return round(words / wpm)
    
    def reading_chunk(self, wpm, minutes):
        number_of_words = wpm * minutes
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + number_of_words
        chunk = " ".join(self._contents.split()[chunk_start:chunk_end])
        self._read_so_far += number_of_words
        return chunk