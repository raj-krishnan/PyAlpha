"""
Contains lists of stocks in the S&P100 and S&P500.

NOTE
====
Some of the stocks have been commented out due to errors arising when
on attempting to procure their data using ystockquote.
ISSUE: https://github.com/cgoldberg/ystockquote/issues/43
"""

SNP100 = [
        "AAPL",   # Apple Inc.
        "ABBV",   # AbbVie Inc.
        "ABT",    # Abbott Laboratories
        "ACN",    # Accenture plc
        "AGN",    # Allergan plc
        "AIG",    # American International Group Inc.
        "ALL",    # Allstate Corp.
        "AMGN",   # Amgen Inc.
        "AMZN",   # Amazon.com
        "AXP",    # American Express Inc.
        "BA",     # Boeing Co.
        "BAC",    # Bank of America Corp
        "BIIB",   # Biogen Idec
        "BK",     # Bank of New York
        "BLK",    # BlackRock Inc
        "BMY",    # Bristol-Myers Squibb
        "BRK",    # Berkshire Hathaway
        "C",      # Citigroup Inc
        "CAT",    # Caterpillar Inc
        "CELG",   # Celgene Corp
        "CL",     # Colgate-Palmolive Co.
        "CMCSA",  # Comcast Corporation
        "COF",    # Capital One Financial Corp.
        "COP",    # ConocoPhillips
        "COST",   # Costco
        "CSCO",   # Cisco Systems
        "CVS",    # CVS Caremark
        "CVX",    # Chevron
        "DD",     # DuPont
        "DHR",    # Danaher
        "DIS",    # The Walt Disney Company
        "DOW",    # Dow Chemical
        "DUK",    # Duke Energy
        "EMC",    # EMC Corporation
        "EMR",    # Emerson Electric Co.
        "EXC",    # Exelon
        "F",      # Ford Motor
        "FB",     # Facebook
        "FDX",    # FedEx
        "FOX",    # Twenty-First Century Fox Inc
        "FOXA",   # Twenty-First Century Fox Inc
        "GD",     # General Dynamics
        "GE",     # General Electric Co.
        "GILD",   # Gilead Sciences
        "GM",     # General Motors
        "GOOG",   # Alphabet Inc
        "GOOGL",  # Alphabet Inc
        "GS",     # Goldman Sachs
        "HAL",    # Halliburton
        "HD",     # Home Depot
        "HON",    # Honeywell
        "IBM",    # International Business Machines
        "INTC",   # Intel Corporation
        "JNJ",    # Johnson & Johnson Inc
        "JPM",    # JP Morgan Chase & Co
        "KMI",    # Kinder Morgan Inc/DE
        "KO",     # The Coca-Cola Company
        "LLY",    # Eli Lilly and Company
        "LMT",    # Lockheed-Martin
        "LOW",    # Lowe's
        "MA",     # Mastercard Inc
        "MCD",    # McDonald's Corp
        "MDLZ",   # Mondelēz International
        "MDT",    # Medtronic Inc.
        "MET",    # Metlife Inc.
        "MMM",    # 3M Company
        "MO",     # Altria Group
        "MON",    # Monsanto
        "MRK",    # Merck & Co.
        "MS",     # Morgan Stanley
        "MSFT",   # Microsoft
        # "NEE",    # NextEra Energy                          YSTOCKQUOTE ERROR
        "NKE",    # Nike
        "ORCL",   # Oracle Corporation
        "OXY",    # Occidental Petroleum Corp.
        "PCLN",   # Priceline Group Inc/The
        "PEP",    # Pepsico Inc.
        "PFE",    # Pfizer Inc
        "PG",     # Procter & Gamble Co
        "PM",     # Phillip Morris International
        # "PYPL",   # PayPal Holdings                         YSTOCKQUOTE ERROR
        "QCOM",   # Qualcomm Inc.
        "RTN",    # Raytheon Company
        "SBUX",   # Starbucks Corporation
        "SLB",    # Schlumberger
        "SO",     # Southern Company
        "SPG",    # Simon Property Group, Inc.
        "T",      # AT&T Inc
        "TGT",    # Target Corp.
        "TWX",    # Time Warner Inc.
        "TXN",    # Texas Instruments
        "UNH",    # UnitedHealth Group Inc.
        "UNP",    # Union Pacific Corp.
        "UPS",    # United Parcel Service Inc
        "USB",    # US Bancorp
        "UTX",    # United Technologies Corp
        "V",      # Visa Inc.
        "VZ",     # Verizon Communications Inc
        "WBA",    # Walgreens Boots Alliance
        "WFC",    # Wells Fargo
        "WMT",    # Wal-Mart
        "XOM",    # Exxon Mobil Corp
]

SNP500 = [
        "MMM",    # 3M Company
        "ABT",    # Abbott Laboratories
        "ABBV",   # AbbVie
        "ACN",    # Accenture plc
        "ATVI",   # Activision Blizzard
        "AYI",    # Acuity Brands Inc
        "ADBE",   # Adobe Systems Inc
        "AAP",    # Advance Auto Parts
        "AES",    # AES Corp
        "AET",    # Aetna Inc
        "AFL",    # AFLAC Inc
        "AMG",    # Affiliated Managers Group Inc
        "A",      # Agilent Technologies Inc
        "APD",    # Air Products & Chemicals Inc
        "AKAM",   # Akamai Technologies Inc
        "ALK",    # Alaska Air Group Inc
        "ALB",    # Albemarle Corp
        "AGN",    # Allergan plc
        "LNT",    # Alliant Energy Corp
        "ALXN",   # Alexion Pharmaceuticals
        "ALLE",   # Allegion
        "ADS",    # Alliance Data Systems
        "ALL",    # Allstate Corp
        "GOOGL",  # Alphabet Inc Class A
        "GOOG",   # Alphabet Inc Class C
        "MO",     # Altria Group Inc
        "AMZN",   # Amazon.com Inc
        "AEE",    # Ameren Corp
        "AAL",    # American Airlines Group
        "AEP",    # American Electric Power
        "AXP",    # American Express Co
        "AIG",    # American International Group, Inc.
        "AMT",    # American Tower Corp A
        "AWK",    # American Water Works Company Inc
        "AMP",    # Ameriprise Financial
        "ABC",    # AmerisourceBergen Corp
        "AME",    # Ametek
        "AMGN",   # Amgen Inc
        "APH",    # Amphenol Corp A
        "APC",    # Anadarko Petroleum Corp
        "ADI",    # Analog Devices, Inc.
        "ANTM",   # Anthem Inc.
        "AON",    # Aon plc
        "APA",    # Apache Corporation
        "AIV",    # Apartment Investment & Mgmt
        "AAPL",   # Apple Inc.
        "AMAT",   # Applied Materials Inc
        "ADM",    # Archer-Daniels-Midland Co
        "ARNC",   # Arconic Inc
        "AJG",    # Arthur J. Gallagher & Co.
        "AIZ",    # Assurant Inc
        "T",      # AT&T Inc
        "ADSK",   # Autodesk Inc
        "ADP",    # Automatic Data Processing
        "AN",     # AutoNation Inc
        "AZO",    # AutoZone Inc
        "AVB",    # AvalonBay Communities, Inc.
        "AVY",    # Avery Dennison Corp
        "BHI",    # Baker Hughes Inc
        "BLL",    # Ball Corp
        "BAC",    # Bank of America Corp
        "BK",     # The Bank of New York Mellon Corp.
        "BCR",    # Bard (C.R.) Inc.
        "BAX",    # Baxter International Inc.
        "BBT",    # BB&T Corporation
        "BDX",    # Becton Dickinson
        "BBBY",   # Bed Bath & Beyond
        "BRK",    # Berkshire Hathaway
        "BBY",    # Best Buy Co. Inc.
        "BIIB",   # BIOGEN IDEC Inc.
        "BLK",    # BlackRock
        "HRB",    # Block H&R
        "BA",     # Boeing Company
        "BWA",    # BorgWarner
        "BXP",    # Boston Properties
        "BSX",    # Boston Scientific
        "BMY",    # Bristol-Myers Squibb
        "AVGO",   # Broadcom
        "BF-B",   # Brown-Forman Corporation
        "CHRW",   # C. H. Robinson Worldwide
        "CA",     # CA, Inc.
        "COG",    # Cabot Oil & Gas
        "CPB",    # Campbell Soup
        "COF",    # Capital One Financial
        "CAH",    # Cardinal Health Inc.
        "HSIC",   # Henry Schein
        "KMX",    # Carmax Inc
        "CCL",    # Carnival Corp.
        "CAT",    # Caterpillar Inc.
        "CBG",    # CBRE Group
        "CBS",    # CBS Corp.
        "CELG",   # Celgene Corp.
        "CNC",    # Centene Corporation
        "CNP",    # CenterPoint Energy
        "CTL",    # CenturyLink Inc
        "CERN",   # Cerner
        "CF",     # CF Industries Holdings Inc
        "SCHW",   # Charles Schwab Corporation
        "CHTR",   # Charter Communications
        "CHK",    # Chesapeake Energy
        "CVX",    # Chevron Corp.
        "CMG",    # Chipotle Mexican Grill
        "CB",     # Chubb Limited
        "CHD",    # Church & Dwight
        "CI",     # CIGNA Corp.
        "XEC",    # Cimarex Energy
        "CINF",   # Cincinnati Financial
        "CTAS",   # Cintas Corporation
        "CSCO",   # Cisco Systems
        "C",      # Citigroup Inc.
        "CFG",    # Citizens Financial Group
        "CTXS",   # Citrix Systems
        "CLX",    # The Clorox Company
        "CME",    # CME Group Inc.
        "CMS",    # CMS Energy
        "COH",    # Coach Inc.
        "KO",     # Coca Cola Company
        "CTSH",   # Cognizant Technology Solutions
        "CL",     # Colgate-Palmolive
        "CMCSA",  # Comcast A Corp
        "CMA",    # Comerica Inc.
        "CAG",    # ConAgra Foods Inc.
        "CXO",    # Concho Resources
        "COP",    # ConocoPhillips
        "ED",     # Consolidated Edison
        "STZ",    # Constellation Brands
        "GLW",    # Corning Inc.
        "COST",   # Costco Co.
        "COTY",   # Coty, Inc
        "CCI",    # Crown Castle International Corp.
        "CSRA",   # CSRA Inc.
        "CSX",    # CSX Corp.
        "CMI",    # Cummins Inc.
        "CVS",    # CVS Health
        "DHI",    # D. R. Horton
        "DHR",    # Danaher Corp.
        "DRI",    # Darden Restaurants
        "DVA",    # DaVita Inc.
        "DE",     # Deere & Co.
        "DLPH",   # Delphi Automotive
        "DAL",    # Delta Air Lines
        "XRAY",   # Dentsply Sirona
        "DVN",    # Devon Energy Corp.
        "DLR",    # Digital Realty Trust
        "DFS",    # Discover Financial Services
        "DISCA",  # Discovery Communications-A
        "DISCK",  # Discovery Communications-C
        "DG",     # Dollar General
        "DLTR",   # Dollar Tree
        "D",      # Dominion Resources
        "DOV",    # Dover Corp.
        "DOW",    # Dow Chemical
        "DPS",    # Dr Pepper Snapple Group
        "DTE",    # DTE Energy Co.
        "DD",     # Du Pont (E.I.)
        "DUK",    # Duke Energy
        "DNB",    # Dun & Bradstreet
        "ETFC",   # E*Trade
        "EMN",    # Eastman Chemical
        "ETN",    # Eaton Corporation
        "EBAY",   # eBay Inc.
        "ECL",    # Ecolab Inc.
        "EIX",    # Edison Int'l
        "EW",     # Edwards Lifesciences
        "EA",     # Electronic Arts
        "EMR",    # Emerson Electric Company
        "ENDP",   # Endo International
        "ETR",    # Entergy Corp.
        "EOG",    # EOG Resources
        "EQT",    # EQT Corporation
        "EFX",    # Equifax Inc.
        "EQIX",   # Equinix
        "EQR",    # Equity Residential
        "ESS",    # Essex Property Trust Inc
        "EL",     # Estee Lauder Cos.
        "ES",     # Eversource Energy
        "EXC",    # Exelon Corp.
        "EXPE",   # Expedia Inc.
        "EXPD",   # Expeditors Int'l
        "ESRX",   # Express Scripts
        "EXR",    # Extra Space Storage
        "XOM",    # Exxon Mobil Corp.
        "FFIV",   # F5 Networks
        "FB",     # Facebook
        "FAST",   # Fastenal Co
        "FRT",    # Federal Realty Investment Trust
        "FDX",    # FedEx Corporation
        "FIS",    # Fidelity National Information Services
        "FITB",   # Fifth Third Bancorp
        "FSLR",   # First Solar Inc
        "FE",     # FirstEnergy Corp
        "FISV",   # Fiserv Inc
        "FLIR",   # FLIR Systems
        "FLS",    # Flowserve Corporation
        "FLR",    # Fluor Corp.
        "FMC",    # FMC Corporation
        "FTI",    # FMC Technologies Inc.
        "FL",     # Foot Locker Inc
        "F",      # Ford Motor
        # "FTV",    # Fortive Corp                            YSTOCKQUOTE ERROR
        "FBHS",   # Fortune Brands Home & Security
        "BEN",    # Franklin Resources
        "FCX",    # Freeport-McMoran Cp & Gld
        "FTR",    # Frontier Communications
        "GPS",    # Gap (The)
        "GRMN",   # Garmin Ltd.
        "GD",     # General Dynamics
        "GE",     # General Electric
        "GGP",    # General Growth Properties Inc.
        "GIS",    # General Mills
        "GM",     # General Motors
        "GPC",    # Genuine Parts
        "GILD",   # Gilead Sciences
        "GPN",    # Global Payments Inc
        "GS",     # Goldman Sachs Group
        "GT",     # Goodyear Tire & Rubber
        "GWW",    # Grainger (W.W.) Inc.
        "HAL",    # Halliburton Co.
        "HBI",    # Hanesbrands Inc
        "HOG",    # Harley-Davidson
        "HAR",    # Harman Int'l Industries
        "HRS",    # Harris Corporation
        "HIG",    # Hartford Financial Svc.Gp.
        "HAS",    # Hasbro Inc.
        "HCA",    # HCA Holdings
        "HCP",    # HCP Inc.
        "HP",     # Helmerich & Payne
        "HES",    # Hess Corporation
        "HPE",    # Hewlett Packard Enterprise
        "HOLX",   # Hologic
        "HD",     # Home Depot
        "HON",    # Honeywell Int'l Inc.
        "HRL",    # Hormel Foods Corp.
        "HST",    # Host Hotels & Resorts
        "HPQ",    # HP Inc.
        "HUM",    # Humana Inc.
        "HBAN",   # Huntington Bancshares
        "ITW",    # Illinois Tool Works
        "ILMN",   # Illumina Inc
        "IR",     # Ingersoll-Rand PLC
        "INTC",   # Intel Corp.
        "ICE",    # Intercontinental Exchange
        "IBM",    # International Bus. Machines
        "IP",     # International Paper
        "IPG",    # Interpublic Group
        "IFF",    # Intl Flavors & Fragrances
        "INTU",   # Intuit Inc.
        "ISRG",   # Intuitive Surgical Inc.
        "IVZ",    # Invesco Ltd.
        "IRM",    # Iron Mountain Incorporated
        "JEC",    # Jacobs Engineering Group
        "JBHT",   # J. B. Hunt Transport Services
        "SJM",    # JM Smucker
        "JNJ",    # Johnson & Johnson
        "JCI",    # Johnson Controls International Plc
        "JPM",    # JPMorgan Chase & Co.
        "JNPR",   # Juniper Networks
        "KSU",    # Kansas City Southern
        "K",      # Kellogg Co.
        "KEY",    # KeyCorp
        "KMB",    # Kimberly-Clark
        "KIM",    # Kimco Realty
        "KMI",    # Kinder Morgan
        "KLAC",   # KLA-Tencor Corp.
        "KSS",    # Kohl's Corp.
        "KHC",    # Kraft Heinz Co
        "KR",     # Kroger Co.
        "LB",     # L Brands Inc.
        "LLL",    # L-3 Communications Holdings
        "LH",     # Laboratory Corp. of America Holding
        "LRCX",   # Lam Research
        "LM",     # Legg Mason
        "LEG",    # Leggett & Platt
        "LEN",    # Lennar Corp.
        "LVLT",   # Level 3 Communications
        "LUK",    # Leucadia National Corp.
        "LLY",    # Lilly (Eli) & Co.
        "LNC",    # Lincoln National
        "LLTC",   # Linear Technology Corp.
        "LKQ",    # LKQ Corporation
        "LMT",    # Lockheed Martin Corp.
        "L",      # Loews Corp.
        "LOW",    # Lowe's Cos.
        "LYB",    # LyondellBasell
        "MTB",    # M&T Bank Corp.
        "MAC",    # Macerich
        "M",      # Macy's Inc.
        "MNK",    # Mallinckrodt Plc
        "MRO",    # Marathon Oil Corp.
        "MPC",    # Marathon Petroleum
        "MAR",    # Marriott Int'l.
        "MMC",    # Marsh & McLennan
        "MLM",    # Martin Marietta Materials
        "MAS",    # Masco Corp.
        "MAS",    # Masco Corp.
        "MA",     # Mastercard Inc.
        "MAT",    # Mattel Inc.
        "MKC",    # McCormick & Co.
        "MCD",    # McDonald's Corp.
        "MCK",    # McKesson Corp.
        "MJN",    # Mead Johnson
        "MDT",    # Medtronic plc
        "MRK",    # Merck & Co.
        "MET",    # MetLife Inc.
        "MTD",    # Mettler Toledo
        "KORS",   # Michael Kors Holdings
        "MCHP",   # Microchip Technology
        "MU",     # Micron Technology
        "MSFT",   # Microsoft Corp.
        "MHK",    # Mohawk Industries
        "TAP",    # Molson Coors Brewing Company
        "MDLZ",   # Mondelez International
        "MON",    # Monsanto Co.
        "MNST",   # Monster Beverage
        "MCO",    # Moody's Corp
        "MS",     # Morgan Stanley
        "MOS",    # The Mosaic Company
        "MSI",    # Motorola Solutions Inc.
        "MUR",    # Murphy Oil
        "MYL",    # Mylan N.V.
        "NDAQ",   # NASDAQ OMX Group
        "NOV",    # National Oilwell Varco Inc.
        "NAVI",   # Navient
        "NTAP",   # NetApp
        "NFLX",   # Netflix Inc.
        "NWL",    # Newell Rubbermaid Co.
        "NFX",    # Newfield Exploration Co
        "NEM",    # Newmont Mining Corp. (Hldg. Co.)
        "NWSA",   # News Corp. Class A
        "NWS",    # News Corp. Class B
        # "NEE",    # NextEra Energy                          YSTOCKQUOTE ERROR
        "NLSN",   # Nielsen Holdings
        "NKE",    # Nike
        "NI",     # NiSource Inc.
        "NBL",    # Noble Energy Inc
        "JWN",    # Nordstrom
        "NSC",    # Norfolk Southern Corp.
        "NTRS",   # Northern Trust Corp.
        "NOC",    # Northrop Grumman Corp.
        "NRG",    # NRG Energy
        "NUE",    # Nucor Corp.
        "NVDA",   # Nvidia Corporation
        "ORLY",   # O'Reilly Automotive
        "OXY",    # Occidental Petroleum
        "OMC",    # Omnicom Group
        "OKE",    # ONEOK
        "ORCL",   # Oracle Corp.
        "OI",     # Owens-Illinois Inc
        "PCAR",   # PACCAR Inc.
        "PH",     # Parker-Hannifin
        "PDCO",   # Patterson Companies
        "PAYX",   # Paychex Inc.
        # "PYPL",   # PayPal                                  YSTOCKQUOTE ERROR
        "PNR",    # Pentair Ltd.
        "PBCT",   # People's United Financial
        "PEP",    # PepsiCo Inc.
        "PKI",    # PerkinElmer
        "PRGO",   # Perrigo
        "PFE",    # Pfizer Inc.
        "PCG",    # PG&E Corp.
        "PM",     # Philip Morris International
        "PSX",    # Phillips 66
        "PNW",    # Pinnacle West Capital
        "PXD",    # Pioneer Natural Resources
        "PBI",    # Pitney-Bowes
        "PNC",    # PNC Financial Services
        "RL",     # Polo Ralph Lauren Corp.
        "PPG",    # PPG Industries
        "PPL",    # PPL Corp.
        "PX",     # Praxair Inc.
        "PCLN",   # Priceline.com Inc
        "PFG",    # Principal Financial Group
        "PG",     # Procter & Gamble
        "PGR",    # Progressive Corp.
        "PLD",    # Prologis
        "PRU",    # Prudential Financial
        "PEG",    # Public Serv. Enterprise Inc.
        "PSA",    # Public Storage
        "PHM",    # Pulte Homes Inc.
        "PVH",    # PVH Corp.
        "QRVO",   # Qorvo
        "PWR",    # Quanta Services Inc.
        "QCOM",   # QUALCOMM Inc.
        "DGX",    # Quest Diagnostics
        "RRC",    # Range Resources Corp.
        "RTN",    # Raytheon Co.
        "O",      # Realty Income Corporation
        "RHT",    # Red Hat Inc.
        "REGN",   # Regeneron
        "RF",     # Regions Financial Corp.
        "RSG",    # Republic Services Inc
        "RAI",    # Reynolds American Inc.
        "RHI",    # Robert Half International
        "ROK",    # Rockwell Automation Inc.
        "COL",    # Rockwell Collins
        "ROP",    # Roper Industries
        "ROST",   # Ross Stores
        "RCL",    # Royal Caribbean Cruises Ltd
        "R",      # Ryder System
        "CRM",    # Salesforce.com
        "SCG",    # SCANA Corp
        "SLB",    # Schlumberger Ltd.
        "SNI",    # Scripps Networks Interactive Inc.
        "STX",    # Seagate Technology
        "SEE",    # Sealed Air
        "SRE",    # Sempra Energy
        "SHW",    # Sherwin-Williams
        "SIG",    # Signet Jewelers
        "SPG",    # Simon Property Group Inc
        "SWKS",   # Skyworks Solutions
        "SLG",    # SL Green Realty
        "SNA",    # Snap-On Inc.
        "SO",     # Southern Co.
        "LUV",    # Southwest Airlines
        "SWN",    # Southwestern Energy
        "SE",     # Spectra Energy Corp.
        "SPGI",   # S&P Global, Inc.
        "STJ",    # St Jude Medical
        "SWK",    # Stanley Black & Decker
        "SPLS",   # Staples Inc.
        "SBUX",   # Starbucks Corp.
        "STT",    # State Street Corp.
        "SRCL",   # Stericycle Inc
        "SYK",    # Stryker Corp.
        "STI",    # SunTrust Banks
        "SYMC",   # Symantec Corp.
        "SYF",    # Synchrony Financial
        "SYY",    # Sysco Corp.
        "TROW",   # T. Rowe Price Group
        "TGT",    # Target Corp.
        "TEL",    # TE Connectivity Ltd.
        "TGNA",   # Tegna
        "TDC",    # Teradata Corp.
        "TSO",    # Tesoro Petroleum Co.
        "TXN",    # Texas Instruments
        "TXT",    # Textron Inc.
        "COO",    # The Cooper Companies
        "HSY",    # The Hershey Company
        "TRV",    # The Travelers Companies Inc.
        "TMO",    # Thermo Fisher Scientific
        "TIF",    # Tiffany & Co.
        "TWX",    # Time Warner Inc.
        "TJX",    # TJX Companies Inc.
        "TMK",    # Torchmark Corp.
        "TSS",    # Total System Services
        "TSCO",   # Tractor Supply Company
        "TDG",    # TransDigm Group
        "RIG",    # Transocean
        "TRIP",   # TripAdvisor
        "FOXA",   # Twenty-First Century Fox Class A
        "FOX",    # Twenty-First Century Fox Class B
        "TSN",    # Tyson Foods
        "UDR",    # UDR Inc
        "ULTA",   # Ulta Salon Cosmetics & Fragrance Inc
        "USB",    # U.S. Bancorp
        "UA",     # Under Armour
        # "UA.C",   # Under Armour                            YSTOCKQUOTE ERROR
        "UNP",    # Union Pacific
        "UAL",    # United Continental Holdings
        "UNH",    # United Health Group Inc.
        "UPS",    # United Parcel Service
        "URI",    # United Rentals, Inc.
        "UTX",    # United Technologies
        "UHS",    # Universal Health Services, Inc.
        "UNM",    # Unum Group
        "URBN",   # Urban Outfitters
        "VFC",    # V.F. Corp.
        "VLO",    # Valero Energy
        "VAR",    # Varian Medical Systems
        "VTR",    # Ventas Inc
        "VRSN",   # Verisign Inc.
        "VRSK",   # Verisk Analytics
        "VZ",     # Verizon Communications
        "VRTX",   # Vertex Pharmaceuticals Inc
        "VIAB",   # Viacom Inc.
        "V",      # Visa Inc.
        "VNO",    # Vornado Realty Trust
        "VMC",    # Vulcan Materials
        "WMT",    # Wal-Mart Stores
        "WBA",    # Walgreens Boots Alliance
        "DIS",    # The Walt Disney Company
        "WM",     # Waste Management Inc.
        "WAT",    # Waters Corporation
        "WFC",    # Wells Fargo
        "HCN",    # Welltower Inc.
        "WDC",    # Western Digital
        "WU",     # Western Union Co
        "WRK",    # Westrock Co
        "WY",     # Weyerhaeuser Corp.
        "WHR",    # Whirlpool Corp.
        "WFM",    # Whole Foods Market
        "WMB",    # Williams Cos.
        # "WLTW",   # Willis Towers Watson                    YSTOCKQUOTE ERROR
        "WEC",    # Wisconsin Energy Corporation
        "WYN",    # Wyndham Worldwide
        "WYNN",   # Wynn Resorts Ltd
        "XEL",    # Xcel Energy Inc
        "XRX",    # Xerox Corp.
        "XLNX",   # Xilinx Inc
        "XL",     # XL Capital
        "XYL",    # Xylem Inc.
        "YHOO",   # Yahoo Inc.
        "YUM",    # Yum! Brands Inc
        "ZBH",    # Zimmer Biomet Holdings
        "ZION",   # Zions Bancorp
        "ZTS",    # Zoetis
]
