import sys
import smog_index
import flesch
import gunning
import dale_chall
from textstat.textstat import textstat

def Ans (a) :
    if a == 1:
        return flesch.flesch_reading_ease(InputFileText.read())
    elif a == 2:
        return smog_index.smog_index(InputFileText.read())
    elif a == 3:
        return gunning.gunning_fog(InputFileText.read())
    elif a == 4 :
        return dale_chall.dale_chall_readability_score(InputFileText.read()) 

if __name__ == "__main__" :
    if len(sys.argv) != 3 :
        print("Usage: python main.py [PATH_TO_FILE] [OPTIONS]")
        print("[OPTIONS]:\n1. Flesch Reading Ease")
        print("2. Smog Index")
        print("3. Gunning Fog")
        print("4. Dale Chall Readability Score")
        sys.exit()
    InputFileText = open(sys.argv[1], 'r', encoding="utf-8")
    print(sys.argv[2])
    print(Ans(int(sys.argv[2])))