

class Language:
    def __init__(self) -> None:
        pass 

    def language(self, a: str, b: str, c:str) -> list:
        list_ru: list = []
        for i in range(ord(a), ord(b)):
            list_ru.append(chr(i))

        list_ru.append(c)
        return list_ru
    
    def ru(self) -> list:
        return self.language('а','я','я')
    
    def en(self) -> list:
        return self.language('a','z','z')
    
    def determine(self, line: str) -> str:
        for i in self.ru():
            if i == line[0]:
                return 'ru'
        return 'en'


class Caesar():
    def __init__(self, line: str, number: int, ev: str) -> None:
        self.lan = Language()
        self.line: str = line
        self.number: int = number
        self.ev: str = ev

    def caesar(self) -> None:
        len_number: int
        res: str = ''
        list_len: list = []

        if self.lan.determine(self.line) == 'ru':
            list_len = self.lan.ru()
        else:
            list_len = self.lan.en()

        len_number = len(list_len)

        if len(self.line.split(' ')) == 1:
            for i in self.line:
                x = 0
                for a in list_len:
                    if a == i:
                        break
                    x += 1
                
                if self.ev == 'code':
                    number = x + self.number
                else:
                    number = x - self.number

                if number < len_number:
                    res += list_len[number]
                else:
                    res += list_len[number - len_number]

            print(res)

        else:
            list_res: list = []
            for i in self.line.split(' '):
                res = ''
                for b in i:
                    x = 0
                    for a in list_len:
                        if a == b:
                            break
                        x += 1
                    
                    if self.ev == 'code':
                        number = x + self.number
                    else:
                        number = x - self.number
                    
                    if number <= len_number:
                        res += list_len[number]
                    else:
                        res += list_len[number - len_number]
            
                list_res.append(res)
            
            res = ''
            for i in list_res:
                res += i + ' '
            
            print(res)
        
Caesar('рдьд йпд одьч ч игим рмьм', 4, 'decode').caesar()