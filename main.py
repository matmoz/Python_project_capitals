import string
import random

def capitals_state(file_name): # przetwarzamy plik panstw i stolic na liste dwuwymiarowa
    capitals_state = []
    with open(file_name, "r") as file:
        for line in file:
            state = line.split(',')
            capitals = state[1].strip('  \n')
            state = state[0]
            capitals_state.append([state, capitals])
    return capitals_state

def write_intro(name, index): # szablon poczatku testu
    name_q, name_a = name
    with open(name_q, "w") as test:
        test.write("\n{:.<35}   {:.<20}".format('Imie i nazwisko', 'Data'))
        test.write("\n\n{:.<20}".format('klasa'))
        test.write("\n\n{:>38} {:>10}".format('Sprawdzian Panstwa i Stolice', '(Formularz %d)' %index))
        test.close()
    with open(name_a, "w") as odp: # szablon poczatku odpowiedzi
        odp.write("Formularz %d" %index)

def write_end(name): # szablon konca testu
    with open(name, "a") as test:
        test.write("\n\n{:.<10}   {:.<10}".format('Pkt', 'Ocena'))
        test.close()

def random_questions(file_trouple): #generujemy schemat do pytan nazwe panstwa ze stolica + 3 losowe stolice
    list = capitals_state("stolice.txt")
    state_capitals = []
    capitals = []
    tmp = []
    for x in range(list.__len__()):
        capitals.append(list[x][1])
    for i in range(capitals.__len__()):
        while 1:
            correct = random.choice(list)
            if correct not in state_capitals: # zapobiegamy powtarzaniu sie pytan o dane panstwo
                state_capitals.append(correct)
                tmp.append(correct[0])
                tmp.append(correct[1])
                break
            else:
                continue
        for j in range(3): # losujemy 3 dodatkowe stolice wykluczajac te co zostaly juz wygenerowane w pyaniu
            while 1:
                odp = random.choice(capitals)
                if odp not in tmp:
                    tmp.append(odp)
                    break
        nr = random.choice([1, 2, 3, 4]) # losujemy ktora z odpowiedzi za mienimy miejscem z ta wlasciwa
        M = tmp[nr]
        tmp[nr] = tmp[1]
        tmp[1] = M
        if nr == 1:
            nr = 'A'
        if nr == 2:
            nr = 'B'
        if nr == 3:
            nr = 'C'
        if nr == 4:
            nr = 'D'
        tmp[5:] = [nr, file_trouple, i] #generujemy szablon danych pytania
        write_questions_answers(tmp) # [panstwo, stolica_1, ..., ...,  stolica_4, poprawna odp, nazwa pliku, nr pytania]
        tmp = []

def write_questions_answers(lista):#wpisujemy wygenerowane pytania i odpowiedzi do odpowiednich plikow
    state, a, b, c, d, odp, plik, index = lista
    file_a, file_o = plik
    with open(file_a, "a") as file_a: # zapisujemy kolejno pytania do utworzonego juz wczesniej pliku
        file_a.write("\n\n%d." %(index + 1) + " Jaka stolice ma panstwo %s?\n" %state)
        file_a.write("{}\n".format("   A. %s" %a))
        file_a.write("{}\n".format("   B. %s" % b))
        file_a.write("{}\n".format("   C. %s" % c))
        file_a.write("{}\n".format("   D. %s" % d))
        file_a.close()
    with open(file_o, "a") as file_o: # zapisujemy kolejno odpowiedzi do pliku z odpowiedziami
        file_o.write("\n%d." %(index + 1) + "%s" %odp )
        file_o.close()

if "__main__" == __name__:
    ilosc_spr = 1 # podajemy ile testow chcemy wygenerowac
    for cout in range(ilosc_spr):
        cout = cout + 1
        file_q = "test_" + str(cout) + ".txt"
        file_a = "odp_" + str(cout) + ".txt"
        file = (file_q, file_a) # tworzymy nazwe plikow testu
        write_intro(file, cout) # wpisujemy z szablonu niezmienny poczatek dla kazdego z testow
        random_questions(file) # losowe pytania zapisujemy do pliku
        write_end(file_q)   # wpisujemy zakonczenie do pliku tekstowego

