from smartphone import Smartphone

catalog = [
    Smartphone ("Honor" , "A50" , "+79032556522"),
    Smartphone ("Honor" , "A50" , "+79036585555"),
    Smartphone ("Honor" , "A50" , "+79039854522"),
    Smartphone ("Honor" , "A50" , "+79098524174"),
    Smartphone ("Honor" , "A50" , "+79020254885"),

]
for phone in catalog:
    print(f"{phone.marka} - {phone.model}. {phone.number}")