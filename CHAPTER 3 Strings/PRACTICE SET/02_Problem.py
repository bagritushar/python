letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>
plz visit our office.
place: <|PLACE|>
'''  
print(letter.replace("<|NAME|>","Tushar Bagri").replace("<|DATE|>","23 February 2026").replace("<|PLACE|>","Mumbai"))


