from mailing import Mailing
from address import Address

to_address = Address (445000, "Тольятти", "Ленина", 32, 201)
from_address = Address (652114,"Екатеринбург", "Космонавтов",22, 2)
track = "12654"
cost = "200"

mailing = Mailing(to_address, from_address, cost, track)

print (mailing)
