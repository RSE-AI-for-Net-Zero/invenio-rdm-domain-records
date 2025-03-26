.. invenio-rdm-domain-records documentation master file, created by
   sphinx-quickstart on Wed Mar 26 09:40:42 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

invenio-rdm-domain-records
==========================

Extends *invenio-rdm-records*'s DataCite metadata model.

1. Adds a single, unpopulated, :code:`marshallow.fields.Dict` named *domain_metadata* to the schema that validates data as it comes off the wire. This validation would otherwise would fail if additional fields are present.
2. Extends the jsonschema used for validation at record creation - again with a subschema named *domain_metadata* containing only an external :code:`$ref` to `<local://domain/root.json>`_.  This referenced schema is the entry point for the extended data model (which is loaded into the app's local registry of jsonschemas by the :code:`invenio_jsonschemas.InvenioJSONSchemas` extension at app load time).
3. Similarly extends the Opensearch record index mapping, otherwise record indexing would fail.
4. Adds an error handler for :code:`jsonschema.exceptions.ValidationError` in the REST API application, so that useful jsonschema validation error details are returned to the client (with HTTP respose status 422) in case of validation failure.

  
**Important** - for this to work properly, at app load time the ``DomainInvenioRDMRecords`` **must be loaded in place of** ``InvenioRDMRecords``.  This is currently achieved by replacing the app factory functions in :code:`invenio_app.factory` with those in :code:`invenio_factory_patch.factory` (see `<https://github.ic.ac.uk/aeronautics/invenio-factory-patch.git>`_).


ext.py
^^^^^^
.. automodule:: invenio_rdm_domain_records.ext
   :members:

records/api.py
^^^^^^^^^^^^^^
.. automodule:: invenio_rdm_domain_records.records.api
   :members:
      



