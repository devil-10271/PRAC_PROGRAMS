import win10toast
import time
a=win10toast.ToastNotifier()

tim=int(time.strftime('%S'))
print(tim)
while True:
    ti=int(time.strftime('%S'))
    if tim == ti:
        tim=ti+2
        a.show_toast("Notification",'drink watter',duration=10)