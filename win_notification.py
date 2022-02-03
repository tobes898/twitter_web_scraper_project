from win10toast import ToastNotifier

def MyNotification(text):
    toaster = ToastNotifier()
    toaster.show_toast("Twitter Notification", text)