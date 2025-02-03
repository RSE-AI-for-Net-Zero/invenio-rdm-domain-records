from invenio_rdm_records import InvenioRDMRecords
from invenio_rdm_records.services import (RDMRecordServiceConfig,
                                          RDMFileRecordServiceConfig,
                                          RDMFileDraftServiceConfig,
                                          RDMRecordCommunitiesConfig,
                                          RDMCommunityRecordsConfig,
                                          RDMRecordRequestsConfig)

from invenio_rdm_records.services.config import (RDMMediaFileRecordServiceConfig,
                                                 RDMRecordMediaFilesServiceConfig,
                                                 RDMMediaFileDraftServiceConfig)

from invenio_rdm_records.oaiserver.services.config import OAIPMHServerServiceConfig
    
from invenio_rdm_records.services.schemas import RDMRecordSchema
from invenio_rdm_records.services.schemas.metadata import MetadataSchema
from marshmallow.fields import Dict
from marshmallow_utils.fields import NestedAttribute

from flask import Blueprint
from flask_iiif import IIIF

from .records.api import DomainRDMDraft, DomainRDMRecord

class DomainMetadataSchema(MetadataSchema):
    domain_metadata = Dict()

class DomainRDMRecordSchema(RDMRecordSchema):
    metadata = NestedAttribute(DomainMetadataSchema)

class DomainRDMRecordServiceConfig(RDMRecordServiceConfig):
    schema = DomainRDMRecordSchema

class DomainInvenioRDMRecords(InvenioRDMRecords):
    '''
    blueprint = Blueprint(
        "invenio_rdm_records",
        __name__,
        template_folder="templates",
        static_folder="static",
    )
    '''
    def init_app(self, app):
        # RDMRecordServiceConfig picks up record & draft api class via these two config keys
        app.config["RDM_RECORD_CLS"] = DomainRDMRecord
        app.config["RDM_DRAFT_CLS"] = DomainRDMDraft
        
        super(DomainInvenioRDMRecords, self).init_app(app)

    def service_configs(self, app):
        class ServiceConfigs:
            record = DomainRDMRecordServiceConfig.build(app)
            record_with_media_files = RDMRecordMediaFilesServiceConfig.build(app)
            file = RDMFileRecordServiceConfig.build(app)
            file_draft = RDMFileDraftServiceConfig.build(app)
            media_file = RDMMediaFileRecordServiceConfig.build(app)
            media_file_draft = RDMMediaFileDraftServiceConfig.build(app)
            oaipmh_server = OAIPMHServerServiceConfig
            record_communities = RDMRecordCommunitiesConfig.build(app)
            community_records = RDMCommunityRecordsConfig.build(app)
            record_requests = RDMRecordRequestsConfig.build(app)

        return ServiceConfigs

   

        

