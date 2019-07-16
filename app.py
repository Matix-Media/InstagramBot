os = input("Select your OS (linux, win): ")
lang = input("Select your language (de, en): ")



if os == "linux":
    if lang == "en":
        exec(open("app.linux.en.py").read())

    if lang == "de":
        exec(open("app.linux.de.py").read())


if os == "win":
    if lang == "en":
        exec(open("app.win.en.py").read())

    if lang == "de":
        exec(open("app.win.de.py").read())

