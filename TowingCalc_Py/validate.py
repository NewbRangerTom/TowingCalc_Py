class validate():
    """Input validation methodes"""
    def disallowZero(self):
        while True:
            print('\nEnter vehicle',variable,': ')
            variable = input()
            if variable == '':
                print(variable,'Can not be blank')
                continue
            elif int(variable) == 0:
                print(variable,'can not be 0')
                continue
            elif int(variable) > 0:
                break

    def allowZero(self):
        while True:
            print('\nEnter vehicle', variable,': ')
            variable = input()
            if variable == '':
                print(variable,'Can not be blank')
                continue
            elif int(variable) >= 0:
                break