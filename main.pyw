import pytesseract
from PIL import Image
from PIL import ImageGrab
from win10toast import ToastNotifier
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        
file_path = "C:\\Projects\\data.txt"
log_path = "C:\\Projects\\main.log"

questions = []

try:
    with open(file_path, 'r', encoding="utf8") as file:
        lines = file.readlines()
        num_lines = len(lines)
        i = 0
        while i < num_lines:
            question = lines[i].strip()
            answers = []
            correct_answer = None
            i += 1
            while i < num_lines and not lines[i].strip().startswith("❌"):
                answer = lines[i].strip()
                if answer.endswith("✓"):
                    correct_answer = len(answers)
                    answer = answer[:-1]
                answers.append(answer)
                i += 1
            questions.append(Question(question, answers, correct_answer))
            i += 1

    logf = open(log_path, "w")
    toast = ToastNotifier()

    img = ImageGrab.grabclipboard()
    input_string = pytesseract.image_to_string(img, lang='rus+eng')
    
    best_match = process.extractOne(input_string, [q.question for q in questions], scorer=fuzz.ratio)
    
    index = [q.question for q in questions].index(best_match[0])
    
    if best_match:
        if questions[index].correct_answer is not None:
            toast.show_toast(best_match[0], questions[index].answers[questions[index].correct_answer], duration = 20, threaded = True)
        else:
            toast.show_toast("Did't find answer", best_match[0], duration = 20, threaded = True)
    else:
        toast.show_toast("No question", input_string, duration = 20, threaded = True)
  
    
except Exception as e:
    logf.write(str(e))