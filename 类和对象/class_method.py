class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)







