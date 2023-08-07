from lib.diary import Diary

def test_diary_counts_words_in_all_entries():
    diary = Diary()
    diary.add(FakeFourWordDiaryEntry())
    diary.add(FakeTwoWordDiaryEntry())
    assert diary.count_words() == 6

class FakeFourWordDiaryEntry():
    def count_words(self):
        return 4
    
class FakeTwoWordDiaryEntry():
    def count_words(self):
        return 2