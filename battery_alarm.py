import subprocess

THRESHOLD = 101


def run():
    output = subprocess.check_output(["acpi"], universal_newlines=True)
    for s in output.split("\n"):
        s = s.strip()
        if len(s) == 0:
            continue
        perc = int(s.split(" ")[3].split('%')[0])
        try:
            if perc < THRESHOLD and s.split(" ")[2].find("Discharging") != -1:
                subprocess.call(["notify-send",
                                 "--icon",
                                 "/usr/share/icons/gnome/32x32/status/battery-caution.png",
                                 "-u",
                                 "critical", "Battery at %d" % perc
                                 ])
            else:
                print("All fine")
        except Exception as e:
            subprocess.call(["notify-send",
                             "--icon",
                             "/usr/share/icons/gnome/32x32/status/battery-caution.png",
                             "-u",
                             "critical", "Failed to run:" + e.__str__()
                             ])


if __name__ == '__main__':
    run()
