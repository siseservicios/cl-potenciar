Crear un archivo yaml en conf/ (donde esta odoo.conf) con la siguiente estructura

.. code-block:: yaml

    version: '1.0'
    databases:
        - database1: ['yxblue.potenciarsgr.com.ar', 'augusta.com.ar', 'quejodidosestostipos.com.ar']
        - testeo13: ['testeo13.potenciarsgr.com.ar']
        - ppooiiuu: ['ppoolol11.potenciarsgr.com.ar', 'miweb.com.ar' ]


poner el nombre del archivo en el parametro dbfilter del config
