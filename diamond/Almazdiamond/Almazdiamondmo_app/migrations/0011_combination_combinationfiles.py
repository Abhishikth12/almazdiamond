# Generated by Django 5.0.1 on 2025-02-22 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almazdiamondmo_app', '0010_alter_stone_stone_clarity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, choices=[('AED', 'United Arab Emirates dirham'), ('AFN', 'Afghan afghani'), ('ALL', 'Albanian lek'), ('AMD', 'Armenian dram'), ('ANG', 'Netherlands Antillean guilder'), ('AOA', 'Angolan kwanza'), ('ARS', 'Argentine peso'), ('AUD', 'Australian dollar'), ('AWG', 'Aruban florin'), ('AZN', 'Azerbaijani manat'), ('BAM', 'Bosnia and Herzegovina convertible mark'), ('BBD', 'Barbadian dollar'), ('BDT', 'Bangladeshi taka'), ('BGN', 'Bulgarian lev'), ('BHD', 'Bahraini dinar'), ('BIF', 'Burundian franc'), ('BMD', 'Bermudian dollar'), ('BND', 'Brunei dollar'), ('BOB', 'Bolivian boliviano'), ('BRL', 'Brazilian real'), ('BSD', 'Bahamian dollar'), ('BTN', 'Bhutanese ngultrum'), ('BWP', 'Botswana pula'), ('BYN', 'Belarusian ruble'), ('BZD', 'Belize dollar'), ('CAD', 'Canadian dollar'), ('CDF', 'Congolese franc'), ('CHF', 'Swiss franc'), ('CLP', 'Chilean peso'), ('CNY', 'Chinese yuan'), ('COP', 'Colombian peso'), ('CRC', 'Costa Rican colón'), ('CUP', 'Cuban peso'), ('CVE', 'Cape Verdean escudo'), ('CZK', 'Czech koruna'), ('DJF', 'Djiboutian franc'), ('DKK', 'Danish krone'), ('DOP', 'Dominican peso'), ('DZD', 'Algerian dinar'), ('EGP', 'Egyptian pound'), ('ERN', 'Eritrean nakfa'), ('ETB', 'Ethiopian birr'), ('EUR', 'Euro'), ('FJD', 'Fijian dollar'), ('FKP', 'Falkland Islands pound'), ('FOK', 'Faroese króna'), ('GBP', 'British pound'), ('GEL', 'Georgian lari'), ('GGP', 'Guernsey pound'), ('GHS', 'Ghanaian cedi'), ('GIP', 'Gibraltar pound'), ('GMD', 'Gambian dalasi'), ('GNF', 'Guinean franc'), ('GTQ', 'Guatemalan quetzal'), ('GYD', 'Guyanese dollar'), ('HKD', 'Hong Kong dollar'), ('HNL', 'Honduran lempira'), ('HRK', 'Croatian kuna'), ('HTG', 'Haitian gourde'), ('HUF', 'Hungarian forint'), ('IDR', 'Indonesian rupiah'), ('ILS', 'Israeli new shekel'), ('IMP', 'Isle of Man pound'), ('INR', 'Indian rupee'), ('IQD', 'Iraqi dinar'), ('IRR', 'Iranian rial'), ('ISK', 'Icelandic króna'), ('JEP', 'Jersey pound'), ('JMD', 'Jamaican dollar'), ('JOD', 'Jordanian dinar'), ('JPY', 'Japanese yen'), ('KES', 'Kenyan shilling'), ('KGS', 'Kyrgyzstani som'), ('KHR', 'Cambodian riel'), ('KID', 'Kiribati dollar'), ('KMF', 'Comorian franc'), ('KRW', 'South Korean won'), ('KWD', 'Kuwaiti dinar'), ('KYD', 'Cayman Islands dollar'), ('KZT', 'Kazakhstani tenge'), ('LAK', 'Lao kip'), ('LBP', 'Lebanese pound'), ('LKR', 'Sri Lankan rupee'), ('LRD', 'Liberian dollar'), ('LSL', 'Lesotho loti'), ('LYD', 'Libyan dinar'), ('MAD', 'Moroccan dirham'), ('MDL', 'Moldovan leu'), ('MGA', 'Malagasy ariary'), ('MKD', 'Macedonian denar'), ('MMK', 'Myanmar kyat'), ('MNT', 'Mongolian tögrög'), ('MOP', 'Macanese pataca'), ('MRU', 'Mauritanian ouguiya'), ('MUR', 'Mauritian rupee'), ('MVR', 'Maldivian rufiyaa'), ('MWK', 'Malawian kwacha'), ('MXN', 'Mexican peso'), ('MYR', 'Malaysian ringgit'), ('MZN', 'Mozambican metical'), ('NAD', 'Namibian dollar'), ('NGN', 'Nigerian naira'), ('NIO', 'Nicaraguan córdoba'), ('NOK', 'Norwegian krone'), ('NPR', 'Nepalese rupee'), ('NZD', 'New Zealand dollar'), ('OMR', 'Omani rial'), ('PAB', 'Panamanian balboa'), ('PEN', 'Peruvian sol'), ('PGK', 'Papua New Guinean kina'), ('PHP', 'Philippine peso'), ('PKR', 'Pakistani rupee'), ('PLN', 'Polish złoty'), ('PYG', 'Paraguayan guaraní'), ('QAR', 'Qatari riyal'), ('RON', 'Romanian leu'), ('RSD', 'Serbian dinar'), ('RUB', 'Russian ruble'), ('RWF', 'Rwandan franc'), ('SAR', 'Saudi riyal'), ('SBD', 'Solomon Islands dollar'), ('SCR', 'Seychellois rupee'), ('SDG', 'Sudanese pound'), ('SEK', 'Swedish krona'), ('SGD', 'Singapore dollar'), ('SHP', 'Saint Helena pound'), ('SLL', 'Sierra Leonean leone'), ('SOS', 'Somali shilling'), ('SRD', 'Surinamese dollar'), ('SSP', 'South Sudanese pound'), ('STN', 'São Tomé and Príncipe dobra'), ('SYP', 'Syrian pound'), ('SZL', 'Eswatini lilangeni'), ('THB', 'Thai baht'), ('TJS', 'Tajikistani somoni'), ('TMT', 'Turkmenistani manat'), ('TND', 'Tunisian dinar'), ('TOP', 'Tongan paʻanga'), ('TRY', 'Turkish lira'), ('TTD', 'Trinidad and Tobago dollar'), ('TVD', 'Tuvaluan dollar'), ('TWD', 'New Taiwan dollar'), ('TZS', 'Tanzanian shilling'), ('UAH', 'Ukrainian hryvnia'), ('UGX', 'Ugandan shilling'), ('USD', 'United States dollar'), ('UYU', 'Uruguayan peso'), ('UZS', 'Uzbekistani soʻm'), ('VES', 'Venezuelan bolívar'), ('VND', 'Vietnamese đồng'), ('VUV', 'Vanuatu vatu'), ('WST', 'Samoan tala'), ('XAF', 'Central African CFA franc'), ('XCD', 'East Caribbean dollar'), ('XOF', 'West African CFA franc'), ('XPF', 'CFP franc'), ('YER', 'Yemeni rial'), ('ZAR', 'South African rand'), ('ZMW', 'Zambian kwacha'), ('ZWL', 'Zimbabwean dollar')], max_length=10, null=True)),
                ('ring', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Almazdiamondmo_app.ringsettings')),
                ('stone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Almazdiamondmo_app.stone')),
            ],
        ),
        migrations.CreateModel(
            name='CombinationFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='combinationfiles/')),
                ('combination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Almazdiamondmo_app.combination')),
            ],
        ),
    ]
