fields = [
    "vads_amount",
    "vads_auth_mode",
    "vads_auth_number",
    "vads_auth_result",
    "vads_capture_delay",
    "vads_card_brand",
    "vads_card_number",
    "vads_payment_certificate",
    "vads_ctx_mode",
    "vads_currency",
    "vads_effective_amount",
    "vads_site_id",
    "vads_trans_date",
    "vads_trans_id",
    "vads_trans_uuid",
    "vads_validation_mode",
    "vads_version",
    "vads_warranty_result",
    "vads_payment_src",
    "vads_order_id",
    "vads_cust_email",
    "vads_cust_id",
    "vads_cust_title",
    "vads_cust_status",
    "vads_cust_name",
    "vads_cust_zip",
    "vads_cust_city",
    "vads_cust_country",
    "vads_cust_phone",
    "vads_cust_cell_phone",
    "vads_ship_to_status",
    "vads_ship_to_name",
    "vads_ship_to_street",
    "vads_ship_to_city",
    "vads_ship_to_zip",
    "vads_ship_to_country",
    "vads_ship_to_phone_num",
    "vads_sequence_number",
    "vads_contract_used",
    "vads_trans_status",
    "vads_expiry_month",
    "vads_expiry_year",
    "vads_bank_product",
    "vads_pays_ip",
    "vads_presentation_date",
    "vads_effective_creation_date",
    "vads_operation_type",
    "vads_threeds_enrolled",
    "vads_threeds_cavv",
    "vads_threeds_eci",
    "vads_threeds_xid",
    "vads_threeds_cavvAlgorithm",
    "vads_threeds_status",
    "vads_threeds_sign_valid",
    "vads_threeds_error_code",
    "vads_threeds_exit_status",
    "vads_result",
    "vads_extra_result",
    "vads_card_country",
    "vads_language",
    "vads_hash",
    "vads_url_check_src",
    "vads_action_mode",
    "vads_cust_address",
    "vads_payment_config",
    "vads_page_action",
    "vads_shop_name",
    "vads_shop_url",
    "vads_bank_code",
    "signature"
]


fields = {
    """Mode d’acquisition des informations de la carte.
    INTERACTIVE: saisie des informations de la carte sur la page de paiement.
    SILENT: saisie des informations de la carte sur le site marchand
    (soumis à option commerciale délivrée par votre banque)."""
    'vads_action_mode': ['INTERACTIVE', 'SILENT'],

    """Montant de la transaction exprimé dans la plus petite unité de la
    monnaie ou devise(le centime pour l'euro) .."""
    'vads_amount': '1000',  # 10,00

    """Champ retourné dans la réponse.
    Spécifie de quelle manière est réalisée la demande d’autorisation.
    FULL : correspond à une autorisation du montant total de la transaction.
    Valeur utilisée dans le cas d’un paiement comptant, si la durée séparant
    la date de remise demandée de la date du jour est strictement inférieure
    à la durée de validité de l'autorisation.
    MARK : correspond à une autorisation de 1 euro."""
    'vads_auth_mode': ['FULL', 'MARK'],

    """Champ retourné dans la réponse.
    Numéro d'autorisation retourné par le serveur bancaire, si disponible
    (sinon vide)."""
    'vads_auth_number': '123456',

    """Champ retourné dans la réponse.
    Code retour de la demande d'autorisation retournée par la banque émettrice,
    si disponible
    Valeur Description Motif-frauduleux
    00 Transaction approuvée ou traitéeavec succès.
    02 Contacter l’émetteur de carte.
    03 Accepteur invalide. OUI
    04 Conserver la carte. OUI
    05 Ne pas honorer. OUI
    07 Conserver la carte, conditionsspéciales. OUI
    08 Approuver après identification.
    12 Transaction invalide. OUI
    13 Montant invalide OUI
    14 Numéro de porteur invalide. OUI
    15 Emetteur de carte inconnu. OUI
    17 Annulation acheteur.
    19 Répéter la transaction ultérieurement.
    20 Réponse erronée (erreur dans le domaine serveur).
    24 Mise à jour de fichier non supportée
    26 Enregistrement dupliqué, ancien enregistrement remplacé.
    27 Erreur en « edit » sur champ de liste à jour fichier.
    28 Accès interdit au fichier.
    29 Mise à jour impossible.
    30 Erreur de format.
    31 Identifiant de l’organisme acquéreur inconnu. OUI
    34 Suspicion de fraude. OUI
    33 Date de validité de la carte dépassée. OUI
    38 Date de validité de la carte dépassée.
    41 Carte perdue. OUI
    43 Carte volée. OUI
    51 Provision insuffisante ou créditdépassé.
    54 Date de validité de la carte dépassée. OUI
    55 Code confidentiel erroné.
    56 Carte absente du fichier. OUI
    57 Transaction non permise à ce porteur. OUI
    58 Transaction non permise à ce porteur.
    59 Suspicion de fraude. OUI
    60 L’accepteur de carte doit contacter l’acquéreur.
    61 Montant de retrait hors limite.
    63 Règles de sécurité non respectées. OUI
    68 Réponse non parvenue ou reçue trop tard.
    75 Nombre d’essais code confidentiel dépassé.
    25 Impossible de localiser l’enregistrement dans le fichier.
    76 Porteur déjà en opposition, ancien enregistrement conservé. OUI
    90 Arrêt momentané du système.
    91 Émetteur de cartes inaccessible.
    94 Transaction dupliquée.
    96 Mauvais fonctionnement du système.
    97 Échéance de la temporisation de surveillance globale.
    98 Serveur indisponible routage réseau demandé à nouveau.
    99 Incident domaine initiateur."""
    'vads_auth_result': [
        '00', '02', '03', '04', '05', '07', '08', '12', '13', '14', '15', '17',
        '19', '20', '24', '26', '27', '28', '29', '30', '31', '34', '33', '38',
        '41', '43', '51', '54', '55', '56', '57', '58', '59', '60', '61', '63',
        '68', '75', '25', '76', '90', '91', '94', '96', '97', '98', '99'],

    """Permet de spécifier les langues disponibles sur la page de paiement sous
    forme de liste.
    Chaque élément de la liste doit être séparé par un point-virgule « ; ».
    Est matérialisé par l’affichage de drapeaux sur la page de paiement .
    Format langue1;langue2;langue3
    'Allemand': 'de',
    'Anglais': 'en',
    'Chinois': 'zh',
    'Espagnol': 'es',
    'Français': 'fr',
    'Italien': 'it',
    'Japonais': 'ja',
    'Néerlandais': 'nl',
    'Polonais': 'pl',
    'Portugais': 'pt',
    'Russe': 'ru',
    'Suédois': 'sv',
    'Turc': 'tr',
    """
    'vads_available_languages': [
        'de', 'en', 'zh', 'es', 'fr', 'it', 'ja',
        'nl', 'pl', 'pt', 'ru', 'sv', 'tr'],

    """Champ retourné dans la réponse.
    Code banque associé à la banque émettrice."""
    'vads_bank_code': 12345,

    """Champ retourné dans la réponse.
    Code produit de la carte utilisée pour le paiement.
    VISA
    A Visa Traditional
    B Visa Traditional Rewards
    C Visa Signature
    D Visa Signature Preferred
    E Proprietary ATM
    F Visa Classic
    G Visa Business
    G1 Visa Signature Business
    G2 Reserved
    G3 Visa Business Enhanced
    H Reserved
    I Visa Infinite
    J Reserved
    J1 Reserved
    J2 Reserved
    J3 Visa Healthcare
    J4 Reserved
    K Visa Corporate T&E
    K1 Visa GSA Corporate T&E
    L Electron
    N Visa Platinium
    N1 TBA
    P Visa Gold
    Q Private Label
    Q1 Reserved
    R Proprietary
    S Visa Purchasing
    S1 Visa Purchasing
    S2 Visa Purchasing
    S3 Visa Purchasing
    S4 Government Services Loan
    S5 Commercial Transport EBT
    S6 Business Loan
    S7 Visa Distribution
    T Reserved
    U Visa TravelMoney
    V Visa VPay
    W Reserved
    X Reserved
    Y Reserved
    Z Reserved

    MASTERCARD
    MPN MASTERCARD PREPAID DEBIT STANDARD-INSURANCE
    MPO MASTERCARD PREPAID DEBIT STANDARD-OTHER
    MPP MASTERCARD PREPAID CARD
    MPR MASTERCARD PREPAID DEBIT STANDARD-TRAVEL
    MPT MASTERCARD PREPAID DEBIT STANDARD-TEEN
    MPV MASTERCARD PREPAID DEBIT STANDARD-VERNMENT
    MPW DEBIT MASTERCARD BUSINESS CARD PREPAID WORK B2B
    MPX MASTERCARD PREPAID DEBIT STANDARD-FLEX BENEFIT
    MPY MASTERCARD PREPAID DEB STANDARD-EMPLOYEE INCENTIVE
    MRG MASTERCARD PREPAID CARD
    MRH MASTERCARD UNKNOWN PRODUCT
    MRW PREPAID MASTERCARD BUSINESS CARD
    MSG PREPAID MAESTRO CONSUMER RELOADABLE CARD
    MSI MAESTRO CARD
    MWB WORLD MASTERCARD FOR BUSINESS CARD
    MWE WORLD ELITE MASTERCARD CARD
    DLS DEBIT MASTERCARD CARD-DELAYED DEBIT
    MCB MASTERCARD BUSINESSCARD CARD
    MCC MASTERCARD CREDIT CARD (MIXED BIN)
    MVOIR MASTERCARD FLEET CARD
    MCG LD MASTERCARD CARD
    MCO MASTERCARD CORPORATE CARD
    MCP MASTERCARD PURCHASING CARD
    MCS STANDARD MASTERCARD CARD
    MCW WORLD MASTERCARD CARD
    MDG LD DEBIT MASTERCARD CARD
    MDH WORLD DEBIT EMBOSSED MASTERCARD CARD
    MDP PLATINUM DEBIT MASTERCARD CARD
    MDS DEBIT MASTERCARD CARD
    MIU DEBIT MASTERCARD UNEMBOSSED
    MNW MASTERCARD WORLD CARD
    MOC MASTERCARD UNKNOWN PRODUCT
    MPG DEBIT MASTERCARD STANDARD PREPAID-GENERAL SPEND
    MPL PLATINUM MASTERCARD CARD
    MPP MASTERCARD PREPAID CARD
    MRG MASTERCARD PREPAID CARD
    MRO MASTERCARD REWARDS ONLY
    MRW PREPAID MASTERCARD BUSINESS CARD
    MSB MAESTRO SMALL BUSINESS CARD
    MSI MAESTRO CARD
    MSO MAESTRO PREPAID OTHER CARD
    MSW PREPAID MAESTRO CORPORATE CARD
    OLS MAESTRO-DELAYED DEBIT
    TCB MASTERCARD BUSINESS CARD-IMMEDIATE DEBIT
    TCC MASTERCARD (MIXED BIN)-IMMEDIATE DEBIT
    TCG LD MASTERCARD CARD-IMMEDIATE DEBIT
    TCS MASTERCARD STANDARD CARD-IMMEDIATE DEBIT
    TCW WORLD SIGNIA MASTERCARD CARD-IMMEDIATE DEBIT
    TNW MASTERCARD NEW WORLD-IMMEDIATE DEBIT
    TPL PLATINUM MASTERCARD-IMMEDIATE DEBIT
    WBE MASTERCARD UNKNOWN PRODUCT

    CB Désignation
    1 Carte nationale de retrait
    2 Carte nationale de retrait et de paiement
    3 Carte nationale de paiement
    4 Carte nationale de paiement et de retrait à autorisation systématique
    5 Carte nationale de paiement à autorisation systématique
    """
    'vads_bank_product': {
        'VISA': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'G1', 'G2', 'G3',
                 'H', 'I', 'J', 'J1', 'J2', 'J3', 'J4', 'K', 'K1', 'L',
                 'N', 'N1', 'P', 'Q', 'Q1', 'R', 'S', 'S1', 'S2', 'S3',
                 'S4', 'S5', 'S6', 'S7', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'MASTERCARD': ['MPN', 'MPO', 'MPP', 'MPR', 'MPT', 'MPV', 'MPW', 'MPX',
                       'MPY', 'MRG', 'MRH', 'MRW', 'MSG', 'MSI', 'MWB', 'MWE',
                       'DLS', 'MCB', 'MCC', 'MVOIR', 'MCG', 'MCO', 'MCP',
                       'MCS', 'MCW', 'MDG', 'MDH', 'MDP', 'MDS', 'MIU', 'MNW',
                       'MOC', 'MPG', 'MPL', 'MPP', 'MRG', 'MRO', 'MRW', 'MSB',
                       'MSI', 'MSO', 'MSW', 'OLS', 'TCB', 'TCC', 'TCG', 'TCS',
                       'TCW', 'TNW', 'TPL', 'WBE'],
        'CB': ['1', '2', '3', '4', '5'],
    },

    """Jour de naissance du porteur."""
    'vads_birth_day': 21,

    """Mois de naissance du porteur"""
    'vads_birth_month': 12,

    """Année de naissance du porteur."""
    'vads_birth_year': 1987,

    """Indique le délai en nombre de jours avant remise en banque.
    Si ce paramètre n’est pas transmis, alors la valeur par défaut définie dans
    le Back Office sera utilisée. Cette dernière est paramétrable dans le Back
    Office par toutes les personnes dûment habilitées."""
    'vads_capture_delay': 123,

    """Champ retourné dans la réponse.
    Moyen de paiement utilisé, si disponible (vide sinon).
    La valeur est issue des fichiers de plages de BIN.
    AMEX American Express
    AURORE-MULTI Carte Aurore (Multi enseigne)
    CB CB
    COFINOGA Cofinoga
    DINERS * Carte Diners Club
    E-CARTEBLEUE E-carte bleue
    E_CV E-chèque vacance
    JCB * Carte JCB
    MAESTRO Maestro
    MASTERCARD MasterCard
    ONEY Paiement en 3/4 fois Oney FacilyPay
    ONEY_SANDBOX Paiement en 3/4 fois Oney FacilyPay - Sandbox
    PAYPAL PayPal
    PAYPAL_SB PayPal - Sandbox
    V_ME V.me by Visa
    VISA Visa
    VISA_ELECTRON Visa Electron
    """
    'vads_card_brand': ['AMEX', 'AURORE-MULTI', 'CB', 'COFINOGA', 'DINERS *',
                        'E-CARTEBLEUE', 'E_CV', 'JCB *', 'MAESTRO',
                        'MASTERCARD', 'ONEY', 'ONEY_SANDBOX', 'PAYPAL',
                        'PAYPAL_SB', 'V_ME', 'VISA', 'VISA_ELECTRON'],

    """Champ retourné dans la réponse.
    Code pays de la carte utilisée pour le paiement à la norme ISO 3166"""
    'vads_card_country': [{"Name":"Afghanistan","Code":"AF"},{"Name":"Åland Islands","Code":"AX"},{"Name":"Albania","Code":"AL"},{"Name":"Algeria","Code":"DZ"},{"Name":"American Samoa","Code":"AS"},{"Name":"Andorra","Code":"AD"},{"Name":"Angola","Code":"AO"},{"Name":"Anguilla","Code":"AI"},{"Name":"Antarctica","Code":"AQ"},{"Name":"Antigua and Barbuda","Code":"AG"},{"Name":"Argentina","Code":"AR"},{"Name":"Armenia","Code":"AM"},{"Name":"Aruba","Code":"AW"},{"Name":"Australia","Code":"AU"},{"Name":"Austria","Code":"AT"},{"Name":"Azerbaijan","Code":"AZ"},{"Name":"Bahamas","Code":"BS"},{"Name":"Bahrain","Code":"BH"},{"Name":"Bangladesh","Code":"BD"},{"Name":"Barbados","Code":"BB"},{"Name":"Belarus","Code":"BY"},{"Name":"Belgium","Code":"BE"},{"Name":"Belize","Code":"BZ"},{"Name":"Benin","Code":"BJ"},{"Name":"Bermuda","Code":"BM"},{"Name":"Bhutan","Code":"BT"},{"Name":"Bolivia, Plurinational State of","Code":"BO"},{"Name":"Bonaire, Sint Eustatius and Saba","Code":"BQ"},{"Name":"Bosnia and Herzegovina","Code":"BA"},{"Name":"Botswana","Code":"BW"},{"Name":"Bouvet Island","Code":"BV"},{"Name":"Brazil","Code":"BR"},{"Name":"British Indian Ocean Territory","Code":"IO"},{"Name":"Brunei Darussalam","Code":"BN"},{"Name":"Bulgaria","Code":"BG"},{"Name":"Burkina Faso","Code":"BF"},{"Name":"Burundi","Code":"BI"},{"Name":"Cambodia","Code":"KH"},{"Name":"Cameroon","Code":"CM"},{"Name":"Canada","Code":"CA"},{"Name":"Cape Verde","Code":"CV"},{"Name":"Cayman Islands","Code":"KY"},{"Name":"Central African Republic","Code":"CF"},{"Name":"Chad","Code":"TD"},{"Name":"Chile","Code":"CL"},{"Name":"China","Code":"CN"},{"Name":"Christmas Island","Code":"CX"},{"Name":"Cocos (Keeling) Islands","Code":"CC"},{"Name":"Colombia","Code":"CO"},{"Name":"Comoros","Code":"KM"},{"Name":"Congo","Code":"CG"},{"Name":"Congo, the Democratic Republic of the","Code":"CD"},{"Name":"Cook Islands","Code":"CK"},{"Name":"Costa Rica","Code":"CR"},{"Name":"Côte d'Ivoire","Code":"CI"},{"Name":"Croatia","Code":"HR"},{"Name":"Cuba","Code":"CU"},{"Name":"Curaçao","Code":"CW"},{"Name":"Cyprus","Code":"CY"},{"Name":"Czech Republic","Code":"CZ"},{"Name":"Denmark","Code":"DK"},{"Name":"Djibouti","Code":"DJ"},{"Name":"Dominica","Code":"DM"},{"Name":"Dominican Republic","Code":"DO"},{"Name":"Ecuador","Code":"EC"},{"Name":"Egypt","Code":"EG"},{"Name":"El Salvador","Code":"SV"},{"Name":"Equatorial Guinea","Code":"GQ"},{"Name":"Eritrea","Code":"ER"},{"Name":"Estonia","Code":"EE"},{"Name":"Ethiopia","Code":"ET"},{"Name":"Falkland Islands (Malvinas)","Code":"FK"},{"Name":"Faroe Islands","Code":"FO"},{"Name":"Fiji","Code":"FJ"},{"Name":"Finland","Code":"FI"},{"Name":"France","Code":"FR"},{"Name":"French Guiana","Code":"GF"},{"Name":"French Polynesia","Code":"PF"},{"Name":"French Southern Territories","Code":"TF"},{"Name":"Gabon","Code":"GA"},{"Name":"Gambia","Code":"GM"},{"Name":"Georgia","Code":"GE"},{"Name":"Germany","Code":"DE"},{"Name":"Ghana","Code":"GH"},{"Name":"Gibraltar","Code":"GI"},{"Name":"Greece","Code":"GR"},{"Name":"Greenland","Code":"GL"},{"Name":"Grenada","Code":"GD"},{"Name":"Guadeloupe","Code":"GP"},{"Name":"Guam","Code":"GU"},{"Name":"Guatemala","Code":"GT"},{"Name":"Guernsey","Code":"GG"},{"Name":"Guinea","Code":"GN"},{"Name":"Guinea-Bissau","Code":"GW"},{"Name":"Guyana","Code":"GY"},{"Name":"Haiti","Code":"HT"},{"Name":"Heard Island and McDonald Islands","Code":"HM"},{"Name":"Holy See (Vatican City State)","Code":"VA"},{"Name":"Honduras","Code":"HN"},{"Name":"Hong Kong","Code":"HK"},{"Name":"Hungary","Code":"HU"},{"Name":"Iceland","Code":"IS"},{"Name":"India","Code":"IN"},{"Name":"Indonesia","Code":"ID"},{"Name":"Iran, Islamic Republic of","Code":"IR"},{"Name":"Iraq","Code":"IQ"},{"Name":"Ireland","Code":"IE"},{"Name":"Isle of Man","Code":"IM"},{"Name":"Israel","Code":"IL"},{"Name":"Italy","Code":"IT"},{"Name":"Jamaica","Code":"JM"},{"Name":"Japan","Code":"JP"},{"Name":"Jersey","Code":"JE"},{"Name":"Jordan","Code":"JO"},{"Name":"Kazakhstan","Code":"KZ"},{"Name":"Kenya","Code":"KE"},{"Name":"Kiribati","Code":"KI"},{"Name":"Korea, Democratic People's Republic of","Code":"KP"},{"Name":"Korea, Republic of","Code":"KR"},{"Name":"Kuwait","Code":"KW"},{"Name":"Kyrgyzstan","Code":"KG"},{"Name":"Lao People's Democratic Republic","Code":"LA"},{"Name":"Latvia","Code":"LV"},{"Name":"Lebanon","Code":"LB"},{"Name":"Lesotho","Code":"LS"},{"Name":"Liberia","Code":"LR"},{"Name":"Libya","Code":"LY"},{"Name":"Liechtenstein","Code":"LI"},{"Name":"Lithuania","Code":"LT"},{"Name":"Luxembourg","Code":"LU"},{"Name":"Macao","Code":"MO"},{"Name":"Macedonia, the Former Yugoslav Republic of","Code":"MK"},{"Name":"Madagascar","Code":"MG"},{"Name":"Malawi","Code":"MW"},{"Name":"Malaysia","Code":"MY"},{"Name":"Maldives","Code":"MV"},{"Name":"Mali","Code":"ML"},{"Name":"Malta","Code":"MT"},{"Name":"Marshall Islands","Code":"MH"},{"Name":"Martinique","Code":"MQ"},{"Name":"Mauritania","Code":"MR"},{"Name":"Mauritius","Code":"MU"},{"Name":"Mayotte","Code":"YT"},{"Name":"Mexico","Code":"MX"},{"Name":"Micronesia, Federated States of","Code":"FM"},{"Name":"Moldova, Republic of","Code":"MD"},{"Name":"Monaco","Code":"MC"},{"Name":"Mongolia","Code":"MN"},{"Name":"Montenegro","Code":"ME"},{"Name":"Montserrat","Code":"MS"},{"Name":"Morocco","Code":"MA"},{"Name":"Mozambique","Code":"MZ"},{"Name":"Myanmar","Code":"MM"},{"Name":"Namibia","Code":"NA"},{"Name":"Nauru","Code":"NR"},{"Name":"Nepal","Code":"NP"},{"Name":"Netherlands","Code":"NL"},{"Name":"New Caledonia","Code":"NC"},{"Name":"New Zealand","Code":"NZ"},{"Name":"Nicaragua","Code":"NI"},{"Name":"Niger","Code":"NE"},{"Name":"Nigeria","Code":"NG"},{"Name":"Niue","Code":"NU"},{"Name":"Norfolk Island","Code":"NF"},{"Name":"Northern Mariana Islands","Code":"MP"},{"Name":"Norway","Code":"NO"},{"Name":"Oman","Code":"OM"},{"Name":"Pakistan","Code":"PK"},{"Name":"Palau","Code":"PW"},{"Name":"Palestine, State of","Code":"PS"},{"Name":"Panama","Code":"PA"},{"Name":"Papua New Guinea","Code":"PG"},{"Name":"Paraguay","Code":"PY"},{"Name":"Peru","Code":"PE"},{"Name":"Philippines","Code":"PH"},{"Name":"Pitcairn","Code":"PN"},{"Name":"Poland","Code":"PL"},{"Name":"Portugal","Code":"PT"},{"Name":"Puerto Rico","Code":"PR"},{"Name":"Qatar","Code":"QA"},{"Name":"Réunion","Code":"RE"},{"Name":"Romania","Code":"RO"},{"Name":"Russian Federation","Code":"RU"},{"Name":"Rwanda","Code":"RW"},{"Name":"Saint Barthélemy","Code":"BL"},{"Name":"Saint Helena, Ascension and Tristan da Cunha","Code":"SH"},{"Name":"Saint Kitts and Nevis","Code":"KN"},{"Name":"Saint Lucia","Code":"LC"},{"Name":"Saint Martin (French part)","Code":"MF"},{"Name":"Saint Pierre and Miquelon","Code":"PM"},{"Name":"Saint Vincent and the Grenadines","Code":"VC"},{"Name":"Samoa","Code":"WS"},{"Name":"San Marino","Code":"SM"},{"Name":"Sao Tome and Principe","Code":"ST"},{"Name":"Saudi Arabia","Code":"SA"},{"Name":"Senegal","Code":"SN"},{"Name":"Serbia","Code":"RS"},{"Name":"Seychelles","Code":"SC"},{"Name":"Sierra Leone","Code":"SL"},{"Name":"Singapore","Code":"SG"},{"Name":"Sint Maarten (Dutch part)","Code":"SX"},{"Name":"Slovakia","Code":"SK"},{"Name":"Slovenia","Code":"SI"},{"Name":"Solomon Islands","Code":"SB"},{"Name":"Somalia","Code":"SO"},{"Name":"South Africa","Code":"ZA"},{"Name":"South Georgia and the South Sandwich Islands","Code":"GS"},{"Name":"South Sudan","Code":"SS"},{"Name":"Spain","Code":"ES"},{"Name":"Sri Lanka","Code":"LK"},{"Name":"Sudan","Code":"SD"},{"Name":"Suriname","Code":"SR"},{"Name":"Svalbard and Jan Mayen","Code":"SJ"},{"Name":"Swaziland","Code":"SZ"},{"Name":"Sweden","Code":"SE"},{"Name":"Switzerland","Code":"CH"},{"Name":"Syrian Arab Republic","Code":"SY"},{"Name":"Taiwan, Province of China","Code":"TW"},{"Name":"Tajikistan","Code":"TJ"},{"Name":"Tanzania, United Republic of","Code":"TZ"},{"Name":"Thailand","Code":"TH"},{"Name":"Timor-Leste","Code":"TL"},{"Name":"Togo","Code":"TG"},{"Name":"Tokelau","Code":"TK"},{"Name":"Tonga","Code":"TO"},{"Name":"Trinidad and Tobago","Code":"TT"},{"Name":"Tunisia","Code":"TN"},{"Name":"Turkey","Code":"TR"},{"Name":"Turkmenistan","Code":"TM"},{"Name":"Turks and Caicos Islands","Code":"TC"},{"Name":"Tuvalu","Code":"TV"},{"Name":"Uganda","Code":"UG"},{"Name":"Ukraine","Code":"UA"},{"Name":"United Arab Emirates","Code":"AE"},{"Name":"United Kingdom","Code":"GB"},{"Name":"United States","Code":"US"},{"Name":"United States Minor Outlying Islands","Code":"UM"},{"Name":"Uruguay","Code":"UY"},{"Name":"Uzbekistan","Code":"UZ"},{"Name":"Vanuatu","Code":"VU"},{"Name":"Venezuela, Bolivarian Republic of","Code":"VE"},{"Name":"Viet Nam","Code":"VN"},{"Name":"Virgin Islands, British","Code":"VG"},{"Name":"Virgin Islands, U.S.","Code":"VI"},{"Name":"Wallis and Futuna","Code":"WF"},{"Name":"Western Sahara","Code":"EH"},{"Name":"Yemen","Code":"YE"},{"Name":"Zambia","Code":"ZM"},{"Name":"Zimbabwe","Code":"ZW"}],

    """Dans la demande de paiement
    Numéro de carte en clair (cas du paiement silencieux).
    Dans la réponse
    • Numéro de carte masqué. Contient les 6 premiers chiffres du numéro,
    suivi par “XXXXXX” et enfin les 4 derniers numéros.
    • IBAN et BIC utilisés pour le paiement, séparés par un « _ » dans le cas
    d’un paiement par prélèvement."""
    'vads_card_number': 36 * '1',

    """Permet de spécifier, pour chaque réseau d’acceptation, le contrat
    commerçant à utiliser sous forme de liste.
    Format RESEAU1=contrat1;RESEAU2=contrat2;RESEAU3=contrat3
    AMEX American Express
    AURORE Réseau Cetelem Aurore (cartes Enseignes et carte Aurore
    universelle)
    CB réseau CB (Visa, Mastercard, CB, eCB, Maestro, Visa Electron)
    COFINOGA réseau Cofinoga (carte Be Smart et enseignes)
    DINERS * réseau Diners (carte Diners Club et Discover)
    E_CV réseau ANCV
    JCB * réseau JCB
    ONEY réseau Oney
    ONEY_SANDBOX réseau Oney - mode sandbox
    PAYPAL réseau PayPal
    PAYPAL_SB réseau PayPal - mode sandbox
    V_ME réseau V.me by Visa
    """
    'vads_contracts': ['AMEX', 'AURORE', 'CB', 'COFINOGA', 'DINERS *',
                       'E_CV', 'JCB *', 'ONEY', 'ONEY_SANDBOX', 'PAYPAL',
                       'PAYPAL_SB', 'V_ME'],

    """Champ retourné dans la réponse.
    Ce champ définit la valeur du contrat associé à la transaction.
    Il est valorisé par le contrat enregistré par défaut dans votre
    boutique ou prend la valeur du champ vads_contracts passé lors
    de la demande de paiement."""
    'vads_contract_used': 250 * 'X'

}
