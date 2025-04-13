from weasyprint import HTML
import os
from datetime import datetime
from django.conf import settings

# === TRANSLATION DICTIONARY ===
translations = { 
    'en': {
        'title': 'Credit Card Statement',
        'summary': 'Account Summary',
        'transactions': 'Transaction Details',
        'payment': 'Payment Summary',
        'rewards': 'Reward Points',
        'available_points': 'Available Points',
        'credit_usage': 'Credit Usage Summary',
        'footer': 'This is a computer-generated statement. No signature is required.',
        'customer_name': 'Customer Name',
        'card_number': 'Card Number',
        'statement_date': 'Statement Date',
        'current_balance': 'Current Balance',
        'previous_balance': 'Previous Balance',
        'payments_made': 'Payments Made',
        'new_purchases': 'New Purchases',
        'interest_charges': 'Interest Charges',
        'min_due': 'Minimum Payment Due',
        'total_due': 'Total Payment Due',
        'due_date': 'Payment Due Date',
        'credit_limit': 'Credit Limit',
        'available_credit': 'Available Credit',
        'cash_limit': 'Cash Limit',
        'available_cash': 'Available Cash',
        'date': 'Date',
        'merchant': 'Merchant',
        'amount': 'Amount',
        'type': 'Type',
    },
    'ta': {
        'title': 'கடன் அட்டை அறிக்கை',
        'summary': 'கணக்கு சுருக்கம்',
        'transactions': 'பரிவர்த்தனை விவரங்கள்',
        'payment': 'கட்டண சுருக்கம்',
        'rewards': 'வெகுமதி புள்ளிகள்',
        'available_points': 'கிடைக்கும் புள்ளிகள்',
        'credit_usage': 'கடன் பயன்பாடு சுருக்கம்',
        'footer': 'இது கணினி உருவாக்கிய அறிக்கை. கையொப்பம் தேவையில்லை.',
        'customer_name': 'வாடிக்கையாளர் பெயர்',
        'card_number': 'அட்டை எண்',
        'statement_date': 'அறிக்கையின் தேதி',
        'current_balance': 'தற்போதைய இருப்பு',
        'previous_balance': 'முந்தைய இருப்பு',
        'payments_made': 'கட்டணங்கள்',
        'new_purchases': 'புதிய வாங்கல்கள்',
        'interest_charges': 'வட்டிப் பணம்',
        'min_due': 'குறைந்தபட்ச கட்டணம்',
        'total_due': 'மொத்த கட்டணம்',
        'due_date': 'கட்டண நாளில்',
        'credit_limit': 'கடன் வரம்பு',
        'available_credit': 'பாவிக்கக்கூடிய கடன்',
        'cash_limit': 'பண வரம்பு',
        'available_cash': 'மீதமுள்ள பணம்',
        'date': 'தேதி',
        'merchant': 'வணிகர்',
        'amount': 'தொகை',
        'type': 'வகை',
    },
    'hi': {
        'title': 'क्रेडिट कार्ड विवरण',
        'summary': 'खाता सारांश',
        'transactions': 'लेन-देन विवरण',
        'payment': 'भुगतान सारांश',
        'rewards': 'इनाम अंक',
        'available_points': 'उपलब्ध अंक',
        'credit_usage': 'क्रेडिट उपयोग सारांश',
        'footer': 'यह एक कंप्यूटर जनित विवरण है। किसी हस्ताक्षर की आवश्यकता नहीं है।',
        'customer_name': 'ग्राहक नाम',
        'card_number': 'कार्ड नंबर',
        'statement_date': 'विवरण तिथि',
        'current_balance': 'वर्तमान शेष',
        'previous_balance': 'पिछला शेष',
        'payments_made': 'किए गए भुगतान',
        'new_purchases': 'नई खरीदारी',
        'interest_charges': 'ब्याज शुल्क',
        'min_due': 'न्यूनतम देय',
        'total_due': 'कुल देय',
        'due_date': 'देय तिथि',
        'credit_limit': 'क्रेडिट सीमा',
        'available_credit': 'उपलब्ध क्रेडिट',
        'cash_limit': 'नकद सीमा',
        'available_cash': 'उपलब्ध नकद',
        'date': 'तारीख',
        'merchant': 'व्यापारी',
        'amount': 'राशि',
        'type': 'प्रकार',
    },
    'ar': {
        'title': 'كشف حساب بطاقة الائتمان',
        'summary': 'ملخص الحساب',
        'transactions': 'تفاصيل المعاملات',
        'payment': 'ملخص الدفع',
        'rewards': 'نقاط المكافآت',
        'available_points': 'النقاط المتاحة',
        'credit_usage': 'ملخص الاستخدام الائتماني',
        'footer': 'هذا كشف حساب مُولد بواسطة الحاسوب. لا يتطلب توقيعاً.',
        'customer_name': 'اسم العميل',
        'card_number': 'رقم البطاقة',
        'statement_date': 'تاريخ البيان',
        'current_balance': 'الرصيد الحالي',
        'previous_balance': 'الرصيد السابق',
        'payments_made': 'المدفوعات',
        'new_purchases': 'المشتريات الجديدة',
        'interest_charges': 'الرسوم المالية',
        'min_due': 'الحد الأدنى للدفع',
        'total_due': 'إجمالي المبلغ المستحق',
        'due_date': 'تاريخ الاستحقاق',
        'credit_limit': 'حد الائتمان',
        'available_credit': 'الائتمان المتاح',
        'cash_limit': 'حد السحب النقدي',
        'available_cash': 'النقد المتاح',
        'date': 'التاريخ',
        'merchant': 'التاجر',
        'amount': 'المبلغ',
        'type': 'النوع',
    },
    'zh': {
    'title': '信用卡账单',
    'summary': '账户摘要',
    'transactions': '交易明细',
    'payment': '付款摘要',
    'rewards': '奖励积分',
    'available_points': '可用积分',
    'credit_usage': '信用额度使用情况',
    'footer': '这是计算机生成的账单，无需签名。',
    'customer_name': '客户姓名',
    'card_number': '卡号',
    'statement_date': '账单日期',
    'current_balance': '当前余额',
    'previous_balance': '上期余额',
    'payments_made': '已付款项',
    'new_purchases': '本期消费',
    'interest_charges': '利息费用',
    'min_due': '最低应还款额',
    'total_due': '总应还款额',
    'due_date': '还款截止日',
    'credit_limit': '信用额度',
    'available_credit': '可用信用额度',
    'cash_limit': '取现额度',
    'available_cash': '可用取现金额',
    'date': '日期',
    'merchant': '商户',
    'amount': '金额',
    'type': '类型',
    },
    'fr': {
    'title': 'Relevé de Carte de Crédit',
    'summary': 'Résumé du Compte',
    'transactions': 'Détails des Transactions',
    'payment': 'Résumé des Paiements',
    'rewards': 'Points de Récompense',
    'available_points': 'Points Disponibles',
    'credit_usage': 'Utilisation du Crédit',
    'footer': 'Ceci est un relevé généré par ordinateur. Aucune signature requise.',
    'customer_name': 'Nom du Client',
    'card_number': 'Numéro de Carte',
    'statement_date': 'Date du Relevé',
    'current_balance': 'Solde Actuel',
    'previous_balance': 'Solde Précédent',
    'payments_made': 'Paiements Effectués',
    'new_purchases': 'Nouveaux Achats',
    'interest_charges': 'Frais d\'intérêt',
    'min_due': 'Paiement Minimum',
    'total_due': 'Montant Total Dû',
    'due_date': 'Date d\'échéance',
    'credit_limit': 'Limite de Crédit',
    'available_credit': 'Crédit Disponible',
    'cash_limit': 'Limite d\'Avance de Fonds',
    'available_cash': 'Fonds Disponibles',
    'date': 'Date',
    'merchant': 'Commerçant',
    'amount': 'Montant',
    'type': 'Type',
    },
    'es': {
    'title': 'Estado de Cuenta de Tarjeta de Crédito',
    'summary': 'Resumen de la Cuenta',
    'transactions': 'Detalles de Transacciones',
    'payment': 'Resumen de Pagos',
    'rewards': 'Puntos de Recompensa',
    'available_points': 'Puntos Disponibles',
    'credit_usage': 'Uso del Crédito',
    'footer': 'Este es un estado generado por computadora. No requiere firma.',
    'customer_name': 'Nombre del Cliente',
    'card_number': 'Número de Tarjeta',
    'statement_date': 'Fecha del Estado',
    'current_balance': 'Saldo Actual',
    'previous_balance': 'Saldo Anterior',
    'payments_made': 'Pagos Realizados',
    'new_purchases': 'Nuevas Compras',
    'interest_charges': 'Cargos por Interés',
    'min_due': 'Pago Mínimo',
    'total_due': 'Total Adeudado',
    'due_date': 'Fecha de Vencimiento',
    'credit_limit': 'Límite de Crédito',
    'available_credit': 'Crédito Disponible',
    'cash_limit': 'Límite de Efectivo',
    'available_cash': 'Efectivo Disponible',
    'date': 'Fecha',
    'merchant': 'Comerciante',
    'amount': 'Cantidad',
    'type': 'Tipo',
    },
    'ms': {
    'title': 'Penyata Kad Kredit',
    'summary': 'Ringkasan Akaun',
    'transactions': 'Butiran Transaksi',
    'payment': 'Ringkasan Pembayaran',
    'rewards': 'Mata Ganjaran',
    'available_points': 'Mata Tersedia',
    'credit_usage': 'Penggunaan Kredit',
    'footer': 'Ini adalah penyata yang dijana oleh komputer. Tandatangan tidak diperlukan.',
    'customer_name': 'Nama Pelanggan',
    'card_number': 'Nombor Kad',
    'statement_date': 'Tarikh Penyata',
    'current_balance': 'Baki Semasa',
    'previous_balance': 'Baki Sebelumnya',
    'payments_made': 'Pembayaran Dibuat',
    'new_purchases': 'Pembelian Baru',
    'interest_charges': 'Caj Faedah',
    'min_due': 'Bayaran Minimum',
    'total_due': 'Jumlah Perlu Dibayar',
    'due_date': 'Tarikh Bayaran',
    'credit_limit': 'Had Kredit',
    'available_credit': 'Kredit Tersedia',
    'cash_limit': 'Had Tunai',
    'available_cash': 'Tunai Tersedia',
    'date': 'Tarikh',
    'merchant': 'Peniaga',
    'amount': 'Jumlah',
    'type': 'Jenis',
    },
    'ja': {
    'title': 'クレジットカード明細書',
    'summary': '口座概要',
    'transactions': '取引明細',
    'payment': '支払概要',
    'rewards': 'リワードポイント',
    'available_points': '利用可能ポイント',
    'credit_usage': 'クレジット利用状況',
    'footer': 'これはコンピューターによって生成された明細書です。署名は不要です。',
    'customer_name': '顧客名',
    'card_number': 'カード番号',
    'statement_date': '明細日',
    'current_balance': '現在残高',
    'previous_balance': '前回残高',
    'payments_made': '支払い済み',
    'new_purchases': '新規購入',
    'interest_charges': '利息',
    'min_due': '最低支払額',
    'total_due': '合計支払額',
    'due_date': '支払期日',
    'credit_limit': 'クレジット限度額',
    'available_credit': '利用可能クレジット',
    'cash_limit': '現金限度額',
    'available_cash': '利用可能現金',
    'date': '日付',
    'merchant': '加盟店',
    'amount': '金額',
    'type': 'タイプ',
    },
    'de': {
    'title': 'Kreditkartenabrechnung',
    'summary': 'Kontenübersicht',
    'transactions': 'Transaktionsdetails',
    'payment': 'Zahlungsübersicht',
    'rewards': 'Bonuspunkte',
    'available_points': 'Verfügbare Punkte',
    'credit_usage': 'Kreditnutzung',
    'footer': 'Dies ist ein computererstellter Auszug. Keine Unterschrift erforderlich.',
    'customer_name': 'Kundenname',
    'card_number': 'Kartennummer',
    'statement_date': 'Abrechnungsdatum',
    'current_balance': 'Aktueller Kontostand',
    'previous_balance': 'Vorheriger Kontostand',
    'payments_made': 'Geleistete Zahlungen',
    'new_purchases': 'Neue Einkäufe',
    'interest_charges': 'Zinsbelastungen',
    'min_due': 'Mindestzahlung',
    'total_due': 'Gesamtbetrag fällig',
    'due_date': 'Fälligkeitsdatum',
    'credit_limit': 'Kreditlimit',
    'available_credit': 'Verfügbarer Kredit',
    'cash_limit': 'Bargeldlimit',
    'available_cash': 'Verfügbares Bargeld',
    'date': 'Datum',
    'merchant': 'Händler',
    'amount': 'Betrag',
    'type': 'Typ',
    },
 }  

# === PDF GENERATION FUNCTION ===
def generate_pdf(customer, account, transactions, rewards, language='en'):
    # Fallback to English if language code is missing
    t = translations.get(language, translations['en'])

    # Handle RTL direction
    is_rtl = language == 'ar'
    text_direction = 'rtl' if is_rtl else 'ltr'
    text_align = 'right' if is_rtl else 'left'

    today = datetime.now().strftime('%d %B %Y')

    # Transaction rows
    tx_rows = ""
    for txn in transactions:
        tx_rows += f"""
        <tr>
            <td>{txn['TransactionDate']}</td>
            <td>{txn['MerchantName']}</td>
            <td style='text-align:right'>RM {txn['Amount']:.2f}</td>
            <td>{txn['TransactionType']}</td>
        </tr>
        """

    # HTML content
    html_string = f"""
    <html>
    <head>
        <meta charset='UTF-8'>
        <style>
            @page {{
                size: A4;
                margin: 40px;
                @bottom-center {{
                    content: "Public Bank Berhad (6463-H) | www.pbebank.com | Customer Care: 1-800-22-5555 | Email: customerservice@publicbank.com.my\\A {t['footer']}";
                    font-size: 10px;
                    color: #666;
                    white-space: pre;
                }}
            }}
            body {{
                font-family: 'Arial', sans-serif;
                direction: {text_direction};
                text-align: {text_align};
                color: #333;
                font-size: 12px;
                margin: 0;
            }}
            .header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 2px solid #ccc;
                padding-bottom: 10px;
            }}
            .header h1 {{ color: #007bff; }}
            .header .title {{ font-size: 15px; font-weight: bold; color: #007bff; }}
            .section-title {{
                background-color: #f1f1f1;
                padding: 8px;
                font-weight: bold;
                font-size: 14px;
                border-left: 5px solid #007bff;
                margin-top: 30px;
            }}
            .info p {{ margin: 4px 0; }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }}
            th, td {{ border: 1px solid #ddd; padding: 6px; }}
            th {{ background-color: #007bff; color: white; text-align: {text_align}; }}
        </style>
    </head>
    <body>

        <div class='header'>
            <h1>PUBLIC BANK</h1>
            <div class='title'>{t['title']}</div>
        </div>

        <div class='info'>
            <div class='section-title'>{t['summary']}</div>
            <p><strong>{t['customer_name']}:</strong> {customer['FirstName']} {customer['LastName']}</p>
            <p><strong>{t['card_number']}:</strong> {account['CardNumber']} ({account['CardType']})</p>
            <p><strong>{t['statement_date']}:</strong> {today}</p>
            <p><strong>{t['current_balance']}:</strong> RM {account['CurrentBalance']:.2f}</p>
        </div>

        <div class='section-title'>{t['payment']}</div>
        <table>
            <tr><td><strong>{t['previous_balance']}:</strong></td><td>RM {account.get('PreviousBalance', '0.00')}</td></tr>
            <tr><td><strong>{t['payments_made']}:</strong></td><td>RM {account.get('TotalPayment', '0.00')}</td></tr>
            <tr><td><strong>{t['new_purchases']}:</strong></td><td>RM {account.get('NewPurchases', '0.00')}</td></tr>
            <tr><td><strong>{t['interest_charges']}:</strong></td><td>RM {account.get('Interest', '0.00')}</td></tr>
            <tr><td><strong>{t['min_due']}:</strong></td><td>RM {account.get('MinDue', '0.00')}</td></tr>
            <tr><td><strong>{t['total_due']}:</strong></td><td>RM {account.get('TotalDue', '0.00')}</td></tr>
            <tr><td><strong>{t['due_date']}:</strong></td><td>{account.get('DueDate', 'N/A')}</td></tr>
        </table>

        <div class='section-title'>{t['credit_usage']}</div>
        <table>
            <tr><td><strong>{t['credit_limit']}:</strong></td><td>RM {account.get('CreditLimit', '0.00')}</td></tr>
            <tr><td><strong>{t['available_credit']}:</strong></td><td>RM {account.get('AvailableCredit', '0.00')}</td></tr>
            <tr><td><strong>{t['cash_limit']}:</strong></td><td>RM {account.get('CashLimit', '0.00')}</td></tr>
            <tr><td><strong>{t['available_cash']}:</strong></td><td>RM {account.get('AvailableCash', '0.00')}</td></tr>
        </table>

        <div class='section-title'>{t['transactions']}</div>
        <table>
            <thead>
                <tr>
                    <th>{t['date']}</th>
                    <th>{t['merchant']}</th>
                    <th>{t['amount']}</th>
                    <th>{t['type']}</th>
                </tr>
            </thead>
            <tbody>
                {tx_rows}
            </tbody>
        </table>
    """

    if rewards:
        html_string += f"""
        <div class='section-title'>{t['rewards']}</div>
        <p><strong>{t['available_points']}:</strong> {rewards['AvailablePoints']}</p>
        """

    html_string += "</body></html>"

    filename = f"statement_{account['CardNumber'].replace(' ', '')}_{datetime.now().strftime('%Y%m%d')}.pdf"
    media_path = os.path.join(settings.MEDIA_ROOT, filename)
    HTML(string=html_string, base_url=settings.BASE_DIR).write_pdf(media_path)

    return filename
