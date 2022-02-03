from win10toast import ToastNotifier

class WindowAlert:

    def MyNotification(self, text):
        toaster = ToastNotifier()
        toaster.show_toast("Twitter Notification", text, duration=10)


