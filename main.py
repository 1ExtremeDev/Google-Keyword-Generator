import random, requests, re, time, os

class OutPut():
    def __init__(self, keywords: list=None) -> ...:
        if keywords is None: keywords = []
        self.keywords = keywords
        self.save()
    def save(self):
        saved = ""
        if len(self.keywords) == 0:
            return
        for each in self.keywords:
            saved+=each + '\n'
        file = open('output.txt', 'a+', encoding='utf-8').write(saved)
        return 

class Generator:
    def __init__(keyword, times) -> any:
        return Generator.generate(keyword, times)
    def generate(keyword, times):
        result_keywords = []
        for each in range(times):
            value = random.randint(1,100*100); api = "https://suggestqueries.google.com/complete/search?client=chrome&q={}%20{}&jsonp=jsonpCB&_={}".format(keyword, each, value); del value, each; x = requests.get(api); del api; z = re.findall(',\[\"(.*?)\],\[\"', str(x.content))
            del x
            for each in z:
                if each.endswith('\"'):
                    for zz in each.split('"'):
                        if zz == ',' or zz == '': ...
                        else: result_keywords.append(zz)
                        del zz
                else: result_keywords.append(each)
                del each
            del z
        return result_keywords

question = {
    0: 'What\'s the keyword?',
    1: 'How many times do you want to check?'
}

def doStuff(nr: int=None) -> str:
    if nr is None: nr = 0
    print(question[nr])
    try:
        if nr == 0: keyword = input('> ')
        else: keyword = int(input('> '))
    except: print('Invalid input.');time.sleep(2);os._exit()
    return keyword
keyword = doStuff()
times = doStuff(1)
OutPut(Generator.__init__(keyword, times))
