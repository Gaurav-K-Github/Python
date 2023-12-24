import random

animals = ['elephant','bear','cheetah','giraffe','wolf','tiger','penguin',
          'rabbit','lion','monkey','rhinoceros','sheep','kangaroo','zebra']
fruits = ['apple','banana','grapes','mango','lime','watermelon','jackfruit',
          'guava','orange','papaya','pear','peach','pomegranate','strawberry']
stationary = ['pencil','eraser','sharpener','envelope','paper','stapler','folder',
              'marker','in kpot','calculator','glue','notebook','scissors','ruler']
countries = ['argentina', 'brazil', 'canada', 'denmark', 'egypt', 'france', 'germany',
             'india', 'japan', 'kenya', 'mexico', 'norway', 'portugal', 'russia']
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink',
          'brown', 'black', 'white', 'gray', 'silver', 'gold', 'maroon']

while 1:
    words = animals + fruits + stationary + countries + colors
    random_word = random.choice(words)
    print("WHAT'S THE WORD?")
    if random_word in animals:
        print("Hint:It is an animal")
    elif random_word in fruits:
        print('Hint:It is a fruit')
    elif random_word in countries:
        print('Hint:It is a country')
    elif random_word in colors:
        print('Hint:It is a color')
    else:
        print("Hint:It is a stationary item")

    user_guesses = ''
    chances = 5

    while chances>0:
        wrong_guesses=0
        for letter in random_word:
            if letter in user_guesses:
                print(letter, end=' ')
            else:
                wrong_guesses+=1
                print('_', end=' ')
        if wrong_guesses==0:
            print('\nYOU WIN. The word is',random_word)
            again = input('Press y to play again, n to quit ')
            if again == 'y':
                break
            else:
                quit()
