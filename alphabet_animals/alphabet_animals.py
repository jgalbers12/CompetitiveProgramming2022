from sys import stdin, stdout, exit

animal_list = [False] * 26

def char_to_index(c):
    return(ord(c) - ord("a"))

if __name__ == "__main__":
    last_animal = stdin.readline().rstrip()
    last_animal_l_index = char_to_index(last_animal[-1])
    n = int(stdin.readline())
    animals_to_remember = []
    for i in range(n):
        animal = stdin.readline().rstrip()
        f_index = char_to_index(animal[0])
        if f_index == last_animal_l_index:
            animals_to_remember.append(animal)
        animal_list[f_index] = True
    output = "?"
    first_playable_found = False
    for animal in animals_to_remember:
        if animal[0] == animal[-1]:
            if len(animals_to_remember) > 1:
                if not first_playable_found:
                    output = animal
                    first_playable_found = True
            else:
                output = animal + "!"
                break
        elif animal_list[char_to_index(animal[-1])] == False:
            output = animal + "!"
            break
        elif not first_playable_found:
            output = animal
            first_playable_found = True
    stdout.write(output)
