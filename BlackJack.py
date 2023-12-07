# create data list
# show two of those data and ask from the user about maximum like count
# compare with actual value and reEAT if use correct otherwise end up.
from vs import vst
celebrities = [
    {
        "Name": "Selena Gomez",
        "Profession": "Singer and Actress",
        "Country": "United States",
        "Instagram Followers": 250_000_000
    },
    {
        "Name": "Cristiano Ronaldo",
        "Profession": "Professional Soccer Player",
        "Country": "Portugal",
        "Instagram Followers": 500_000_000
    },
    {
        "Name": "Priyanka Chopra",
        "Profession": "Actress and Producer",
        "Country": "India",
        "Instagram Followers": 7000_000_000
    },
    {
        "Name": "Elon Musk",
        "Profession": "Entrepreneur and CEO of SpaceX and Tesla",
        "Country": "United States",
        "Instagram Followers": 30_000_000
    },
    {
        "Name": "Kylie Jenner",
        "Profession": "Businesswoman and Reality TV Personality",
        "Country": "United States",
        "Instagram Followers": 300_000_000
    },
    {
        "Name": "Dwayne 'The Rock' Johnson",
        "Profession": "Actor and Former Professional Wrestler",
        "Country": "United States",
        "Instagram Followers": 300_000_000
    },
    {
        "Name": "Beyoncé",
        "Profession": "Singer and Actress",
        "Country": "United States",
        "Instagram Followers": 200_000_000
    },
    {
        "Name": "Lionel Messi",
        "Profession": "Professional Soccer Player",
        "Country": "Argentina",
        "Instagram Followers": 200_000_000
    },
    {
        "Name": "Taylor Swift",
        "Profession": "Singer and Songwriter",
        "Country": "United States",
        "Instagram Followers": 170_000_000
    },
    {
        "Name": "Kim Kardashian",
        "Profession": "Businesswoman and Reality TV Personality",
        "Country": "United States",
        "Instagram Followers": 250_000_000
    }
]
not_changed = 0
def printing_details(currentNumber):
    print(f"Name : {celebrities[currentNumber]["Name"]}\n"
          f"Profession : {celebrities[currentNumber]["Profession"]}\n"
          f"Country : {celebrities[currentNumber]["Country"]}\n")
def returnFollowers(notChanged,currentNumber):
    if int(celebrities[notChanged]["Instagram Followers"])\
          > int(celebrities[currentNumber]["Instagram Followers"]):
       
        return 1
    elif int(celebrities[notChanged]["Instagram Followers"])\
          < int(celebrities[currentNumber]["Instagram Followers"]):
        global not_changed
        not_changed = currentNumber
        return 2
def game():
    current_Number = 1
    global not_changed
    print("\n\n\n\n\n\n")
    while(current_Number<10):
        printing_details(not_changed)
        print(vst)
        printing_details(current_Number)
        user_choise = input("high/low : ")
        if (user_choise=="high" and returnFollowers(not_changed,current_Number)==2)\
            or(user_choise=="low" and returnFollowers(not_changed,current_Number)==1):
            print("\nanswer is corrent\n")
            current_Number+=1
        else:
            print("fail")
            current_Number = 10

game()
