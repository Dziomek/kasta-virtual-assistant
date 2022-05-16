import wolframalpha


class Calculate:

    @staticmethod
    def makeCalculations(text):
        app_id = "L52Y7X-8LJK6XHPQ9"
        client = wolframalpha.Client(app_id)
        res = client.query(text)
        try:
            answer = next(res.results).text
            return f"The answer is {answer}"
        except:
            return "Oh i missed that, try again"

