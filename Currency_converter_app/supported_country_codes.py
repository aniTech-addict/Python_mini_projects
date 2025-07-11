# Country name conversion to country code for API CALL

country_codes = {'UNITED ARAB EMIRATES': 'AED',
 'AFGHANISTAN': 'AFN',
 'ALBANIA': 'ALL',
 'ARMENIA': 'AMD',
 'NETHERLANDS ANTILLES': 'ANG',
 'ANGOLA': 'AOA',
 'ARGENTINA': 'ARS',
 'AUSTRALIA': 'AUD',
 'ARUBA': 'AWG',
 'AZERBAIJAN': 'AZN',
 'BOSNIA AND HERZEGOVINA': 'BAM',
 'BARBADOS': 'BBD',
 'BANGLADESH': 'BDT',
 'BULGARIA': 'BGN',
 'BAHRAIN': 'BHD',
 'BURUNDI': 'BIF',
 'BERMUDA': 'BMD',
 'BRUNEI': 'BND',
 'BOLIVIA': 'BOB',
 'BRAZIL': 'BRL',
 'BAHAMAS': 'BSD',
 'BHUTAN': 'BTN',
 'BOTSWANA': 'BWP',
 'BELARUS': 'BYN',
 'BELIZE': 'BZD',
 'CANADA': 'CAD',
 'DEMOCRATIC REPUBLIC OF THE CONGO': 'CDF',
 'SWITZERLAND': 'CHF',
 'CHILE': 'CLP',
 'CHINA': 'CNY',
 'COLOMBIA': 'COP',
 'COSTA RICA': 'CRC',
 'CUBA': 'CUP',
 'CAPE VERDE': 'CVE',
 'CZECH REPUBLIC': 'CZK',
 'DJIBOUTI': 'DJF',
 'DENMARK': 'DKK',
 'DOMINICAN REPUBLIC': 'DOP',
 'ALGERIA': 'DZD',
 'EGYPT': 'EGP',
 'ERITREA': 'ERN',
 'ETHIOPIA': 'ETB',
 'EUROPEAN UNION': 'EUR',
 'FIJI': 'FJD',
 'FALKLAND ISLANDS': 'FKP',
 'FAROE ISLANDS': 'FOK',
 'UNITED KINGDOM': 'GBP',
 'GEORGIA': 'GEL',
 'GUERNSEY': 'GGP',
 'GHANA': 'GHS',
 'GIBRALTAR': 'GIP',
 'THE GAMBIA': 'GMD',
 'GUINEA': 'GNF',
 'GUATEMALA': 'GTQ',
 'GUYANA': 'GYD',
 'HONG KONG': 'HKD',
 'HONDURAS': 'HNL',
 'CROATIA': 'HRK',
 'HAITI': 'HTG',
 'HUNGARY': 'HUF',
 'INDONESIA': 'IDR',
 'ISRAEL': 'ILS',
 'ISLE OF MAN': 'IMP',
 'INDIA': 'INR',
 'IRAQ': 'IQD',
 'IRAN': 'IRR',
 'ICELAND': 'ISK',
 'JERSEY': 'JEP',
 'JAMAICA': 'JMD',
 'JORDAN': 'JOD',
 'JAPAN': 'JPY',
 'KENYA': 'KES',
 'KYRGYZSTAN': 'KGS',
 'CAMBODIA': 'KHR',
 'KIRIBATI': 'KID',
 'COMOROS': 'KMF',
 'SOUTH KOREA': 'KRW',
 'KUWAIT': 'KWD',
 'CAYMAN ISLANDS': 'KYD',
 'KAZAKHSTAN': 'KZT',
 'LAOS': 'LAK',
 'LEBANON': 'LBP',
 'SRI LANKA': 'LKR',
 'LIBERIA': 'LRD',
 'LESOTHO': 'LSL',
 'LIBYA': 'LYD',
 'MOROCCO': 'MAD',
 'MOLDOVA': 'MDL',
 'MADAGASCAR': 'MGA',
 'NORTH MACEDONIA': 'MKD',
 'MYANMAR': 'MMK',
 'MONGOLIA': 'MNT',
 'MACAU': 'MOP',
 'MAURITANIA': 'MRU',
 'MAURITIUS': 'MUR',
 'MALDIVES': 'MVR',
 'MALAWI': 'MWK',
 'MEXICO': 'MXN',
 'MALAYSIA': 'MYR',
 'MOZAMBIQUE': 'MZN',
 'NAMIBIA': 'NAD',
 'NIGERIA': 'NGN',
 'NICARAGUA': 'NIO',
 'NORWAY': 'NOK',
 'NEPAL': 'NPR',
 'NEW ZEALAND': 'NZD',
 'OMAN': 'OMR',
 'PANAMA': 'PAB',
 'PERU': 'PEN',
 'PAPUA NEW GUINEA': 'PGK',
 'PHILIPPINES': 'PHP',
 'PAKISTAN': 'PKR',
 'POLAND': 'PLN',
 'PARAGUAY': 'PYG',
 'QATAR': 'QAR',
 'ROMANIA': 'RON',
 'SERBIA': 'RSD',
 'RUSSIA': 'RUB',
 'RWANDA': 'RWF',
 'SAUDI ARABIA': 'SAR',
 'SOLOMON ISLANDS': 'SBD',
 'SEYCHELLES': 'SCR',
 'SUDAN': 'SDG',
 'SWEDEN': 'SEK',
 'SINGAPORE': 'SGD',
 'SAINT HELENA': 'SHP',
 'SIERRA LEONE': 'SLE',
 'SOMALIA': 'SOS',
 'SURINAME': 'SRD',
 'SOUTH SUDAN': 'SSP',
 'SÃO TOMÉ AND PRÍNCIPE': 'STN',
 'SYRIA': 'SYP',
 'ESWATINI': 'SZL',
 'THAILAND': 'THB',
 'TAJIKISTAN': 'TJS',
 'TURKMENISTAN': 'TMT',
 'TUNISIA': 'TND',
 'TONGA': 'TOP',
 'TURKEY': 'TRY',
 'TRINIDAD AND TOBAGO': 'TTD',
 'TUVALU': 'TVD',
 'TAIWAN': 'TWD',
 'TANZANIA': 'TZS',
 'UKRAINE': 'UAH',
 'UGANDA': 'UGX',
 'UNITED STATES': 'USD',
 'URUGUAY': 'UYU',
 'UZBEKISTAN': 'UZS',
 'VENEZUELA': 'VES',
 'VIETNAM': 'VND',
 'VANUATU': 'VUV',
 'SAMOA': 'WST',
 'CEMAC': 'XAF',
 'ORGANISATION OF EASTERN CARIBBEAN STATES': 'XCD',
 'INTERNATIONAL MONETARY FUND': 'XDR',
 'CFA': 'XOF',
 "COLLECTIVITÉS D'OUTRE-MER": 'XPF',
 'YEMEN': 'YER',
 'SOUTH AFRICA': 'ZAR',
 'ZAMBIA': 'ZMW',
 'ZIMBABWE': 'ZWL'}