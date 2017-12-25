#_*_ coding:utf-8 _*_
class person:
    attraction = 0
    assets = 0
    skills = []
    love_status = None
    lover = None
    job = None
    company = None

    def __init__(self,name,sex,role):
        self.name = name
        self.sex = sex
        self.role = role
        print '\033[32;1m-\033[0m'*60
        if self.role == 'rich':
            self.assets += 1000000
            self.attraction += 80
            print '\033[32;1mMy name is %s,I am a %s guy,i have %s money!' \
                  'It is  good to be rich...\033[0m ' %(self.name, self.role, self.assets)
        elif self.role == 'poor':
            self.assets += 5000
            self.attraction += 40
            print '\033[31;1mMy name is %s,I am a %s guy,i have %s money!' \
                  'I hate to be poor,but life is fucking hard....\033[0m ' %(self.name, self.role, self.assets)


        elif self.role == 'beauty':
            self.assets += 5000
            self.attraction += 90
            print '\033[32;1m My name is %s,i am %s girl,I do not have much money,but i am very beautiful,' \
                  'which makes me feel good and confident,' \
                  'but i don not want to be poor forever \033[0m' %(self.name,self.role)

    def talk(self,msg,tone='nomal'):
        if tone == 'normal':
            print '\033[32;1m%s:%s\033[0m' %(self.name,msg)
        elif tone == 'angry':
             print '\033[31;1m%s:%s\033[0m' %(self.name,msg)

    def assets_balance(self,amount,action):
        if action == 'earn':
            self.assets += amount
            print '\033[33;1m%s just made %sRMB!Current assets is %s\033[0m' %(self.name,amount,self.assets)
        elif action == 'cost':
            self.assets -= amount
            print '\033[33;1m%s just made %sRMB!Current assets is %s\033[0m' % (self.name, amount,self.assets)

p = person('Alex','male','rich')
p.talk('Hi guys')
p.assets_balance(5300,'earn')

p3 = person('Liz','female','beauty')
p2 = person('HanXin','male','poor')
p2.assets_balance(3000,'cost')
p2.lover = p3.name
p2.talk('I am poor but i have a beautifull girl,her name is %s,i love her very much ' % p2.name)



p3.love_status == 'not_single'
p3.lover = p2.name
p3.talk("I am a pretty girl but with no money,i have a boyfriend who's name is %s,he is not handsome,"
        "and not rich,but he loves me a lot,C'east La Vie" % p3.lover,'angry')




