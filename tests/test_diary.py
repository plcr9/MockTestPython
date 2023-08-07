from lib.diary import Diary

def test_diary_counts_words_in_all_entries():
    diary = Diary()
    diary.add(FakeFourWordDiaryEntry())
    diary.add(FakeTwoWordDiaryEntry())
    assert diary.count_words() == 6

def test_diary_entry_counts_words_in_a_single_entry():
    diary = Diary()
    diary.add(FakeFourWordDiaryEntry())
    assert diary.count_words() == 4

class FakeFourWordDiaryEntry():
    def count_words(self):
        return 4
    
class FakeTwoWordDiaryEntry():
    def count_words(self):
        return 2