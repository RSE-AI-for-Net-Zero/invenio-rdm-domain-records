from invenio_rdm_records.records.api import RDMDraft, RDMRecord
from invenio_records.systemfields import ConstantField
from invenio_records_resources.records.systemfields import IndexField

from .systemfields import SlowlyChangingConstantField

def current_ae_schema_version():
    """
    return ae_datastore_schemas.__version__
    """
    pass

class DomainRDMDraft(RDMDraft):
    # Remember to update INDEXER_DEFAULT_INDEX in Invenio-App-RDM if you
    # update the JSONSchema and mappings to a new version.
    schema = ConstantField("$schema", "local://records/domain-record-v6.0.0.json")
    index = IndexField("rdmdomainrecords-drafts-draft-v6.0.0", search_alias="rdmdomainrecords-drafts")
    ae_schema_version = SlowlyChangingConstantField("ae_schema_version", current_ae_schema_version())

class DomainRDMRecord(RDMRecord):
    # Remember to update INDEXER_DEFAULT_INDEX in Invenio-App-RDM if you
    # update the JSONSchema and mappings to a new version.
    schema = ConstantField("$schema", "local://records/domain-record-v6.0.0.json")
    index = IndexField(
        "rdmdomainrecords-records-record-v6.0.0", search_alias="rdmdomainrecords-records"
    )
    ae_schema_version = SlowlyChangingConstantField("ae_schema_version", current_ae_schema_version())
