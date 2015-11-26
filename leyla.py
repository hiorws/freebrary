__author__ = 'ozgur'
from time import sleep

main_quest_dict = {'q1': 'Hic Ahmed Arif siiri okumus mudur?',
                   'q2': 'Benimle gun icinde "Minnet Eylemem" dinler mi?',
                   'q3': 'Whatsapp\'siz yasabilir mi?',
                   'q4': 'Saatlerce "Murat Yilmazyildirim" dinlersem benden sikilir mi?',
                   'q5': 'XXXXX'}

enter_helper_text = "Evet icin 'e' , hayir icin, 'h' giriniz:"


def ask_questions():
    for quest_no, quest_text in main_quest_dict.items():
        print quest_text
        answer = raw_input(enter_helper_text)
        if answer == 'e':
            pass
        else:
            finish_decision()
    passed_test()


def passed_test():
    print "Sonuc hesaplaniyor. Lutfen bekleyiniz..."
    sleep(2.5)
    print "Sonuc: KACIRMA!"


def finish_decision():
    print "Hanimefendi sizin icin cok uygun degil sevgili Ozgur."
    exit()


def main():
    print "Welcome to the Leyla Finder."
    ask_questions()


if __name__ == '__main__':
    main()
