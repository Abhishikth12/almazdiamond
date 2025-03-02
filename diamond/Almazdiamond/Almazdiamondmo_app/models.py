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

SETTING_TYPES=(
    ('Solitaire','Solitaire'),
    ('Halo','Halo'),
    ('Pave','Pave'),
    ('Three Stone','Three Stone'),
    ('Nature','Nature'),
    ('Hidden Halo','Hidden Halo'),
    ('Sidestone','Sidestone'),
    ('Vintage','Vintage')

)

METAL_TYPES=(
    ('Yellow Gold','Yellow Gold'),
    ('White Gold','White Gold'),
    ('Rose Gold','Rose Gold'),
    ('Platinum','Platinum')
)
RING_SHAPES=(
    ('Round','Round'),
    ('Oval','Oval'),
    ('Pear','Pear'),
    ('E-Cushion','E-Cushion'),
    ('Cushion','Cushion'),
    ('Emerald','Emerald'),
    ('Princess','Princess'),
    ('Marquise','Marquise'),
    ('Radiant','Radiant')
    )

STONE_SHAPES=(
    ('Round','Round'),
    ('Emarald','Emarald'),
    ('Heart','Heart'),
    ('Marquise','Marquise'),
    ('Oval','Oval'),
    ('Pear','Pear'),
    ('Princess','Princess'),
    ('Radiant','Radiant'),
    ('Cushion','Cushion'),
    ('E-Cushion','E-Cushion')
    )

STONE_CUT_CHOICES=(
    ('Good','Good'),
    ('Very Good','Very Good'),
    ('Excellent','Excellent')
)

STONE_CLARITY=(
    ('SH','SH'),
    ('VS2','VS1'),
    ('VS1','VS1'),
    ('VVS2','VVS2'),
    ('VVS1','VVS1'),
    ('IF','IF'),
    ('FL','FL')
)
class Shoppers(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    address_line1=models.TextField(null=True,blank=True)
    address_line2=models.TextField(null=True,blank=True)
    pincode=models.CharField(max_length=10,null=True,blank=True)
class RingSettingTypes(models.Model):
    ring_setting=models.CharField(choices=SETTING_TYPES,max_length=60,null=True,blank=True)
    image=models.ImageField(upload_to='Ring_setting_images/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class RingSettings(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Ring_setting_variants(models.Model):
    ring=models.ForeignKey(RingSettings,on_delete=models.CASCADE)
    ring_settings=models.CharField(choices=SETTING_TYPES,max_length=60,null=True,blank=True)
    metal_type=models.CharField(choices=METAL_TYPES,max_length=100,null=True,blank=True)
    shapes=models.CharField(choices=RING_SHAPES,max_length=100,null=True,blank=True)
    price=models.FloatField(null=True,blank=True)
    currency=models.CharField(choices=CURRENCY_CHOICES,max_length=10,null=True,blank=True)
    image=models.ImageField(upload_to='Ring_images/',null=True,blank=True)

class RingDetails(models.Model):
    ring_variant=models.ForeignKey(Ring_setting_variants,on_delete=models.CASCADE,null=True,blank=True)
    file=models.FileField(upload_to='Ring_images/',null=True,blank=True)

class Stone(models.Model):
    stone_name=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    stone_type=models.CharField(max_length=100,null=True,blank=True)
    stone_shape=models.CharField(choices=STONE_SHAPES,max_length=100,null=True,blank=True)
    stone_carat=models.FloatField(null=True,blank=True)
    stone_color=models.CharField(max_length=100,null=True,blank=True)
    stone_clarity=models.CharField(choices=STONE_CLARITY,max_length=100,null=True,blank=True)
    stone_cut=models.CharField(choices=STONE_CUT_CHOICES,max_length=100,null=True,blank=True)
    stone_price=models.FloatField(null=True,blank=True)
    currency=models.CharField(choices=CURRENCY_CHOICES,max_length=10,null=True,blank=True)
    image=models.ImageField(upload_to='Stone_images/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class StoneDetails(models.Model):
    stone=models.ForeignKey(Stone,on_delete=models.CASCADE)
    file=models.FileField(upload_to='Stone_images/',null=True,blank=True)

class Combination(models.Model):
    stone=models.ForeignKey(Stone,on_delete=models.CASCADE)
    ring=models.ForeignKey(RingSettings,on_delete=models.CASCADE)
    price=models.FloatField(null=True,blank=True)
    currency=models.CharField(choices=CURRENCY_CHOICES,max_length=10,null=True,blank=True)

class CombinationFiles(models.Model):
    combination=models.ForeignKey(Combination,on_delete=models.CASCADE)
    files=models.FileField(upload_to='combinationfiles/',null=True,blank=True)
