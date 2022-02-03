from win10toast import ToastNotifier

class WindowAlert:

    def MyNotification(self, text):
        print("HI")
        toaster = ToastNotifier()
        toaster.show_toast("Twitter Notification", text)



# client = webscrapper.setupTweepyClient()
# tweet = client.get_tweet(id=1488985196955418625)
# MyNotification(str(tweet[0]))
