# -----------------------------------------------------------------------------
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'Potenciar13',
    'version': '13.0.1.0.0',
    'license': 'Other OSI approved licence',
    'category': 'generico',
    'summary': 'Customization for Potenciar V13',
    "development_status": "Mature",
    'author': 'jeo Software',
    'depends': [
        # basic applications
	'accounting_pdf_reports',
	'l10n_ar_reports',
	'l10n_ar_account_withholding',
	'account_financial_report',
	'padron_afip',
	'l10n_ar_export_arba',
	'l10n_ar_export_sicore',
	'backend_theme_v13',


        # minimum modules for argentinian localizacion + utilities + fixes
        'standard_depends_ce',

        # utilitarios adicionales

    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,

    'env-ver': '2',

    'config': [
	'workers = 2',
	'max_cron_threads = 1'
    ],

    'git-repos': [
        'git@github.com:siseservicios/cl-potenciar.git',

	# JEO
        'https://github.com/jobiols/odoo-addons jeo-odoo-addons',
        'https://github.com/jobiols/odoo-jeo-ce jeo-odoo-jeo-ce',

        # REGABY
        'https://github.com/regaby/odoo-custom regaby-odoo-custom',

	# ADHOC
        'https://github.com/ingadhoc/odoo-argentina adhoc-odoo-argentina',
        'https://github.com/ingadhoc/odoo-argentina-ce adhoc-odoo-argentina-ce',
        'https://github.com/ingadhoc/argentina-sale adhoc-argentina-sale',
        'https://github.com/ingadhoc/account-financial-tools adhoc-account-financial-tools',
        'https://github.com/ingadhoc/account-payment adhoc-account-payment',
        'https://github.com/ingadhoc/miscellaneous adhoc-miscellaneous',
        'https://github.com/ingadhoc/argentina-reporting adhoc-argentina-reporting',
        'https://github.com/ingadhoc/reporting-engine adhoc-reporting-engine',
        'https://github.com/ingadhoc/aeroo_reports adhoc-aeroo_reports',
        'https://github.com/ingadhoc/sale adhoc-sale',
        'https://github.com/ingadhoc/product adhoc-product',
        'https://github.com/ingadhoc/stock adhoc-stock',
        'https://github.com/ingadhoc/account-invoicing adhoc-account-invoicing',
	'https://github.com/ingadhoc/website adhoc-website',

	# OCA
	'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting',
        'https://github.com/OCA/partner-contact oca-partner-contact',
        'https://github.com/OCA/web oca-web',
        'https://github.com/OCA/server-tools oca-server-tools',
        'https://github.com/OCA/social oca-social',
        'https://github.com/OCA/server-ux oca-server-ux',
        'https://github.com/OCA/server-brand oca-server-brand',
        'https://github.com/OCA/manufacture oca-manufacture',
        'https://github.com/OCA/manufacture-reporting oca-manufacture-reporting',
        'https://github.com/OCA/management-system oca-management-system',
	'https://github.com/OCA/reporting-engine oca-reporting-engine',
        'https://github.com/OCA/sale-workflow oca-sale-workflow',
        'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse',
        'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting',
        'https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow',
        'https://github.com/OCA/queue oca-queue',

        # ODOO MATES
        'https://github.com/odoomates/odooapps odoomates-odooapps',
	    
	# CTMIL - Moldeo
	'https://github.com/ctmil/payment_mercadopago ctmil-payment_mercadopago',
    ],

    'docker-images': [
        'odoo jobiols/odoo-jeo:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx',
    ],
}
