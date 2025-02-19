import psutil
from win10toast import ToastNotifier

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 20 and not plugged:
    toaster = ToastNotifier()
    toaster.show_toast("Battery Low", f"{percent}% Battery remaining!!", duration=5)
elif percent <= 50 and not plugged:
    toaster = ToastNotifier()
    toaster.show_toast("Turn on power saving mode", f"{percent}% Battery remaining!!", duration=5)
elif percent >= 50 and not plugged:
    toaster = ToastNotifier()
    toaster.show_toast("Battery High", f"{percent}% Battery remaining!!", duration=5)