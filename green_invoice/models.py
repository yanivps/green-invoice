from .client import default as default_client, default_user_agent
from typing import TypedDict, List, Literal
import enum


class PaymentTerms(enum.IntEnum):
    IMMEDIATE = -1
    END_OF_MONTH = 0
    END_OF_MONTH_10 = 10
    END_OF_MONTH_15 = 15
    END_OF_MONTH_30 = 30
    END_OF_MONTH_45 = 45
    END_OF_MONTH_60 = 60
    END_OF_MONTH_75 = 75
    END_OF_MONTH_90 = 90
    END_OF_MONTH_120 = 120


class Category(enum.IntEnum):
    OTHER = 0
    INTERNET_AND_COMPUTERS = 1
    ACCOUNTING = 2
    ENGINEERING = 3
    MARKETING = 4
    LEISURE_AND_SPORTS = 5
    HEALTH_AND_MIND = 6
    AGRICULTURE = 7
    ART = 8
    EDUCATION = 9
    COMMUNICATION_AND_JOURNALISM = 10
    RELIGION = 11
    LAW = 12
    ARCHITECTURE_AND_DESIGN = 13
    FINANCE = 14
    TELEVISION_AND_STAGE = 15
    COUCHING_AND_CONSULTING = 16
    HOSTING_AND_CATERING = 17
    DELIVERY = 18
    REAL_ESTATE = 19
    ADMINSTRATION_AND_LOGISTCS = 21


class SubCategory(enum.IntEnum):
    OTHER = 0
    WEB_SOFTWARE = 101
    SOFTWARE_DEVELOPMENT = 102
    DIGITAL_MARKETING = 103
    HARDWARE = 104
    COMPUTER_TECHNICIAN = 105
    TECHNOLOGY_CONSULTANT = 106
    CPA = 201
    BOOKKEEPING = 202
    TAX_ADVISOR = 203
    ENGINEERING_AND_CONSTRUCTION = 301
    FOOD_ENGINEERING = 302
    ELECTRONIC_ENGINEERING = 303
    MECHANICAL_ENGINEERING = 304
    CIVIL_ENGINEERING = 305
    PHOTO = 401
    MARKETING_WRITING = 402
    MARKETING_CONSULTING = 403
    PRINTING_PRODUCTION = 404
    ADVERTISING_CONSULTING = 405
    GRAPHIC_DESIGN = 406
    SALES_AND_MARKETING = 407
    ILLUSTRATOR = 408
    FITNESS_TRAINING = 501
    CIRCLES = 502
    PILATES_AND_YOGA = 503
    DOCTOR = 601
    ALTERNATIVE_TREATMENT = 602
    MASSAGE = 603
    MENTAL_COUNSELING = 604
    PSYCHOLOGIST = 605
    AGRONOMIST = 701
    GARDENER = 702
    AGRICULTURAL = 703
    LITERATURE_POETRY_AND_PLAYS = 801
    DRAW = 802
    STREET_THEATER = 803
    MAGICIAN = 804
    CLOWN = 805
    TUTOR = 901
    LECTURER = 902
    KINDERGARTEN = 903
    MEETING = 904
    REPORTER = 1001
    PHOTOGRAPHER = 1002
    SAP = 1101
    MULTI = 1102
    KASHRUT_SUPERVISOR = 1103
    LAWYER = 1201
    ARCHITECTURE = 1301
    EXTERIOR_DESIGN = 1302
    ECONOMIST = 1401
    BANKER = 1402
    FINANCIAL_COUNSELING = 1403
    PRODUCTIONS = 1501
    MUSICIAN = 1502
    SINGER = 1503
    SOUND = 1504
    PLAYER = 1505
    SCRIPTER = 1506
    TV_AND_CINEMA = 1507
    COACH = 1601
    BUSINESS_CONSULTANT = 1602
    PERSONAL_CONSULTANT = 1603
    FAMILY_THERAPIST = 1604
    COUPLES_THERAPIST = 1605
    CATERING = 1701
    EVENT_PLANNER = 1702
    INTERNATIONAL_TRADE = 1801
    CUSTOMS_CLEARANCE = 1802
    SHIPPING = 1803
    MEDIATION = 1901
    REAL_ESTATE_CONSULTING = 1902
    APPRAISALS = 1903
    AIR_CONDITIONING = 2001
    PLUMBER = 2002
    ELECTRICIAN = 2003
    RENOVATOR = 2004
    CARPENTRY = 2005
    CONTRACTOR = 2006
    HOLDINGS_AND_SERVICES = 2007
    OFFICE_SERVICES = 2101
    DELIVERY = 2102


class IClientDraft(TypedDict, total=False):
    name: str
    active: bool
    department: str
    taxId: str
    accountingKey: str
    paymentTerms: PaymentTerms
    bankName: str
    bankBranch: str
    bankAccount: str
    send: bool
    address: str
    city: str
    zip: str
    country: str
    category: Category
    subCategory: SubCategory
    phone: str
    fax: str
    mobile: str
    remarks: str
    contactPerson: str
    emails: List[str]
    labels: List[str]


class IClient(IClientDraft, total=False):
    id: str
    creationDate: int
    lastUpdateDate: int
    incomeAmount: int
    paymentAmount: int
    balanceAmount: int


class IClientSearchFields(TypedDict, total=False):
    name: str
    active: bool
    email: str
    contactPerson: str
    labels: List[str]
    taxId: str
    page: int
    pageSize: int


class IClientSearchResultItem(TypedDict, total=False):
    id: str
    name: str
    active: bool
    taxId: str
    paymentTerms: int
    bankName: str
    bankBranch: str
    bankAccount: str
    country: str
    phone: str
    mobile: str
    contactPerson: str
    emails: list
    labels: list
    creationDate: int
    lastUpdateDate: int


class IClientSearchResult(TypedDict, total=False):
    total: int
    page: int
    pageSize: int
    pages: int
    items: List[IClientSearchResultItem]


class DocumentType(enum.IntEnum):
    PRICE_QUOTE = 10
    ORDER = 100
    DELIVERY_NOTE = 200
    RETURN_DELIVERY_NOTE = 210
    TRANSACTION_ACCOUNT = 300
    TAX_INVOICE = 305
    TAX_INVOICE_RECEIPT = 320
    REFUND = 330
    RECEIPT = 400
    RECEIPT_FOR_DONATION = 405
    PURCHASE_ORDER = 500
    RECEIPT_OF_A_DEPOSIT = 600
    WITHDRAWAL_OF_DEPOSIT = 610


class DocumentStatus(enum.IntEnum):
    OPENED_DOCUMENT = 0
    CLOSED_DOCUMENT = 1
    MANUALLY_MARKED_AS_CLOSED = 2
    CANCELING_OTHER_DOCUMENT = 3
    CANCELED_DOCUMENT = 4


class DocumentLanguage(str, enum.Enum):
    HEBREW = "he"
    ENGLISH = "en"


class Currency(str, enum.Enum):
    ILS = "ILS"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    CHF = "CHF"
    CNY = "CNY"
    AUD = "AUD"
    CAD = "CAD"
    RUB = "RUB"
    BRL = "BRL"
    HKD = "HKD"
    SGD = "SGD"
    THB = "THB"
    MXN = "MXN"
    TRY = "TRY"
    NZD = "NZD"
    SEK = "SEK"
    NOK = "NOK"
    DKK = "DKK"
    KRW = "KRW"
    INR = "INR"
    IDR = "IDR"
    PLN = "PLN"
    RON = "RON"
    ZAR = "ZAR"
    HRK = "HRK"


class DocumentVatType(enum.IntEnum):
    DEFAULT = 0  # (Based on business type)
    EXEMPT = 1  # (VAT free)
    MIXED = 2  # (Contains exempt and due VAT income rows)


class IncomeVatType(enum.IntEnum):
    DEFAULT = 0  # (VAT will be added based on the business type)
    INCLUDED = 1  # (VAT included in the price)
    EXEMPT = 2  # (VAT free)


class DiscountType(str, enum.Enum):
    SUM = "sum"
    PERCENTAGE = "percentage"


class DocumentLinkType(str, enum.Enum):
    LINK = "link"
    CANCEL = "cancel"


class PaymentDealType(enum.IntEnum):
    REGULAR = 1
    INSTALLMENTS = 2
    CREDIT = 3
    BILLING_DECLINED = 4
    OTHER = 5


class PaymentCardType(enum.IntEnum):
    UNKNOWN = 0
    ISRACARD = 1
    VISA = 2
    MASTERCARD = 3
    AMERICAN_EXPRESS = 4
    DINERS = 5


class PaymentType(enum.IntEnum):
    UNPAID = -1
    DEDUCTION_AT_SOURCE = 0
    CASH = 1
    CHECK = 2
    CREDIT_CARD = 3
    ELECTRONIC_FUND_TRANSFER = 4
    PAYPAL = 5
    PAYMENT_APP = 10
    OTHER = 11


class IDiscount(TypedDict, total=False):
    amount: float
    type: DiscountType


class IDocumentPayment(TypedDict, total=False):
    date: str
    type: PaymentType
    price: float
    currency: Currency
    currencyRate: float
    bankName: str
    bankBranch: str
    bankAccount: str
    chequeNum: str
    accountId: str
    transactionId: str
    cardType: PaymentCardType
    cardNum: str
    dealType: PaymentDealType
    numPayments: int  # credit card payments count
    firstPayment: int  # credit card first payment amount


class IDocumentIncome(TypedDict, total=False):
    catalogNum: str
    description: str
    quantity: int
    price: float
    currency: Currency
    currencyRate: float
    vatRate: float
    itemId: str
    vatType: IncomeVatType


class IDocumentClient(TypedDict, total=False):
    id: str
    name: str
    taxId: str
    department: str
    address: str
    city: str
    zip: str
    country: str
    phone: str
    fax: str
    mobile: str
    emails: List[str]
    add: bool
    self: bool


class BusinessType(enum.IntEnum):
    OSEK_MURSHE = 1
    LTD_COMPANY = 2
    OSEK_PATUR = 3
    NON_PROFIT_ORGANIZATION = 4
    PUBLIC_BENEFIT_COMPANY = 5
    PARTNERSHIP = 6


class IDocumentBusiness(TypedDict, total=False):
    type: BusinessType
    taxId: str
    name: str
    title: str
    address: str
    city: str
    zip: str
    phone: str
    fax: str
    mobile: str
    website: str
    email: str
    bankName: str
    bankBranch: str
    bankAccount: str
    bankSwift: str
    bankAba: str
    bankIban: str
    bankBeneficiary: str
    exemption: bool


class IDocumentDraft(TypedDict, total=False):
    description: str
    remarks: str
    footer: str
    emailContent: str
    type: DocumentType
    date: str
    dueDate: str
    lang: DocumentLanguage
    currency: Currency
    vatType: DocumentVatType
    discount: IDiscount
    rounding: bool
    signed: bool
    attachment: bool
    maxPayments: int
    client: IDocumentClient
    income: List[IDocumentIncome]
    payment: List[IDocumentPayment]
    linkedDocumentIds: List[str]
    linkedPaymentId: str
    linkType: DocumentLinkType


class IDocumentUrl(TypedDict, total=False):
    origin: str
    he: str
    en: str


class ICreatedDocument(TypedDict, total=False):
    id: str
    number: int
    signed: bool
    lang: DocumentLanguage
    url: IDocumentUrl


class IDocument(TypedDict, total=False):
    id: str
    description: str
    type: DocumentType
    number: str
    documentDate: str
    creationDate: int
    status: DocumentStatus
    lang: DocumentLanguage
    amountDueVat: float
    amountExemptVat: float
    amountExcludedVat: float
    amountLocal: float
    amountOpened: float
    vat: float
    amount: float
    currency: Currency
    currencyRate: float
    vatType: DocumentVatType
    income: List[IDocumentIncome]
    payment: List[IDocumentPayment]
    client: IDocumentClient
    business: IDocumentBusiness
    url: IDocumentUrl
    footer: str
    remarks: str
    rounding: bool
    ref: List[DocumentType]
    signed: bool
    cancellable: bool
    discount: IDiscount


class IDocumentSearchFields(TypedDict, total=False):
    page: int
    pageSize: int
    number: int
    type: List[DocumentType]
    status: List[DocumentStatus]
    paymentTypes: List[PaymentType]
    fromDate: str
    toDate: str
    clientId: str
    clientName: str
    description: str
    download: bool
    sort: Literal["documentDate", "creationDate"]


class IDocumentSearchResultItemIncome(IDocumentIncome, total=False):
    vat: float
    amount: float
    amountTotal: float


class IDocumentSearchResultItemPayment(TypedDict, total=False):
    name: str
    type: PaymentType
    price: float
    ref: List[DocumentType]
    cancellable: bool


class IDocumentSearchResultItemClient(TypedDict, total=False):
    id: str
    name: str
    emails: List[str]
    taxId: str
    self: bool


class IDocumentSearchResultItemBusiness(TypedDict, total=False):
    type: BusinessType
    exemption: bool


class IDocumentSearchResultItem(TypedDict, total=False):
    id: str
    description: str
    type: DocumentType
    number: str
    documentDate: str
    creationDate: int
    status: DocumentStatus
    lang: DocumentLanguage
    amountDueVat: float
    amountExemptVat: float
    amountExcludedVat: float
    amountLocal: float
    amountOpened: float
    vat: float
    amount: float
    currency: Currency
    currencyRate: float
    vatType: DocumentVatType
    income: List[IDocumentIncome]
    payment: List[IDocumentSearchResultItemPayment]
    client: IDocumentSearchResultItemClient
    business: IDocumentSearchResultItemBusiness
    url: IDocumentUrl


class IDocumentSearchResult(TypedDict, total=False):
    total: int
    page: int
    pageSize: int
    pages: int
    items: List[IDocumentSearchResultItem]
