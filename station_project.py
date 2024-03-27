print("input shablon1,shablon2 or shablon3:")
shablon = input()


def shablon1():

    print("input time:")
    time = input()
    print("input transport:")
    transport = input()
    print("input adjective1:")
    adjective1 = input()
    print("input adjective2:")
    adjective2 = input()
    print("input noun:")
    noun = input()
    print("input part of body:")
    body = input()
    print("input color:")
    color = input()
    print("input verb:")
    verb = input()
    print("input number:")
    number = input()
    print("input noun2:")
    noun2 = input()
    print("input noun3:")
    noun3 = input()
    print("input part of body:")
    body2 = input()
    print("input verb2:")
    verb2 = input()
    print("input noun4:")
    noun4 = input()
    print("input adjective3:")
    adjective3 = input()
    print("input stupidword")
    stupidword = input()
    print("input noun5:")
    noun5 = input()
    print("It was about" + time + "ago when I arrived at the hospital in a \n" +transport +
           ". The hospital is a/an" + adjective1 + " place, there are a lot of" + adjective2+" " + noun +
           "here There are nurses here who have" + color+" " +
                body + ". If someone wants to come into my room I told them that they have to\n" + verb +" "
           "first. Ive decorated my room with" + number+ " " + noun2 + ".\n Today I talked to a doctor and they were wearing a" + noun3 + " on their " + body2 +
           "I heard that all doctors " + verb2 +" "+ noun4 + "every day for breakfast.\nThe most " +
                adjective3 + " thing about being in the hospital is the " + stupidword +" "+ noun5)


def shablon2():
     print("input proper noun (persons name):")
     personsname = input()
     print("input noun:")
     noun=input()
     print("input adjective (feeling):")
     feeling=input()
     print("input verb:")
     verb=input()
     print("input adjective (feeling2:")
     feeling2=input()
     print("input animal1:")
     animal1=input()
     print("input verb2:")
     verb2=input()
     print("input color1:")
     color1=input()
     print("input verb (ending in ing):")
     verb3 =input()
     print("input adverb (ending in ly):")
     adverb=input()
     print("input number:")
     number1=input()
     print("input measure of time:")
     measureoftime=input()
     print("input color2:")
     color2=input()
     print("input animal2:")
     animal2=input()
     print("input number:")
     number2=input()
     print("input silly word:")
     sillyword=input()
     print("input noun2:")
     noun2=input()
     print(f"""This weekend I am going camping with {personsname}.I packed my lantern, sleeping bag, and {noun}.
           I am so {feeling} to {verb} in a tent. I am {feeling2} we might see an {animal1}, I hear they are kind of dangerous. While we were camping, we are going to hike, fish, and {verb2}. 
           I have heard that the {color1} lake is great for {verb3}. Then we will {adverb} hike through the forest for {number1} {measureoftime}. 
           If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {sillyword} stories and roast {noun2} around the campfire."""
     )

  


def shablon3():
    print("input proper noun (persons name):")
    personsname = input()
    print("input adjecive:")
    adjective = input()
    print("input color:")
    color = input()
    print("input animal:")
    animal = input()
    print("input place:")
    place = input()
    print("adjective2:")
    adjective2 = input()
    print("input magical creature(plural):")
    plural = input()
    print("input adjective3")
    adjective3=input()
    print("input magical creature(plural)2:")
    plural2 = input()
    print("input room in a house:")
    roominahouse = input()
    print("input noun:")
    noun= input()
    print("input noun2:")
    noun2= input()
    print("input noun(plural)3:")
    plural3=input()
    print("input adjective4")
    adjective4=input()
    print("input noun(plural)4:")
    plural4=input()
    print("input number:")
    number=input()
    print("input measure of time:")
    measureoftime=input ()
    print("input verb (ending in ing:")
    verbendingining=input()
    print("input adjective5")
    adjective5=input()
    print(" input noun5:")
    noun5=input()
    print(f"""Dear {personsname}, I am writing to you from a  {adjective} castle in an enchanted forest.
            I found myself here one day after going for a ride on a  {color}  {animal} in {place}.
            There are {adjective2} {plural} and {adjective3} {plural2} here! In the {roominahouse} there is a pool full of {noun}. 
            I fall asleep each night on a {noun2} of {plural3} and dream of {adjective4} {plural4}.
            It feels as though I have lived here for {number} {measureoftime}.
            I hope one day you can visit, although the only way to get here now is {verbendingining} on a  {adjective5} {noun5}.""")






if shablon == "shablon1":
    shablon1()

elif shablon == "shablon2":
    shablon2()

elif shablon == ("shablon3"):
    shablon3()
else:
    print("please refresh")