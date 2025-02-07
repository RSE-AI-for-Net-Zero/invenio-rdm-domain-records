from invenio_rdm_records.records.api import RDMDraft, RDMRecord
from invenio_records.systemfields import ConstantField
from invenio_records_resources.records.systemfields import IndexField

class DomainRDMDraft(RDMDraft):
    # Remember to update INDEXER_DEFAULT_INDEX in Invenio-App-RDM if you
    # update the JSONSchema and mappings to a new version.
    schema = ConstantField("$schema", "local://records/domain-record-v6.0.0.json")
    index = IndexField("rdmdomainrecords-drafts-draft-v6.0.0", search_alias="rdmdomainrecords-drafts")

class DomainRDMRecord(RDMRecord):
    # Remember to update INDEXER_DEFAULT_INDEX in Invenio-App-RDM if you
    # update the JSONSchema and mappings to a new version.
    schema = ConstantField("$schema", "local://records/domain-record-v6.0.0.json")
    index = IndexField(
        "rdmdomainrecords-records-record-v6.0.0", search_alias="rdmdomainrecords-records"
    )
        

