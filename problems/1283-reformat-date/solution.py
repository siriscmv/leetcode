class Solution:
    def reformatDate(self, date: str) -> str:
        d, m, y = date.split(" ")

        MONTHS = {
            "Jan": '01', "Feb": '02', "Mar": '03',
            "Apr": '04', "May": '05', "Jun": '06',
            "Jul": '07', "Aug": '08', "Sep": '09',
            "Oct": '10', "Nov": '11', "Dec": '12'
        }

        if len(d) == 3: d = '0' + d[0:1]
        elif len(d) == 4: d = d[0:2]
        else: raise Exception('date')

        m = MONTHS[m]

        return "-".join([y, m, d])
