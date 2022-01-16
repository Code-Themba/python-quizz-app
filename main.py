from Quizlet import Questions


def do_quiz():
    score = 0
    chances = 3
    question_number = 0

    while chances > 0 or question_number < len(Questions)-1:
        if question_number == len(Questions):
            break

        print(f"{Questions[question_number]['question']}\n {Questions[question_number]['answer_choices']}")
        user_answer = input("Enter Your Answer Here: ").capitalize()
        if user_answer == Questions[question_number]['correct_answer']:
            score += Questions[question_number]["points"]
            print('Correct!! Good job.')
            print(f'The correct answers is {Questions[question_number]["correct_answer"]} ')
            print(f'You earned {Questions[question_number]["points"]} points')
        elif user_answer != Questions[question_number]['correct_answer']:
            score = score
            print('Oh no... Sorry that answer is not correct.')
            print(f'The correct answer is {Questions[question_number]["correct_answer"]} and you entered {user_answer}')
            print(f'You earned no points.')
            chances -= 1

        print()

        question_number += 1

    if score >= 25:
        print(f'You did great and scored {score}. Keep up the good work.')
    else:
        print(f'You only scored {score}. But don\'t give up, you can do it.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    do_quiz()
