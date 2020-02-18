#! python3
import webbrowser, sys, pyperclip

if len(sys.argv) > 1: 			# checks to see if an argument has been introduced in the Run line
    address = ' '.join(sys.argv[1:])
else:					# if no argument is given, this uses the last thing copied to your clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/search/' + address)  # concatenates argument behind URL and opens in default browser
