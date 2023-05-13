#!/usr/bin/env bash
#################################
# Generate the odoo README.rst documentacion for each module in
# the current repository.
# you must install this: pip install gen-odoo-readme

gen-readme \
    --org-name wasf \
    --repo-name cl-potenciar \
    --branch 13.0 \
    --addons-dir "$PWD"
