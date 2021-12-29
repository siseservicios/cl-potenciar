# -----------------------------------------------------------------------------
#
#    Copyright (C) 2019  jeo Software  (http://www.jeosoft.com.ar)
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
    'name': 'Potenciar11',
    'version': '11.0.1.0.0',
    'license': 'Other OSI approved licence',
    'category': 'generico',
    'summary': 'Customization for Potenciar',
    "development_status": "Mature",
    'author': 'jeo Software',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',

        # minimum modules for argentinian localizacion + utilities + fixes
        'standard_depends_ce',

        # utilitarios adicionales
        'backend_theme_v11',
        'l10n_ar_account_withholding_fix',
        'account_financial_report',
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    'env-ver': '2',

    'git-repos': [
        'git@github.com:jobiols/cl-potenciar.git',

		# JEO
        'https://github.com/jobiols/odoo-addons jeo-odoo-addons',
        'https://github.com/jobiols/odoo-jeo-ce jeo-odoo-jeo-ce',

		# ADHOC
        'https://github.com/ingadhoc/odoo-argentina adhoc-odoo-argentina',
        'https://github.com/ingadhoc/argentina-sale adhoc-argentina-sale',
        'https://github.com/ingadhoc/account-financial-tools adhoc-account-financial-tools',
        'https://github.com/ingadhoc/account-payment adhoc-account-payment',
        'https://github.com/ingadhoc/miscellaneous adhoc-miscellaneous',
        'https://github.com/ingadhoc/argentina-reporting adhoc-argentina-reporting',
        'https://github.com/ingadhoc/reporting-engine adhoc-reporting-engine',
        'https://github.com/ingadhoc/aeroo_reports adhoc-aeroo_reports',
        'https://github.com/ingadhoc/sale adhoc-sale',
        'https://github.com/ingadhoc/odoo-support adhoc-odoo-support',
        'https://github.com/ingadhoc/product adhoc-product',
        'https://github.com/ingadhoc/stock adhoc-stock',
        'https://github.com/ingadhoc/account-invoicing adhoc-account-invoicing',
        'https://github.com/ingadhoc/patches adhoc-patches',

		# OCA
		'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting',
        'https://github.com/OCA/partner-contact oca-partner-contact',
        'https://github.com/OCA/web.git',
        'https://github.com/OCA/server-tools.git',
        'https://github.com/OCA/social.git',
        'https://github.com/OCA/server-ux.git',
        'https://github.com/OCA/server-brand.git',
        'https://github.com/OCA/manufacture.git',
        'https://github.com/OCA/manufacture-reporting.git',
        'https://github.com/OCA/management-system.git',
		'https://github.com/OCA/reporting-engine oca-reporting-engine',
        'https://github.com/OCA/sale-workflow.git',
        'https://github.com/OCA/stock-logistics-warehouse.git',
        'https://github.com/OCA/stock-logistics-reporting.git',
        'https://github.com/OCA/stock-logistics-workflow.git',
        'https://github.com/OCA/queue.git',
    ],

    'docker-images': [
        'odoo jobiols/odoo-jeo:11.0',
        'postgres postgres:11.1-alpine',
        'nginx nginx',
        'aeroo adhoc/aeroo-docs',
    ],
}
