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
    'name': 'Potenciar131',
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
        'git@github.com:siseservicios/cl-potenciar.git -b 13.01',

        # WASF
        'git@github.com:siseservicios/wasf_addons.git -b 13.0',

	# JEO
        'https://github.com/jobiols/odoo-addons jeo-odoo-addons -b 13.0',
        'https://github.com/jobiols/odoo-jeo-ce jeo-odoo-jeo-ce -b 13.0',

        # REGABY
        'https://github.com/regaby/odoo-custom regaby-odoo-custom -b 13.0',

	# ADHOC
        'https://github.com/ingadhoc/odoo-argentina adhoc-odoo-argentina -b 13.0',
        'https://github.com/ingadhoc/odoo-argentina-ce adhoc-odoo-argentina-ce -b 13.0',
        'https://github.com/ingadhoc/argentina-sale adhoc-argentina-sale -b 13.0',
        'https://github.com/ingadhoc/account-financial-tools adhoc-account-financial-tools -b 13.0',
        'https://github.com/ingadhoc/account-payment adhoc-account-payment -b 13.0',
        'https://github.com/ingadhoc/miscellaneous adhoc-miscellaneous -b 13.0',
        'https://github.com/ingadhoc/argentina-reporting adhoc-argentina-reporting -b 13.0',
        'https://github.com/ingadhoc/reporting-engine adhoc-reporting-engine -b 13.0',
        'https://github.com/ingadhoc/aeroo_reports adhoc-aeroo_reports -b 13.0',
        'https://github.com/ingadhoc/sale adhoc-sale -b 13.0',
        'https://github.com/ingadhoc/product adhoc-product -b 13.0',
        'https://github.com/ingadhoc/stock adhoc-stock -b 13.0',
        'https://github.com/ingadhoc/account-invoicing adhoc-account-invoicing -b 13.0',
	'https://github.com/ingadhoc/website adhoc-website -b 13.0',

	# OCA '
	'https://github.com/OCA/community-data-files oca-community-data-files -b 13.0',
	'https://github.com/OCA/bank-payment oca-bank-payment -b 13.0',
	'https://github.com/OCA/edi oca-edi -b 13.0',
	'https://github.com/OCA/account-invoicing oca-account-invoicing -b 13.0',
	'https://github.com/OCA/account-fiscal-rule oca-account-fiscal-rule -b 13.0',
	'https://github.com/OCA/account-financial-tools oca-account-financial-tools -b 13.0',
	'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting -b 13.0',
	'https://github.com/OCA/bank-payment oca-bank-payment -b 13.0',
	'https://github.com/OCA/intrastat-extrastat oca-intrastat-extrastat -b 13.0',
        'https://github.com/OCA/manufacture oca-manufacture -b 13.0',
        'https://github.com/OCA/manufacture-reporting oca-manufacture-reporting -b 13.0',
        'https://github.com/OCA/management-system oca-management-system -b 13.0',
        'https://github.com/OCA/partner-contact oca-partner-contact -b 13.0',
	'https://github.com/OCA/pos oca-pos -b 13.0',
	'https://github.com/OCA/reporting-engine oca-reporting-engine -b 13.0',
        'https://github.com/OCA/queue oca-queue -b 13.0',
        'https://github.com/OCA/sale-workflow oca-sale-workflow -b 13.0',
        'https://github.com/OCA/server-tools oca-server-tools -b 13.0',
        'https://github.com/OCA/social oca-social -b 13.0',
        'https://github.com/OCA/server-ux oca-server-ux -b 13.0',
        'https://github.com/OCA/server-brand oca-server-brand -b 13.0',
        'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse -b 13.0',
        'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting -b 13.0',
        'https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow -b 13.0',
        'https://github.com/OCA/web oca-web -b 13.0',
        'https://github.com/OCA/event.git -b 13.0',

        # ODOO MATES
        'https://github.com/odoomates/odooapps odoomates-odooapps -b 13.0',

	# CTMIL - Moldeo
	'https://github.com/ctmil/payment_mercadopago ctmil/payment_mercadopago -b 13.0',

        # localizacion española
        'https://github.com/OCA/l10n-spain.git oca-l10n-spain -b 13.0',
    ],

    'docker-images': [
        'odoo jobiols/odoo-jeo:13.1',
        'postgres postgres:10.1-alpine',
        'nginx nginx',
    ],
}
