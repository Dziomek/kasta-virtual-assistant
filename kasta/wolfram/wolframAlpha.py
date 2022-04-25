import wolframalpha


class Calculate:

    @staticmethod
    def makeCalculations(text):
        app_id = "L52Y7X-8LJK6XHPQ9"
        client = wolframalpha.Client(app_id)
        ind = text.lower().split().index('calculate')
        text = text.split()[ind +1]
        res = client.query(" ".join(text))
        answer = next(res.result).text
        return "The answer is ", answer