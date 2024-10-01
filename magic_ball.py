import sys, time, random

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
def input_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    return input()

print_slow("\nHello, I'm a toy invented in the USA in the 1950s" 
          "\nIt works like this: you ask questions like “Will I ever be rich and famous?”, then you get one of 10 different answers appears at random. ")

print()
print_slow("Let`s start.")
print()
name = input_slow("\nWhat's your name? ")

while True:
    question = input_slow("\nWhat do you want to know? ",)
    
    print_slow("\nThinking...")
    time.sleep(2)  # Pausa de 2 segundos para simular processamento

    answer = ""

    random_number = random.randint(1, 15)

    if random_number == 1:
        answer = "Yes - definitely."
    elif random_number == 2:
        answer = "It is decidedly so."
    elif random_number == 3:
        answer = "Without a doubt."
    elif random_number == 4:
        answer = "Reply hazy, try again."
    elif random_number == 5:
        answer = "Ask again later."
    elif random_number == 6:
        answer = "Better not tell you now."
    elif random_number == 7:
        answer = "My sources say no."
    elif random_number == 8:
        answer = "Outlook not so good."
    elif random_number == 9:
        answer = "Very doubtful"
    elif random_number == 10:
        answer = "Yes, belive in yourself."
    elif random_number == 11:
        answer = "No, sorry."
    elif random_number == 12:
        answer = "Maybe you shoul ask latter."
    elif random_number == 13:
        answer = "Try other question."
    elif random_number == 14:
        answer = "Don`t ask me that."
    elif random_number == 15:
        answer = "Yes, now, go get some pizza!."
    else:
        answer = "Error."

    print_slow(f"\n{name} asks: {question}")
    print()
    time.sleep(1)  # Pausa de 1 segundo antes da resposta
    print_slow(f"\nMagic 8 Ball's answer: {answer}")

    # Pergunta se o usuário quer continuar
    again = input_slow("\nDo you want to ask another question? (yes/no): ").lower()
    if again != "yes":
        print_slow("\nGoodbye!")
        break
