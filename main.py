from FrequencyCounter.same import FrequencyCounterSame

class Example:
    description = ''

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description


if __name__ == '__main__':
    example = Example()
    print('Example set description:', example.set_description('Hi There!'))
    print('Example description is:', example.get_description())

