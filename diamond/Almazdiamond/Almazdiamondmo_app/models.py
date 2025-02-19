from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CURRENCY_CHOICES = [
    ('AED', 'United Arab Emirates dirham'),
    ('AFN', 'Afghan afghani'),
    ('ALL', 'Albanian lek'),
    ('AMD', 'Armenian dram'),
    ('ANG', 'Netherlands Antillean guilder'),
    ('AOA', 'Angolan kwanza'),
    ('ARS', 'Argentine peso'),
    ('AUD', 'Australian dollar'),
    ('AWG', 'Aruban florin'),
    ('AZN', 'Azerbaijani manat'),
    ('BAM', 'Bosnia and Herzegovina convertible mark'),
    ('BBD', 'Barbadian dollar'),
    ('BDT', 'Bangladeshi taka'),
    ('BGN', 'Bulgarian lev'),
    ('BHD', 'Bahraini dinar'),
    ('BIF', 'Burundian franc'),
    ('BMD', 'Bermudian dollar'),
    ('BND', 'Brunei dollar'),
    ('BOB', 'Bolivian boliviano'),
    ('BRL', 'Brazilian real'),
    ('BSD', 'Bahamian dollar'),
    ('BTN', 'Bhutanese ngultrum'),
    ('BWP', 'Botswana pula'),
    ('BYN', 'Belarusian ruble'),
    ('BZD', 'Belize dollar'),
    ('CAD', 'Canadian dollar'),
    ('CDF', 'Congolese franc'),
    ('CHF', 'Swiss franc'),
    ('CLP', 'Chilean peso'),
    ('CNY', 'Chinese yuan'),
    ('COP', 'Colombian peso'),
    ('CRC', 'Costa Rican colón'),
    ('CUP', 'Cuban peso'),
    ('CVE', 'Cape Verdean escudo'),
    ('CZK', 'Czech koruna'),
    ('DJF', 'Djiboutian franc'),
    ('DKK', 'Danish krone'),
    ('DOP', 'Dominican peso'),
    ('DZD', 'Algerian dinar'),
    ('EGP', 'Egyptian pound'),
    ('ERN', 'Eritrean nakfa'),
    ('ETB', 'Ethiopian birr'),
    ('EUR', 'Euro'),
    ('FJD', 'Fijian dollar'),
    ('FKP', 'Falkland Islands pound'),
    ('FOK', 'Faroese króna'),
    ('GBP', 'British pound'),
    ('GEL', 'Georgian lari'),
    ('GGP', 'Guernsey pound'),
    ('GHS', 'Ghanaian cedi'),
    ('GIP', 'Gibraltar pound'),
    ('GMD', 'Gambian dalasi'),
    ('GNF', 'Guinean franc'),
    ('GTQ', 'Guatemalan quetzal'),
    ('GYD', 'Guyanese dollar'),
    ('HKD', 'Hong Kong dollar'),
    ('HNL', 'Honduran lempira'),
    ('HRK', 'Croatian kuna'),
    ('HTG', 'Haitian gourde'),
    ('HUF', 'Hungarian forint'),
    ('IDR', 'Indonesian rupiah'),
    ('ILS', 'Israeli new shekel'),
    ('IMP', 'Isle of Man pound'),
    ('INR', 'Indian rupee'),
    ('IQD', 'Iraqi dinar'),
    ('IRR', 'Iranian rial'),
    ('ISK', 'Icelandic króna'),
    ('JEP', 'Jersey pound'),
    ('JMD', 'Jamaican dollar'),
    ('JOD', 'Jordanian dinar'),
    ('JPY', 'Japanese yen'),
    ('KES', 'Kenyan shilling'),
    ('KGS', 'Kyrgyzstani som'),
    ('KHR', 'Cambodian riel'),
    ('KID', 'Kiribati dollar'),
    ('KMF', 'Comorian franc'),
    ('KRW', 'South Korean won'),
    ('KWD', 'Kuwaiti dinar'),
    ('KYD', 'Cayman Islands dollar'),
    ('KZT', 'Kazakhstani tenge'),
    ('LAK', 'Lao kip'),
    ('LBP', 'Lebanese pound'),
    ('LKR', 'Sri Lankan rupee'),
    ('LRD', 'Liberian dollar'),
    ('LSL', 'Lesotho loti'),
    ('LYD', 'Libyan dinar'),
    ('MAD', 'Moroccan dirham'),
    ('MDL', 'Moldovan leu'),
    ('MGA', 'Malagasy ariary'),
    ('MKD', 'Macedonian denar'),
    ('MMK', 'Myanmar kyat'),
    ('MNT', 'Mongolian tögrög'),
    ('MOP', 'Macanese pataca'),
    ('MRU', 'Mauritanian ouguiya'),
    ('MUR', 'Mauritian rupee'),
    ('MVR', 'Maldivian rufiyaa'),
    ('MWK', 'Malawian kwacha'),
    ('MXN', 'Mexican peso'),
    ('MYR', 'Malaysian ringgit'),
    ('MZN', 'Mozambican metical'),
    ('NAD', 'Namibian dollar'),
    ('NGN', 'Nigerian naira'),
    ('NIO', 'Nicaraguan córdoba'),
    ('NOK', 'Norwegian krone'),
    ('NPR', 'Nepalese rupee'),
    ('NZD', 'New Zealand dollar'),
    ('OMR', 'Omani rial'),
    ('PAB', 'Panamanian balboa'),
    ('PEN', 'Peruvian sol'),
    ('PGK', 'Papua New Guinean kina'),
    ('PHP', 'Philippine peso'),
    ('PKR', 'Pakistani rupee'),
    ('PLN', 'Polish złoty'),
    ('PYG', 'Paraguayan guaraní'),
    ('QAR', 'Qatari riyal'),
    ('RON', 'Romanian leu'),
    ('RSD', 'Serbian dinar'),
    ('RUB', 'Russian ruble'),
    ('RWF', 'Rwandan franc'),
    ('SAR', 'Saudi riyal'),
    ('SBD', 'Solomon Islands dollar'),
    ('SCR', 'Seychellois rupee'),
    ('SDG', 'Sudanese pound'),
    ('SEK', 'Swedish krona'),
    ('SGD', 'Singapore dollar'),
    ('SHP', 'Saint Helena pound'),
    ('SLL', 'Sierra Leonean leone'),
    ('SOS', 'Somali shilling'),
    ('SRD', 'Surinamese dollar'),
    ('SSP', 'South Sudanese pound'),
    ('STN', 'São Tomé and Príncipe dobra'),
    ('SYP', 'Syrian pound'),
    ('SZL', 'Eswatini lilangeni'),
    ('THB', 'Thai baht'),
    ('TJS', 'Tajikistani somoni'),
    ('TMT', 'Turkmenistani manat'),
    ('TND', 'Tunisian dinar'),
    ('TOP', 'Tongan paʻanga'),
    ('TRY', 'Turkish lira'),
    ('TTD', 'Trinidad and Tobago dollar'),
    ('TVD', 'Tuvaluan dollar'),
    ('TWD', 'New Taiwan dollar'),
    ('TZS', 'Tanzanian shilling'),
    ('UAH', 'Ukrainian hryvnia'),
    ('UGX', 'Ugandan shilling'),
    ('USD', 'United States dollar'),
    ('UYU', 'Uruguayan peso'),
    ('UZS', 'Uzbekistani soʻm'),
    ('VES', 'Venezuelan bolívar'),
    ('VND', 'Vietnamese đồng'),
    ('VUV', 'Vanuatu vatu'),
    ('WST', 'Samoan tala'),
    ('XAF', 'Central African CFA franc'),
    ('XCD', 'East Caribbean dollar'),
    ('XOF', 'West African CFA franc'),
    ('XPF', 'CFP franc'),
    ('YER', 'Yemeni rial'),
    ('ZAR', 'South African rand'),
    ('ZMW', 'Zambian kwacha'),
    ('ZWL', 'Zimbabwean dollar'),
]
class Shoppers(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    address_line1=models.TextField(null=True,blank=True)
    address_line2=models.TextField(null=True,blank=True)
    pincode=models.CharField(max_length=10,null=True,blank=True)

class Products(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    price=models.FloatField(null=True,blank=True)
    currency=models.CharField(max_length=50,choices=CURRENCY_CHOICES,default='USD')
    main_image=models.ImageField(upload_to='product_main_image/',null=True,blank=True)

class ProductFiles(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    files=models.FileField(upload_to='product_files/',null=True, blank=True)