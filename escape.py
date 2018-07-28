def escape(word):
    word = word.replace('\\' , '\\\\') # single backslash
    word = word.replace('\f' , '')
    word = word.replace('\b','')
    word = word.replace('\t' , '')
    word = word.replace('\n' , '')
    word = word.replace('\r' , '')
    word = word.replace('\"' , '')
    return word
