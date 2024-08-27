import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")

webbrowser.open("http://google.com/search?q=" + user_term)