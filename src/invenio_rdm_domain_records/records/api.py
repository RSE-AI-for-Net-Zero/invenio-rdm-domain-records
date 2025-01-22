from invenio_rdm_records.records.api import RDMDraft, RDMRecord
from invenio_records.systemfields import ConstantField

class DomainRDMDraft(RDMDraft):
    # Remember to update INDEXER_DEFAULT_INDEX in Invenio-App-RDM if you
    # update the JSONSchema and mappings to a new version.
    schema = ConstantField("$schema", "local://records/domain-record-v6.0.0.json")


class DomainRDMRecord(RDMRecord):
    # Remember to update INDEXER_DEFAULT_INDEX in Invenio-App-RDM if you
    # update the JSONSchema and mappings to a new version.
    schema = ConstantField("$schema", "local://records/domain-record-v6.0.0.json")

