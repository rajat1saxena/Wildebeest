import zen_core as zencoding

def code():
    text = str(raw_input("Enter text"))

    print(text)

    p=zencoding.find_abbr_in_line(text,len(text))

    d=zencoding.expand_abbreviation(text,'html','xhtml')

    d=zencoding.wrap_with_abbreviation('body',d)

    print(d)
    print(p)


