#Maszyna Turinga sprawdzająca poprawność numeru PESEL


from AbstrKlasaMaszynaTuringa import AbstrakcyjnaMaszynaTuringa

class MaszynaTuringa(AbstrakcyjnaMaszynaTuringa):
    def __init__(self, statesList):
        self.states = statesList
        
    @property
    def ListStanow(self):
        lista = list()
        for states in self.states:
            lista.append(states)
        return lista

    @property
    def Przejscia(self):
        przejscia = list()
        for states in self.states:
            for char in self.states[states]:
                przejscia.append((states, char, self.states[states][char][0],self.states[states][char][1],self.states[states][char][2]))
        return przejscia

    def WykonajKrok(self, ZnakZTasmy):
        
        self.tape[self.tapePointer] = self.states[self.currentState][ZnakZTasmy][0]
        if self.states[self.currentState][ZnakZTasmy][1] == 'R':
            self.tapePointer += 1
        else:
            self.tapePointer -= 1
        self.currentState = self.states[self.currentState][ZnakZTasmy][2]
        
        
    def Uruchom(self, Tasma): 
        self.tape = Tasma
        self.tapePointer = 0
        self.currentState = 'start'
        while self.CzyStanJestKoncowy(self.currentState) == False:
            self.WykonajKrok(self.tape[self.tapePointer])
            print(Tasma, self.currentState) #do debugowania
        if self.currentState == 'endF':
            return False
        else:
            return True

    def CzyStanJestPoczatkowy(self, Stan):
        if Stan == 'start':
            return True
        else:
            return False

    def CzyStanJestKoncowy(self, Stan):
        if Stan == 'endT' or Stan == 'endF':
            return True
        else:
            return False

states = dict()
states['start'] = {'#':['#','R','start'], '0':['0','R','second'], '1':['1','R','second'], '2':['2','R','second'], '3':['2','R','second'], '4':['4','R','second'], '5':['5','R','second'], '6':['6','R','second'], '7':['7','R','second'], '8':['8','R','second'], '9':['9','R','second']}  
states['second'] = {'#':['#','R','endF'], '0':['0','R','third'], '1':['1','R','third'],'2':['2','R','third'], '3':['3','R','third'],  '4':['4','R','third'], '5':['5','R','third'], '6':['6','R','third'], '7':['7','R','third'], '8':['8','R','third'], '9':['9','R','third']} #0-9                            
states['third'] = {'#':['#','R','endF'], '0':['0','R','fourthA'], '1':['1','R','fourthB'], '2':['2','R','fourthA'], '3':['3','R','fourthB'], '4':['4','R','endF'], '5':['5','R','endF'], '6':['6','R','endF'], '7':['7','R','endF'], '8':['8','R','endF'], '9':['9','R','endF']}
states['fourthA'] = {'#':['#','R','endF'], '0':['0','R','fifth'], '1':['1','R','fifth'], '2':['2','R','fifth'], '3':['3','R','fifth'], '4':['4','R','fifth'], '5':['5','R','fifth'], '6':['6','R','fifth'],  '7':['7','R','fifth'], '8':['8','R','fifth'], '9':['9','R','fifth']} #0-9                            
states['fourthB'] = {'#':['#','R','endF'], '0':['0','R','fifth'], '1':['1','R','fifth'], '2':['2','R','fifth'],'3':['3','R','endF'], '4':['4','R','endF'], '5':['5','R','endF'],'6':['6','R','endF'], '7':['7','R','endF'], '8':['8','R','endF'],'9':['9','R','endF']}
states['fifth'] = {'#':['#','R','endF'], '0':['0','R','sixthA'], '1':['1','R','sixthB'], '2':['2','R','sixthB'], '3':['3','R','sixthC'], '4':['4','R','endF'], '5':['5','R','endF'],'6':['6','R','endF'], '7':['7','R','endF'], '8':['8','R','endF'],'9':['9','R','endF']}
states['sixthA'] = {'#':['#','R','endF'], '0':['0','R','endF'],'1':['1','R','seventh'], '2':['2','R','seventh'], '3':['3','R','seventh'], '4':['4','R','seventh'], '5':['5','R','seventh'], '6':['6','R','seventh'], '7':['7','R','seventh'], '8':['8','R','seventh'], '9':['9','R','seventh']} #1-9                                    
states['sixthB'] = {'#':['#','R','endF'], '0':['0','R','seventh'], '1':['1','R','seventh'], '2':['2','R','seventh'], '3':['3','R','seventh'], '4':['4','R','seventh'], '5':['5','R','seventh'], '6':['6','R','seventh'], '7':['7','R','seventh'], '8':['8','R','seventh'], '9':['9','R','seventh']}
states['sixthC'] = {'#':['#','R','endF'], '0':['0','R','seventh'], '1':['1','R','seventh'], '2':['2','R','endF'], '3':['3','R','endF'], '4':['4','R','endF'], '5':['5','R','endF'],'6':['6','R','endF'], '7':['7','R','endF'], '8':['8','R','endF'],'9':['9','R','endF']}
states['seventh'] = {'#':['#','R','endF'], '0':['0','R','eighth'], '1':['1','R','eighth'], '2':['2','R','eighth'], '3':['3','R','eighth'], '4':['4','R','eighth'], '5':['5','R','eighth'], '6':['6','R','eighth'], '7':['7','R','eighth'], '8':['8','R','eighth'], '9':['9','R','eighth']}#0-9
states['eighth'] = {'#':['#','R','endF'], '0':['0','R','ninth'], '1':['1','R','ninth'], '2':['2','R','ninth'], '3':['3','R','ninth'], '4':['4','R','ninth'], '5':['5','R','ninth'], '6':['6','R','ninth'], '7':['7','R','ninth'], '8':['8','R','ninth'], '9':['9','R','ninth']} #0-9
states['ninth'] = {'#':['#','R','endF'], '0':['0','R','tenth'], '1':['1','R','tenth'], '2':['2','R','tenth'], '3':['3','R','tenth'], '4':['4','R','tenth'], '5':['5','R','tenth'], '6':['6','R','tenth'], '7':['7','R','tenth'], '8':['8','R','tenth'], '9':['9','R','tenth']} #0-9
states['tenth'] = {'#':['#','R','endF'], '0':['0','R','eleventh'], '1':['1','R','eleventh'], '2':['2','R','eleventh'], '3':['3','R','eleventh'], '4':['4','R','eleventh'], '5':['5','R','eleventh'], '6':['6','R','eleventh'], '7':['7','R','eleventh'], '8':['8','R','eleventh'], '9':['9','R','eleventh']} #0-9
states['eleventh'] = {'#':['#','R','endF'], '0':['0','R','back1'], '1':['1','R','back1'], '2':['2','R','back1'], '3':['3','R','back1'], '4':['4','R','back1'], '5':['5','R','back1'], '6':['6','R','back1'], '7':['7','R','back1'], '8':['8','R','back1'], '9':['9','R','back1']} #0-9
states['back'] = {'#':['#','R','mul1'], '0':['0','L','back'], '1':['1','L','back'], '2':['2','L','back'], '3':['3','L','back'], '4':['4','L','back'], '5':['5','L','back'], '6':['6','L','back'], '7':['7','L','back'], '8':['8','L','back'], '9':['9','L','back']}
states['back1'] = {'#':['#','L','back']}
states['mul1'] = {'0':['0','R','mul2'],'1':['1','R','mul2'],'2':['2','R','mul2'],'3':['3','R','mul2'],'4':['4','R','mul2'],'5':['5','R','mul2'],'6':['6','R','mul2'],'7':['7','R','mul2'],'8':['8','R','mul2'],'9':['9','R','mul2']} #tabliczka mnożenia na 1 (tylko jedności)
states['mul2'] = {'0':['0','R','mul3'],'1':['3','R','mul3'],'2':['6','R','mul3'],'3':['9','R','mul3'],'4':['2','R','mul3'],'5':['5','R','mul3'],'6':['8','R','mul3'],'7':['1','R','mul3'],'8':['4','R','mul3'],'9':['7','R','mul3']} #3
states['mul3'] = {'0':['0','R','mul4'],'1':['7','R','mul4'],'2':['4','R','mul4'],'3':['1','R','mul4'],'4':['8','R','mul4'],'5':['5','R','mul4'],'6':['2','R','mul4'],'7':['9','R','mul4'],'8':['6','R','mul4'],'9':['3','R','mul4']} #7
states['mul4'] = {'0':['0','R','mul5'],'1':['9','R','mul5'],'2':['8','R','mul5'],'3':['7','R','mul5'],'4':['6','R','mul5'],'5':['5','R','mul5'],'6':['4','R','mul5'],'7':['3','R','mul5'],'8':['2','R','mul5'],'9':['1','R','mul5']} #9
states['mul5'] = {'0':['0','R','mul6'],'1':['1','R','mul6'],'2':['2','R','mul6'],'3':['3','R','mul6'],'4':['4','R','mul6'],'5':['5','R','mul6'],'7':['7','R','mul6'],'8':['8','R','mul6'],'9':['9','R','mul6']} #1
states['mul6'] = {'0':['0','R','mul7'],'1':['3','R','mul7'],'2':['6','R','mul7'],'3':['9','R','mul7'],'4':['2','R','mul7'],'5':['5','R','mul7'],'6':['8','R','mul7'],'7':['1','R','mul7'],'8':['4','R','mul7'],'9':['7','R','mul7']} #3
states['mul7'] = {'0':['0','R','mul8'],'1':['7','R','mul8'],'2':['4','R','mul8'],'3':['1','R','mul8'],'4':['8','R','mul8'],'5':['5','R','mul8'],'6':['2','R','mul8'],'7':['9','R','mul8'],'8':['6','R','mul8'],'9':['3','R','mul8']} #7
states['mul8'] = {'0':['0','R','mul9'],'1':['9','R','mul9'],'2':['8','R','mul9'],'3':['7','R','mul9'],'4':['6','R','mul9'],'5':['5','R','mul9'],'6':['4','R','mul9'],'7':['3','R','mul9'],'8':['2','R','mul9'],'9':['1','R','mul9']} #9
states['mul9'] = {'0':['0','R','mul10'],'1':['1','R','mul10'],'2':['2','R','mul10'],'3':['3','R','mul10'],'4':['4','R','mul10'],'5':['5','R','mul10'],'6':['6','R','mul10'],'7':['7','R','mul10'],'8':['8','R','mul10'],'9':['9','R','mul10']} #1
states['mul10'] = {'0':['0','R','cofnij'],'1':['3','R','cofnij'],'2':['6','R','cofnij'],'3':['9','R','cofnij'],'4':['2','R','cofnij'],'5':['5','R','cofnij'],'6':['8','R','cofnij'],'7':['1','R','cofnij'],'8':['4','R','cofnij'],'9':['7','R','cofnij']} #3
states['cofnij'] = {'0':['0','L','sum10'],'1':['1','L','sum10'],'2':['2','L','sum10'],'3':['3','L','sum10'],'4':['4','L','sum10'],'5':['5','L','sum10'],'6':['6','L','sum10'],'7':['7','L','sum10'],'8':['8','L','sum10'],'9':['9','L','sum10']}
states['sum10'] = {'1':['#','L','sum9A'],'2':['#','L','sum9B'],'3':['#','L','sum9C'],'4':['#','L','sum9D'],'5':['#','L','sum9E'],'6':['#','L','sum9F'],'7':['#','L','sum9G'],'8':['#','L','sum9H'],'9':['#','L','sum9I'],'0':['#','L','sum9J']}
states['sum9A'] = {'0':['1','L','return9'], '1':['2','L','return9'],'2':['3','L','return9'],'3':['4','L','return9'],'4':['5','L','return9'],'5':['6','L','return9'],'6':['7','L','return9'],'7':['8','L','return9'],'8':['9','L','return9'],'9':['0','L','return9']}
states['sum9B'] = {'0':['2','L','return9'], '1':['3','L','return9'],'2':['4','L','return9'],'3':['5','L','return9'],'4':['6','L','return9'],'5':['7','L','return9'],'6':['8','L','return9'],'7':['9','L','return9'],'8':['0','L','return9'],'9':['1','L','return9']}
states['sum9C'] = {'0':['3','L','return9'], '1':['4','L','return9'],'2':['5','L','return9'],'3':['6','L','return9'],'4':['7','L','return9'],'5':['8','L','return9'],'6':['9','L','return9'],'7':['0','L','return9'],'8':['1','L','return9'],'9':['2','L','return9']}
states['sum9D'] = {'0':['4','L','return9'], '1':['5','L','return9'],'2':['6','L','return9'],'3':['7','L','return9'],'4':['8','L','return9'],'5':['9','L','return9'],'6':['0','L','return9'],'7':['1','L','return9'],'8':['2','L','return9'],'9':['3','L','return9']}
states['sum9E'] = {'0':['5','L','return9'], '1':['6','L','return9'],'2':['7','L','return9'],'3':['8','L','return9'],'4':['9','L','return9'],'5':['0','L','return9'],'6':['1','L','return9'],'7':['2','L','return9'],'8':['3','L','return9'],'9':['4','L','return9']}
states['sum9F'] = {'0':['6','L','return9'], '1':['7','L','return9'],'2':['8','L','return9'],'3':['9','L','return9'],'4':['0','L','return9'],'5':['1','L','return9'],'6':['2','L','return9'],'7':['3','L','return9'],'8':['4','L','return9'],'9':['5','L','return9']}
states['sum9G'] = {'0':['7','L','return9'], '1':['8','L','return9'],'2':['9','L','return9'],'3':['0','L','return9'],'4':['1','L','return9'],'5':['2','L','return9'],'6':['3','L','return9'],'7':['4','L','return9'],'8':['5','L','return9'],'9':['6','L','return9']}
states['sum9H'] = {'0':['8','L','return9'], '1':['9','L','return9'],'2':['0','L','return9'],'3':['1','L','return9'],'4':['2','L','return9'],'5':['3','L','return9'],'6':['4','L','return9'],'7':['5','L','return9'],'8':['6','L','return9'],'9':['7','L','return9']}
states['sum9I'] = {'0':['9','L','return9'], '1':['0','L','return9'],'2':['1','L','return9'],'3':['2','L','return9'],'4':['3','L','return9'],'5':['4','L','return9'],'6':['5','L','return9'],'7':['6','L','return9'],'8':['7','L','return9'],'9':['8','L','return9']}
states['sum9J'] = {'0':['0','L','return9'], '1':['1','L','return9'],'2':['2','L','return9'],'3':['3','L','return9'],'4':['4','L','return9'],'5':['5','L','return9'],'6':['6','L','return9'],'7':['7','L','return9'],'8':['8','L','return9'],'9':['9','L','return9']}
states['sum9'] = {'1':['#','L','sum8A'],'2':['#','L','sum8B'],'3':['#','L','sum8C'],'4':['#','L','sum8D'],'5':['#','L','sum8E'],'6':['#','L','sum8F'],'7':['#','L','sum8G'],'8':['#','L','sum8H'],'9':['#','L','sum8I'],'0':['#','L','sum8J']}
states['return9'] = {'0':['0','R','sum9'],'1':['1','R','sum9'],'2':['2','R','sum9'],'3':['3','R','sum9'],'4':['4','R','sum9'],'5':['5','R','sum9'],'6':['6','R','sum9'],'7':['7','R','sum9'],'8':['8','R','sum9'],'9':['9','R','sum9']}
states['sum8A'] = {'0':['1','L','return8'], '1':['2','L','return8'],'2':['3','L','return8'],'3':['4','L','return8'],'4':['5','L','return8'],'5':['6','L','return8'],'6':['7','L','return8'],'7':['8','L','return8'],'8':['9','L','return8'],'9':['0','L','return8']}
states['sum8B'] = {'0':['2','L','return8'], '1':['3','L','return8'],'2':['4','L','return8'],'3':['5','L','return8'],'4':['6','L','return8'],'5':['7','L','return8'],'6':['8','L','return8'],'7':['9','L','return8'],'8':['0','L','return8'],'9':['1','L','return8']}
states['sum8C'] = {'0':['3','L','return8'], '1':['4','L','return8'],'2':['5','L','return8'],'3':['6','L','return8'],'4':['7','L','return8'],'5':['8','L','return8'],'6':['9','L','return8'],'7':['0','L','return8'],'8':['1','L','return8'],'9':['2','L','return8']}
states['sum8D'] = {'0':['4','L','return8'], '1':['5','L','return8'],'2':['6','L','return8'],'3':['7','L','return8'],'4':['8','L','return8'],'5':['9','L','return8'],'6':['0','L','return8'],'7':['1','L','return8'],'8':['2','L','return8'],'9':['3','L','return8']}
states['sum8E'] = {'0':['5','L','return8'], '1':['6','L','return8'],'2':['7','L','return8'],'3':['8','L','return8'],'4':['9','L','return8'],'5':['0','L','return8'],'6':['1','L','return8'],'7':['2','L','return8'],'8':['3','L','return8'],'9':['4','L','return8']}
states['sum8F'] = {'0':['6','L','return8'], '1':['7','L','return8'],'2':['8','L','return8'],'3':['9','L','return8'],'4':['0','L','return8'],'5':['1','L','return8'],'6':['2','L','return8'],'7':['3','L','return8'],'8':['4','L','return8'],'9':['5','L','return8']}
states['sum8G'] = {'0':['7','L','return8'], '1':['8','L','return8'],'2':['9','L','return8'],'3':['0','L','return8'],'4':['1','L','return8'],'5':['2','L','return8'],'6':['3','L','return8'],'7':['4','L','return8'],'8':['5','L','return8'],'9':['6','L','return8']}
states['sum8H'] = {'0':['8','L','return8'], '1':['9','L','return8'],'2':['0','L','return8'],'3':['1','L','return8'],'4':['2','L','return8'],'5':['3','L','return8'],'6':['4','L','return8'],'7':['5','L','return8'],'8':['6','L','return8'],'9':['7','L','return8']}
states['sum8I'] = {'0':['9','L','return8'], '1':['0','L','return8'],'2':['1','L','return8'],'3':['2','L','return8'],'4':['3','L','return8'],'5':['4','L','return8'],'6':['5','L','return8'],'7':['6','L','return8'],'8':['7','L','return8'],'9':['8','L','return8']}
states['sum8J'] = {'0':['0','L','return8'], '1':['1','L','return8'],'2':['2','L','return8'],'3':['3','L','return8'],'4':['4','L','return8'],'5':['5','L','return8'],'6':['6','L','return8'],'7':['7','L','return8'],'8':['8','L','return8'],'9':['9','L','return8']}
states['sum8'] = {'1':['#','L','sum7A'],'2':['#','L','sum7B'],'3':['#','L','sum7C'],'4':['#','L','sum7D'],'5':['#','L','sum7E'],'6':['#','L','sum7F'],'7':['#','L','sum7G'],'8':['#','L','sum7H'],'9':['#','L','sum7I'],'0':['#','L','sum7J']}
states['return8'] = {'0':['0','R','sum8'],'1':['1','R','sum8'],'2':['2','R','sum8'],'3':['3','R','sum8'],'4':['4','R','sum8'],'5':['5','R','sum8'],'6':['6','R','sum8'],'7':['7','R','sum8'],'8':['8','R','sum8'],'9':['9','R','sum8']}
states['sum7A'] = {'0':['1','L','return7'], '1':['2','L','return7'],'2':['3','L','return7'],'3':['4','L','return7'],'4':['5','L','return7'],'5':['6','L','return7'],'6':['7','L','return7'],'7':['8','L','return7'],'8':['9','L','return7'],'9':['0','L','return7']}
states['sum7B'] = {'0':['2','L','return7'], '1':['3','L','return7'],'2':['4','L','return7'],'3':['5','L','return7'],'4':['6','L','return7'],'5':['7','L','return7'],'6':['8','L','return7'],'7':['9','L','return7'],'8':['0','L','return7'],'9':['1','L','return7']}
states['sum7C'] = {'0':['3','L','return7'], '1':['4','L','return7'],'2':['5','L','return7'],'3':['6','L','return7'],'4':['7','L','return7'],'5':['8','L','return7'],'6':['9','L','return7'],'7':['0','L','return7'],'8':['1','L','return7'],'9':['2','L','return7']}
states['sum7D'] = {'0':['4','L','return7'], '1':['5','L','return7'],'2':['6','L','return7'],'3':['7','L','return7'],'4':['8','L','return7'],'5':['9','L','return7'],'6':['0','L','return7'],'7':['1','L','return7'],'8':['2','L','return7'],'9':['3','L','return7']}
states['sum7E'] = {'0':['5','L','return7'], '1':['6','L','return7'],'2':['7','L','return7'],'3':['8','L','return7'],'4':['9','L','return7'],'5':['0','L','return7'],'6':['1','L','return7'],'7':['2','L','return7'],'8':['3','L','return7'],'9':['4','L','return7']}
states['sum7F'] = {'0':['6','L','return7'], '1':['7','L','return7'],'2':['8','L','return7'],'3':['9','L','return7'],'4':['0','L','return7'],'5':['1','L','return7'],'6':['2','L','return7'],'7':['3','L','return7'],'8':['4','L','return7'],'9':['5','L','return7']}
states['sum7G'] = {'0':['7','L','return7'], '1':['8','L','return7'],'2':['9','L','return7'],'3':['0','L','return7'],'4':['1','L','return7'],'5':['2','L','return7'],'6':['3','L','return7'],'7':['4','L','return7'],'8':['5','L','return7'],'9':['6','L','return7']}
states['sum7H'] = {'0':['8','L','return7'], '1':['9','L','return7'],'2':['0','L','return7'],'3':['1','L','return7'],'4':['2','L','return7'],'5':['3','L','return7'],'6':['4','L','return7'],'7':['5','L','return7'],'8':['6','L','return7'],'9':['7','L','return7']}
states['sum7I'] = {'0':['9','L','return7'], '1':['0','L','return7'],'2':['1','L','return7'],'3':['2','L','return7'],'4':['3','L','return7'],'5':['4','L','return7'],'6':['5','L','return7'],'7':['6','L','return7'],'8':['7','L','return7'],'9':['8','L','return7']}
states['sum7J'] = {'0':['0','L','return7'], '1':['1','L','return7'],'2':['2','L','return7'],'3':['3','L','return7'],'4':['4','L','return7'],'5':['5','L','return7'],'6':['6','L','return7'],'7':['7','L','return7'],'8':['8','L','return7'],'9':['9','L','return7']}
states['sum7'] = {'1':['#','L','sum6A'],'2':['#','L','sum6B'],'3':['#','L','sum6C'],'4':['#','L','sum6D'],'5':['#','L','sum6E'],'6':['#','L','sum6F'],'7':['#','L','sum6G'],'8':['#','L','sum6H'],'9':['#','L','sum6I'],'0':['#','L','sum6J']}
states['return7'] = {'0':['0','R','sum7'],'1':['1','R','sum7'],'2':['2','R','sum7'],'3':['3','R','sum7'],'4':['4','R','sum7'],'5':['5','R','sum7'],'6':['6','R','sum7'],'7':['7','R','sum7'],'8':['8','R','sum7'],'9':['9','R','sum7']}
states['sum6A'] = {'0':['1','L','return6'], '1':['2','L','return6'],'2':['3','L','return6'],'3':['4','L','return6'],'4':['5','L','return6'],'5':['6','L','return6'],'6':['7','L','return6'],'7':['8','L','return6'],'8':['9','L','return6'],'9':['0','L','return6']}
states['sum6B'] = {'0':['2','L','return6'], '1':['3','L','return6'],'2':['4','L','return6'],'3':['5','L','return6'],'4':['6','L','return6'],'5':['7','L','return6'],'6':['8','L','return6'],'7':['9','L','return6'],'8':['0','L','return6'],'9':['1','L','return6']}
states['sum6C'] = {'0':['3','L','return6'], '1':['4','L','return6'],'2':['5','L','return6'],'3':['6','L','return6'],'4':['7','L','return6'],'5':['8','L','return6'],'6':['9','L','return6'],'7':['0','L','return6'],'8':['1','L','return6'],'9':['2','L','return6']}
states['sum6D'] = {'0':['4','L','return6'], '1':['5','L','return6'],'2':['6','L','return6'],'3':['7','L','return6'],'4':['8','L','return6'],'5':['9','L','return6'],'6':['0','L','return6'],'7':['1','L','return6'],'8':['2','L','return6'],'9':['3','L','return6']}
states['sum6E'] = {'0':['5','L','return6'], '1':['6','L','return6'],'2':['7','L','return6'],'3':['8','L','return6'],'4':['9','L','return6'],'5':['0','L','return6'],'6':['1','L','return6'],'7':['2','L','return6'],'8':['3','L','return6'],'9':['4','L','return6']}
states['sum6F'] = {'0':['6','L','return6'], '1':['7','L','return6'],'2':['8','L','return6'],'3':['9','L','return6'],'4':['0','L','return6'],'5':['1','L','return6'],'6':['2','L','return6'],'7':['3','L','return6'],'8':['4','L','return6'],'9':['5','L','return6']}
states['sum6G'] = {'0':['7','L','return6'], '1':['8','L','return6'],'2':['9','L','return6'],'3':['0','L','return6'],'4':['1','L','return6'],'5':['2','L','return6'],'6':['3','L','return6'],'7':['4','L','return6'],'8':['5','L','return6'],'9':['6','L','return6']}
states['sum6H'] = {'0':['8','L','return6'], '1':['9','L','return6'],'2':['0','L','return6'],'3':['1','L','return6'],'4':['2','L','return6'],'5':['3','L','return6'],'6':['4','L','return6'],'7':['5','L','return6'],'8':['6','L','return6'],'9':['7','L','return6']}
states['sum6I'] = {'0':['9','L','return6'], '1':['0','L','return6'],'2':['1','L','return6'],'3':['2','L','return6'],'4':['3','L','return6'],'5':['4','L','return6'],'6':['5','L','return6'],'7':['6','L','return6'],'8':['7','L','return6'],'9':['8','L','return6']}
states['sum6J'] = {'0':['0','L','return6'], '1':['1','L','return6'],'2':['2','L','return6'],'3':['3','L','return6'],'4':['4','L','return6'],'5':['5','L','return6'],'6':['6','L','return6'],'7':['7','L','return6'],'8':['8','L','return6'],'9':['9','L','return6']}
states['sum6'] = {'1':['#','L','sum5A'],'2':['#','L','sum5B'],'3':['#','L','sum5C'],'4':['#','L','sum5D'],'5':['#','L','sum5E'],'6':['#','L','sum5F'],'7':['#','L','sum5G'],'8':['#','L','sum5H'],'9':['#','L','sum5I'],'0':['#','L','sum5J']}
states['return6'] = {'0':['0','R','sum6'],'1':['1','R','sum6'],'2':['2','R','sum6'],'3':['3','R','sum6'],'4':['4','R','sum6'],'5':['5','R','sum6'],'6':['6','R','sum6'],'7':['7','R','sum6'],'8':['8','R','sum6'],'9':['9','R','sum6']}
states['sum5A'] = {'0':['1','L','return5'], '1':['2','L','return5'],'2':['3','L','return5'],'3':['4','L','return5'],'4':['5','L','return5'],'5':['6','L','return5'],'6':['7','L','return5'],'7':['8','L','return5'],'8':['9','L','return5'],'9':['0','L','return5']}
states['sum5B'] = {'0':['2','L','return5'], '1':['3','L','return5'],'2':['4','L','return5'],'3':['5','L','return5'],'4':['6','L','return5'],'5':['7','L','return5'],'6':['8','L','return5'],'7':['9','L','return5'],'8':['0','L','return5'],'9':['1','L','return5']}
states['sum5C'] = {'0':['3','L','return5'], '1':['4','L','return5'],'2':['5','L','return5'],'3':['6','L','return5'],'4':['7','L','return5'],'5':['8','L','return5'],'6':['9','L','return5'],'7':['0','L','return5'],'8':['1','L','return5'],'9':['2','L','return5']}
states['sum5D'] = {'0':['4','L','return5'], '1':['5','L','return5'],'2':['6','L','return5'],'3':['7','L','return5'],'4':['8','L','return5'],'5':['9','L','return5'],'6':['0','L','return5'],'7':['1','L','return5'],'8':['2','L','return5'],'9':['3','L','return5']}
states['sum5E'] = {'0':['5','L','return5'], '1':['6','L','return5'],'2':['7','L','return5'],'3':['8','L','return5'],'4':['9','L','return5'],'5':['0','L','return5'],'6':['1','L','return5'],'7':['2','L','return5'],'8':['3','L','return5'],'9':['4','L','return5']}
states['sum5F'] = {'0':['6','L','return5'], '1':['7','L','return5'],'2':['8','L','return5'],'3':['9','L','return5'],'4':['0','L','return5'],'5':['1','L','return5'],'6':['2','L','return5'],'7':['3','L','return5'],'8':['4','L','return5'],'9':['5','L','return5']}
states['sum5G'] = {'0':['7','L','return5'], '1':['8','L','return5'],'2':['9','L','return5'],'3':['0','L','return5'],'4':['1','L','return5'],'5':['2','L','return5'],'6':['3','L','return5'],'7':['4','L','return5'],'8':['5','L','return5'],'9':['6','L','return5']}
states['sum5H'] = {'0':['8','L','return5'], '1':['9','L','return5'],'2':['0','L','return5'],'3':['1','L','return5'],'4':['2','L','return5'],'5':['3','L','return5'],'6':['4','L','return5'],'7':['5','L','return5'],'8':['6','L','return5'],'9':['7','L','return5']}
states['sum5I'] = {'0':['9','L','return5'], '1':['0','L','return5'],'2':['1','L','return5'],'3':['2','L','return5'],'4':['3','L','return5'],'5':['4','L','return5'],'6':['5','L','return5'],'7':['6','L','return5'],'8':['7','L','return5'],'9':['8','L','return5']}
states['sum5J'] = {'0':['0','L','return5'], '1':['1','L','return5'],'2':['2','L','return5'],'3':['3','L','return5'],'4':['4','L','return5'],'5':['5','L','return5'],'6':['6','L','return5'],'7':['7','L','return5'],'8':['8','L','return5'],'9':['9','L','return5']}
states['sum5'] = {'1':['#','L','sum4A'],'2':['#','L','sum4B'],'3':['#','L','sum4C'],'4':['#','L','sum4D'],'5':['#','L','sum4E'],'6':['#','L','sum4F'],'7':['#','L','sum4G'],'8':['#','L','sum4H'],'9':['#','L','sum4I'],'0':['#','L','sum4J']}
states['return5'] = {'0':['0','R','sum5'],'1':['1','R','sum5'],'2':['2','R','sum5'],'3':['3','R','sum5'],'4':['4','R','sum5'],'5':['5','R','sum5'],'6':['6','R','sum5'],'7':['7','R','sum5'],'8':['8','R','sum5'],'9':['9','R','sum5']}
states['sum4A'] = {'0':['1','L','return4'], '1':['2','L','return4'],'2':['3','L','return4'],'3':['4','L','return4'],'4':['5','L','return4'],'5':['6','L','return4'],'6':['7','L','return4'],'7':['8','L','return4'],'8':['9','L','return4'],'9':['0','L','return4']}
states['sum4B'] = {'0':['2','L','return4'], '1':['3','L','return4'],'2':['4','L','return4'],'3':['5','L','return4'],'4':['6','L','return4'],'5':['7','L','return4'],'6':['8','L','return4'],'7':['9','L','return4'],'8':['0','L','return4'],'9':['1','L','return4']}
states['sum4C'] = {'0':['3','L','return4'], '1':['4','L','return4'],'2':['5','L','return4'],'3':['6','L','return4'],'4':['7','L','return4'],'5':['8','L','return4'],'6':['9','L','return4'],'7':['0','L','return4'],'8':['1','L','return4'],'9':['2','L','return4']}
states['sum4D'] = {'0':['4','L','return4'], '1':['5','L','return4'],'2':['6','L','return4'],'3':['7','L','return4'],'4':['8','L','return4'],'5':['9','L','return4'],'6':['0','L','return4'],'7':['1','L','return4'],'8':['2','L','return4'],'9':['3','L','return4']}
states['sum4E'] = {'0':['5','L','return4'], '1':['6','L','return4'],'2':['7','L','return4'],'3':['8','L','return4'],'4':['9','L','return4'],'5':['0','L','return4'],'6':['1','L','return4'],'7':['2','L','return4'],'8':['3','L','return4'],'9':['4','L','return4']}
states['sum4F'] = {'0':['6','L','return4'], '1':['7','L','return4'],'2':['8','L','return4'],'3':['9','L','return4'],'4':['0','L','return4'],'5':['1','L','return4'],'6':['2','L','return4'],'7':['3','L','return4'],'8':['4','L','return4'],'9':['5','L','return4']}
states['sum4G'] = {'0':['7','L','return4'], '1':['8','L','return4'],'2':['9','L','return4'],'3':['0','L','return4'],'4':['1','L','return4'],'5':['2','L','return4'],'6':['3','L','return4'],'7':['4','L','return4'],'8':['5','L','return4'],'9':['6','L','return4']}
states['sum4H'] = {'0':['8','L','return4'], '1':['9','L','return4'],'2':['0','L','return4'],'3':['1','L','return4'],'4':['2','L','return4'],'5':['3','L','return4'],'6':['4','L','return4'],'7':['5','L','return4'],'8':['6','L','return4'],'9':['7','L','return4']}
states['sum4I'] = {'0':['9','L','return4'], '1':['0','L','return4'],'2':['1','L','return4'],'3':['2','L','return4'],'4':['3','L','return4'],'5':['4','L','return4'],'6':['5','L','return4'],'7':['6','L','return4'],'8':['7','L','return4'],'9':['8','L','return4']}
states['sum4J'] = {'0':['0','L','return4'], '1':['1','L','return4'],'2':['2','L','return4'],'3':['3','L','return4'],'4':['4','L','return4'],'5':['5','L','return4'],'6':['6','L','return4'],'7':['7','L','return4'],'8':['8','L','return4'],'9':['9','L','return4']}
states['sum4'] = {'1':['#','L','sum3A'],'2':['#','L','sum3B'],'3':['#','L','sum3C'],'4':['#','L','sum3D'],'5':['#','L','sum3E'],'6':['#','L','sum3F'],'7':['#','L','sum3G'],'8':['#','L','sum3H'],'9':['#','L','sum3I'],'0':['#','L','sum3J']}
states['return4'] = {'0':['0','R','sum4'],'1':['1','R','sum4'],'2':['2','R','sum4'],'3':['3','R','sum4'],'4':['4','R','sum4'],'5':['5','R','sum4'],'6':['6','R','sum4'],'7':['7','R','sum4'],'8':['8','R','sum4'],'9':['9','R','sum4']}
states['sum3A'] = {'0':['1','L','return3'], '1':['2','L','return3'],'2':['3','L','return3'],'3':['4','L','return3'],'4':['5','L','return3'],'5':['6','L','return3'],'6':['7','L','return3'],'7':['8','L','return3'],'8':['9','L','return3'],'9':['0','L','return3']}
states['sum3B'] = {'0':['2','L','return3'], '1':['3','L','return3'],'2':['4','L','return3'],'3':['5','L','return3'],'4':['6','L','return3'],'5':['7','L','return3'],'6':['8','L','return3'],'7':['9','L','return3'],'8':['0','L','return3'],'9':['1','L','return3']}
states['sum3C'] = {'0':['3','L','return3'], '1':['4','L','return3'],'2':['5','L','return3'],'3':['6','L','return3'],'4':['7','L','return3'],'5':['8','L','return3'],'6':['9','L','return3'],'7':['0','L','return3'],'8':['1','L','return3'],'9':['2','L','return3']}
states['sum3D'] = {'0':['4','L','return3'], '1':['5','L','return3'],'2':['6','L','return3'],'3':['7','L','return3'],'4':['8','L','return3'],'5':['9','L','return3'],'6':['0','L','return3'],'7':['1','L','return3'],'8':['2','L','return3'],'9':['3','L','return3']}
states['sum3E'] = {'0':['5','L','return3'], '1':['6','L','return3'],'2':['7','L','return3'],'3':['8','L','return3'],'4':['9','L','return3'],'5':['0','L','return3'],'6':['1','L','return3'],'7':['2','L','return3'],'8':['3','L','return3'],'9':['4','L','return3']}
states['sum3F'] = {'0':['6','L','return3'], '1':['7','L','return3'],'2':['8','L','return3'],'3':['9','L','return3'],'4':['0','L','return3'],'5':['1','L','return3'],'6':['2','L','return3'],'7':['3','L','return3'],'8':['4','L','return3'],'9':['5','L','return3']}
states['sum3G'] = {'0':['7','L','return3'], '1':['8','L','return3'],'2':['9','L','return3'],'3':['0','L','return3'],'4':['1','L','return3'],'5':['2','L','return3'],'6':['3','L','return3'],'7':['4','L','return3'],'8':['5','L','return3'],'9':['6','L','return3']}
states['sum3H'] = {'0':['8','L','return3'], '1':['9','L','return3'],'2':['0','L','return3'],'3':['1','L','return3'],'4':['2','L','return3'],'5':['3','L','return3'],'6':['4','L','return3'],'7':['5','L','return3'],'8':['6','L','return3'],'9':['7','L','return3']}
states['sum3I'] = {'0':['9','L','return3'], '1':['0','L','return3'],'2':['1','L','return3'],'3':['2','L','return3'],'4':['3','L','return3'],'5':['4','L','return3'],'6':['5','L','return3'],'7':['6','L','return3'],'8':['7','L','return3'],'9':['8','L','return3']}
states['sum3J'] = {'0':['0','L','return3'], '1':['1','L','return3'],'2':['2','L','return3'],'3':['3','L','return3'],'4':['4','L','return3'],'5':['5','L','return3'],'6':['6','L','return3'],'7':['7','L','return3'],'8':['8','L','return3'],'9':['9','L','return3']}
states['sum3'] = {'1':['#','L','sum2A'],'2':['#','L','sum2B'],'3':['#','L','sum2C'],'4':['#','L','sum2D'],'5':['#','L','sum2E'],'6':['#','L','sum2F'],'7':['#','L','sum2G'],'8':['#','L','sum2H'],'9':['#','L','sum2I'],'0':['#','L','sum2J']}
states['return3'] = {'0':['0','R','sum3'],'1':['1','R','sum3'],'2':['2','R','sum3'],'3':['3','R','sum3'],'4':['4','R','sum3'],'5':['5','R','sum3'],'6':['6','R','sum3'],'7':['7','R','sum3'],'8':['8','R','sum3'],'9':['9','R','sum3']}
states['sum2A'] = {'0':['1','L','return2'], '1':['2','L','return2'],'2':['3','L','return2'],'3':['4','L','return2'],'4':['5','L','return2'],'5':['6','L','return2'],'6':['7','L','return2'],'7':['8','L','return2'],'8':['9','L','return2'],'9':['0','L','return2']}
states['sum2B'] = {'0':['2','L','return2'], '1':['3','L','return2'],'2':['4','L','return2'],'3':['5','L','return2'],'4':['6','L','return2'],'5':['7','L','return2'],'6':['8','L','return2'],'7':['9','L','return2'],'8':['0','L','return2'],'9':['1','L','return2']}
states['sum2C'] = {'0':['3','L','return2'], '1':['4','L','return2'],'2':['5','L','return2'],'3':['6','L','return2'],'4':['7','L','return2'],'5':['8','L','return2'],'6':['9','L','return2'],'7':['0','L','return2'],'8':['1','L','return2'],'9':['2','L','return2']}
states['sum2D'] = {'0':['4','L','return2'], '1':['5','L','return2'],'2':['6','L','return2'],'3':['7','L','return2'],'4':['8','L','return2'],'5':['9','L','return2'],'6':['0','L','return2'],'7':['1','L','return2'],'8':['2','L','return2'],'9':['3','L','return2']}
states['sum2E'] = {'0':['5','L','return2'], '1':['6','L','return2'],'2':['7','L','return2'],'3':['8','L','return2'],'4':['9','L','return2'],'5':['0','L','return2'],'6':['1','L','return2'],'7':['2','L','return2'],'8':['3','L','return2'],'9':['4','L','return2']}
states['sum2F'] = {'0':['6','L','return2'], '1':['7','L','return2'],'2':['8','L','return2'],'3':['9','L','return2'],'4':['0','L','return2'],'5':['1','L','return2'],'6':['2','L','return2'],'7':['3','L','return2'],'8':['4','L','return2'],'9':['5','L','return2']}
states['sum2G'] = {'0':['7','L','return2'], '1':['8','L','return2'],'2':['9','L','return2'],'3':['0','L','return2'],'4':['1','L','return2'],'5':['2','L','return2'],'6':['3','L','return2'],'7':['4','L','return2'],'8':['5','L','return2'],'9':['6','L','return2']}
states['sum2H'] = {'0':['8','L','return2'], '1':['9','L','return2'],'2':['0','L','return2'],'3':['1','L','return2'],'4':['2','L','return2'],'5':['3','L','return2'],'6':['4','L','return2'],'7':['5','L','return2'],'8':['6','L','return2'],'9':['7','L','return2']}
states['sum2I'] = {'0':['9','L','return2'], '1':['0','L','return2'],'2':['1','L','return2'],'3':['2','L','return2'],'4':['3','L','return2'],'5':['4','L','return2'],'6':['5','L','return2'],'7':['6','L','return2'],'8':['7','L','return2'],'9':['8','L','return2']}
states['sum2J'] = {'0':['0','L','return2'], '1':['1','L','return2'],'2':['2','L','return2'],'3':['3','L','return2'],'4':['4','L','return2'],'5':['5','L','return2'],'6':['6','L','return2'],'7':['7','L','return2'],'8':['8','L','return2'],'9':['9','L','return2']}
states['sum2'] = {'1':['#','L','sum1A'],'2':['#','L','sum1B'],'3':['#','L','sum1C'],'4':['#','L','sum1D'],'5':['#','L','sum1E'],'6':['#','L','sum1F'],'7':['#','L','sum1G'],'8':['#','L','sum1H'],'9':['#','L','sum1I'],'0':['#','L','sum1J']}
states['return2'] = {'0':['0','R','sum2'],'1':['1','R','sum2'],'2':['2','R','sum2'],'3':['3','R','sum2'],'4':['4','R','sum2'],'5':['5','R','sum2'],'6':['6','R','sum2'],'7':['7','R','sum2'],'8':['8','R','sum2'],'9':['9','R','sum2']}
states['sum1A'] = {'0':['1','L','return1'], '1':['2','L','return1'],'2':['3','L','return1'],'3':['4','L','return1'],'4':['5','L','return1'],'5':['6','L','return1'],'6':['7','L','return1'],'7':['8','L','return1'],'8':['9','L','return1'],'9':['0','L','return1']}
states['sum1B'] = {'0':['2','L','return1'], '1':['3','L','return1'],'2':['4','L','return1'],'3':['5','L','return1'],'4':['6','L','return1'],'5':['7','L','return1'],'6':['8','L','return1'],'7':['9','L','return1'],'8':['0','L','return1'],'9':['1','L','return1']}
states['sum1C'] = {'0':['3','L','return1'], '1':['4','L','return1'],'2':['5','L','return1'],'3':['6','L','return1'],'4':['7','L','return1'],'5':['8','L','return1'],'6':['9','L','return1'],'7':['0','L','return1'],'8':['1','L','return1'],'9':['2','L','return1']}
states['sum1D'] = {'0':['4','L','return1'], '1':['5','L','return1'],'2':['6','L','return1'],'3':['7','L','return1'],'4':['8','L','return1'],'5':['9','L','return1'],'6':['0','L','return1'],'7':['1','L','return1'],'8':['2','L','return1'],'9':['3','L','return1']}
states['sum1E'] = {'0':['5','L','return1'], '1':['6','L','return1'],'2':['7','L','return1'],'3':['8','L','return1'],'4':['9','L','return1'],'5':['0','L','return1'],'6':['1','L','return1'],'7':['2','L','return1'],'8':['3','L','return1'],'9':['4','L','return1']}
states['sum1F'] = {'0':['6','L','return1'], '1':['7','L','return1'],'2':['8','L','return1'],'3':['9','L','return1'],'4':['0','L','return1'],'5':['1','L','return1'],'6':['2','L','return1'],'7':['3','L','return1'],'8':['4','L','return1'],'9':['5','L','return1']}
states['sum1G'] = {'0':['7','L','return1'], '1':['8','L','return1'],'2':['9','L','return1'],'3':['0','L','return1'],'4':['1','L','return1'],'5':['2','L','return1'],'6':['3','L','return1'],'7':['4','L','return1'],'8':['5','L','return1'],'9':['6','L','return1']}
states['sum1H'] = {'0':['8','L','return1'], '1':['9','L','return1'],'2':['0','L','return1'],'3':['1','L','return1'],'4':['2','L','return1'],'5':['3','L','return1'],'6':['4','L','return1'],'7':['5','L','return1'],'8':['6','L','return1'],'9':['7','L','return1']}
states['sum1I'] = {'0':['9','L','return1'], '1':['0','L','return1'],'2':['1','L','return1'],'3':['2','L','return1'],'4':['3','L','return1'],'5':['4','L','return1'],'6':['5','L','return1'],'7':['6','L','return1'],'8':['7','L','return1'],'9':['8','L','return1']}
states['sum1J'] = {'0':['0','L','return1'], '1':['1','L','return1'],'2':['2','L','return1'],'3':['3','L','return1'],'4':['4','L','return1'],'5':['5','L','return1'],'6':['6','L','return1'],'7':['7','L','return1'],'8':['8','L','return1'],'9':['9','L','return1']}
states['return1'] = {'#':['#','R','sub']}
states['sub'] = {'0':['#','R','goJ'], '1':['#','R','goI'], '2':['#','R','goH'], '3':['#','R','goG'], '4':['#','R','goF'], '5':['#','R','goE'], '6':['#','R','goD'], '7':['#','R','goC'], '8':['#','R','goB'], '9':['#','R','goA']}
states['goA'] = {'#':['#','R','goA'], '1':['1','R','endT'], '2':['#','R','endF'], '3':['#','R','endF'], '4':['#','R','endF'], '5':['#','R','endF'], '6':['#','R','endF'], '7':['#','R','endF'], '8':['#','R','endF'], '9':['#','R','endF'], '0':['#','R','endF']}
states['goB'] = {'#':['#','R','goB'], '1':['#','R','endF'], '2':['1','R','endT'], '3':['#','R','endF'], '4':['#','R','endF'], '5':['#','R','endF'], '6':['#','R','endF'], '7':['#','R','endF'], '8':['#','R','endF'], '9':['#','R','endF'], '0':['#','R','endF']}
states['goC'] = {'#':['#','R','goC'], '1':['#','R','endF'], '2':['#','R','endF'], '3':['1','R','endT'], '4':['#','R','endF'], '5':['#','R','endF'], '6':['#','R','endF'], '7':['#','R','endF'], '8':['#','R','endF'], '9':['#','R','endF'], '0':['#','R','endF']}
states['goD'] = {'#':['#','R','goD'], '1':['#','R','endF'], '2':['#','R','endF'], '3':['#','R','endF'], '4':['1','R','endT'], '5':['#','R','endF'], '6':['#','R','endF'], '7':['#','R','endF'], '8':['#','R','endF'], '9':['#','R','endF'], '0':['#','R','endF']}
states['goE'] = {'#':['#','R','goE'], '1':['#','R','endF'], '2':['#','R','endF'], '3':['#','R','endF'], '4':['#','R','endF'], '5':['1','R','endT'], '6':['#','R','endF'], '7':['#','R','endF'], '8':['#','R','endF'], '9':['#','R','endF'], '0':['#','R','endF']}
states['goF'] = {'#':['#','R','goF'], '1':['#','R','endF'], '2':['#','R','endF'], '3':['#','R','endF'], '4':['#','R','endF'], '5':['#','R','endF'], '6':['1','R','endT'], '7':['#','R','endF'], '8':['#','R','endF'], '9':['#','R','endF'], '0':['#','R','endF']}
states['goG'] = {'#':['#','R','goG'], '1':['#','R','endF'], '2':['#','R','endF'], '3':['#','R','endF'], '4':['#','R','endF'], '5':['#','R','endF'], '6':['#','R','endF'], '7':['1','R','endT'], '8':['#','R','endF'], '9':['#','R','endF'], '0':['#','R','endF']}
states['goH'] = {'#':['#','R','goH'], '1':['#','R','endF'], '2':['#','R','endF'], '3':['#','R','endF'], '4':['#','R','endF'], '5':['#','R','endF'], '6':['#','R','endF'], '7':['#','R','endF'], '8':['1','R','endT'], '9':['#','R','endF'], '0':['#','R','endF']}
states['goI'] = {'#':['#','R','goI'], '1':['#','R','endF'], '2':['#','R','endF'], '3':['#','R','endF'], '4':['#','R','endF'], '5':['#','R','endF'], '6':['#','R','endF'], '7':['#','R','endF'], '8':['#','R','endF'], '9':['1','R','endT'], '0':['#','R','endF']}
states['goJ'] = {'#':['#','R','goJ'], '1':['#','R','endF'], '2':['#','R','endF'], '3':['#','R','endF'], '4':['#','R','endF'], '5':['#','R','endF'], '6':['#','R','endF'], '7':['#','R','endF'], '8':['#','R','endF'], '9':['#','R','endF'], '0':['1','R','endT']}


Maszyna = MaszynaTuringa(states)
tape = ['#','#','8','2','1','2','2','6','9','4','4','8','4']
for i in range(3):
    tape.append('#')

print(tape)
print(Maszyna.Uruchom(tape))
print(Maszyna.tape)


