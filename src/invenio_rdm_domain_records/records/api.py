from invenio_rdm_records.records.api import RDMDraft, RDMRecord
from invenio_records.systemfields import ConstantField
from invenio_records_resources.records.systemfields import IndexField

class DomainRDMDraft(RDMDraft):
    """
    Overrides :code:`invenio_rdm_records.records.api.RDMDraft` schema and index class attributes
    """
    schema = ConstantField("$schema", "local://records/domain-record-v6.0.0.json")
    index = IndexField("rdmdomainrecords-drafts-draft-v6.0.0", search_alias="rdmdomainrecords-drafts")

class DomainRDMRecord(RDMRecord):
    """
    Overrides :code:`invenio_rdm_records.records.api.RDMRecord.schema` schema and index class attributes
    """
    schema = ConstantField("$schema", "local://records/domain-record-v6.0.0.json")
    index = IndexField(
        "rdmdomainrecords-records-record-v6.0.0", search_alias="rdmdomainrecords-records"
    )
        

