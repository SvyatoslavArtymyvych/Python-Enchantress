LOW = 'l'
MIDDLE = 'm'
UPPER_MIDDLE = 'u'
HIGH = 'h'

POPULATIONS_TYPES_CHOICES = (
    (LOW, "Low"),
    (MIDDLE, "Middle"),
    (UPPER_MIDDLE, "Upper-middle"),
    (HIGH, "High"),
)


GASOLINE = 'g'
DIESEL = 'd'
BIO_DIESEL = 'b'
ETHANOL = 'e'
OTHER = 'o'

FUEL_TYPE_CHOICES = (
    (GASOLINE, "Gasoline"),
    (DIESEL, "Diesel"),
    (BIO_DIESEL, "Bio Diesel"),
    (ETHANOL, "Ethanol"),
    (OTHER, "Other"),
)


STATUS_NEW = 'n'
STATUS_USED = 'u'

STATUS_CHOICES = (
    (STATUS_NEW, "New"),
    (STATUS_USED, "Used"),
)


ORDER_STATUS_OPEN = 'o'
ORDER_STATUS_CLOSED = 'c'

ORDER_STATUS_CHOICES = (
    (ORDER_STATUS_OPEN, "Opened"),
    (ORDER_STATUS_CLOSED, "Closed"),
)