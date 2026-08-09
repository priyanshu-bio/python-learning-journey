# for every correct answer 1 marks were given
# 1 marks will be detected for every wrong answer


xs = (('what is the largest planet in our solar system?'),
     ('what is the basic unit of life?'),
     ('largest organ in human body is'),
     ('which planet has most moon in our solar system?'))
ys = (('A. mars', 'B. jupiter', 'C venus', 'D. earth'),
     ('A. organ', 'B. cell', 'C. tissue', 'D. none'),
     ('A. brain', 'B. lungs', 'C. skin', 'D. kidney'),
     ('A. mars', 'B. jupiter', 'C venus', 'D. earth'))
answer = ['B', 'B', 'C', 'B']
guesses = []
score = 0
question_no = 0



for x in xs:
    
    print('-------')
    print(x)
    for y in ys[question_no]:
        print(y)
    guess = input('enter your answer as (A, B. C. D) :  ').upper()
    guesses.append(guess)




    if guess == answer[question_no]:
        score += 1
        print('correct')
         
    else:
        score -= 1
        print('incorrect')
        print(f'the correct answer is : {answer[question_no]}')
    question_no += 1


    
print('----------########---------')
print("-----------result----------")
print('----------########---------')

print('guesses:-')
for guess in guesses:
    print(guess, end=', ')
print()    

print('answer:-')
for answers in answer:
    print(answers, end=', ')
print()

print(input(f'your total score is : {score} or {score/4*100}%' ))
              
   
