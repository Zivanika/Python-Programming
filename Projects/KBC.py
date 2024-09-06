#PROGRAMMED BY AKSHAT JAISWAL
questions = [
    "According to legend, what do vampires drink?\n(a) Blood\n(b) Elixir\n(c) Milk\n(d) Water", "a-Blood",
    "Santa Claus is usually pictured in a suit consisting of which two colors?\n(a) Green & white\n(b) Red & white\n(c) Black & white\n(d) Blue & white", "b-Red & white",
    "Who is Batman's crime-fighting assistant?\n(a) Selena\n(b) Robin\n(c) Harvey\n(d) Gordan", "b-Robin",
    "Which fictional character was raised by apes?\n(a) Mowgli\n(b) Tarzan\n(c) Harry Potter\n(d) You", "b-Tarzan",
    "The racquet of which of these games does not have a net or strings in it?\n(a) Squash\n(b) Tennis\n(c) Badminton\n(d) Table Tennis", "d-Table Tennis",
    "Which of these legendary characters released a genie by rubbing a magical lamp?\n(a) King Arthur\n(b) Hercules\n(c) Pocahontas\n(d) Aladdin", "d-Aladdin",
    "Which of these ancient peoples are known for mummifying bodies?\n(a) Romans\n(b) Vikings\n(c) Egyptians\n(d) Greeks", "c-Egyptians",
    "In the world of computers and technology, what does the H in HTTP stand for?\n(a) High-Definition\n(b) Hyper\n(c) Heightened\n(d) Hypervisor", "b-Hyper",
    "Which term is used to describe a very good investment?\n(a) Potato Chip\n(b) Green Chip\n(c) Blue Chip\n(d) Wood Chip", "c-Blue Chip",
    "What object launched by NASA was named after Edwin Hubble?\n(a) Satellite\n(b) Space Telescope\n(c) Space Shuttle\n(d) Image Sensor", "b-Space Telescope",
    "Which of these alcoholic drinks originated in Mexico?\n(a) Tequila\n(b) Martini\n(c) Sake\n(d) Bloody Mary", "a-Tequila",
    "After which Greek Goddess is the US space program to land the first woman and next man on the Moon by 2024 named?\n(a) Rhea\n(b) Nemesis\n(c) Aphrodite\n(d) Artemis", "d-Artemis",
    "In 2019, which telescope captured the first-ever Black Hole image?\n(a) James Webb Space Telescope\n(b) Event Horizon Telescope\n(c) Hubble Space Telescope\n(d) Spitzer Space Telescope", "b-Event Horizon Telescope"
]
prize_money = [5000, 10000, 20000, 40000, 80000, 160000, 320000,
               640000, 1250000, 2500000, 5000000, 10000000, 50000000]
score = 0
money = 0
index = 0
checkpoint = 0
print("WELCOME TO KAUN BANEGA CROREPATI GAME".center(100))
print("Rules => \n\t1. [You can answer with either a,b,c,d or the word itself.]\n\t2. [There are 3 checkpoints in the game, if you cross that point, you are assured you will atleast take take amount from the game.]\n\t3. [At any point if you feel like quiting, just press 'q' and you will walk away with whatever you've won.]\n\n")
for q in range(0, len(questions), 2):
    print(
        f"QUESTION {index+1} for Rs. {prize_money[index]} => \n"+questions[q])
    answer = input("Answer: ").lower()
    answer_bank = questions[q+1].split("-")
    if (answer == 'q'):
        break
    if ((answer) == (answer_bank[0].lower())) or (answer == (answer_bank[1].lower())):
        money = prize_money[index]
        print(f"\nSahi Jawaab!\nMoney Won => Rs.{money}\n")
        index += 1
        score += 1
        if (money == 10000):
            checkpoint = 1
            print(
                "[You have hit checkpoint 1]\n")
        if (money == 320000):
            checkpoint = 2
            print(
                "[You have hit checkpoint 2]\n")
        if (money == 2500000):
            checkpoint = 3
            print(
                "[You have hit checkpoint 3]\n")
        if (money == 10000000):
            print(
                "[Crorepati Ban gaye aap]\n".upper())
    else:
        print("\nGalat Jawaab.\n")
        print("Correct Answer: "+answer_bank[1])
        if (checkpoint == 1):
            money = 10000
        elif (checkpoint == 2):
            money = 320000
        elif (checkpoint == 3):
            money = 2500000
        else:
            money = 0
        break

print("\nYou got", score, "answers right out of", int(len(questions)/2))
print("Total Money Won: Rs.", money)
