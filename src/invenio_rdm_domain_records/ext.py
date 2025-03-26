import types
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
import flask.json
from flask_iiif import IIIF


from .records.api import DomainRDMDraft, DomainRDMRecord

class DomainMetadataSchema(MetadataSchema):
    """
    Adds an empty :code:`marshmallow.fields.Dict` to
    :code:`invenio-rdm-records`'s existing metadata schema
    """
    domain_metadata = Dict()

class DomainRDMRecordSchema(RDMRecordSchema):
    """
    Overrides metadata class attribute of
    :code:`invenio_rdm_records.services.schemas.RDMRecordSchema`
    """
    metadata = NestedAttribute(DomainMetadataSchema)

class DomainRDMRecordServiceConfig(RDMRecordServiceConfig):
    """
    Overrides schema class attribute of
    :code:`invenio_rdm_records.services.RDMRecordServiceConfig`
    """

    schema = DomainRDMRecordSchema

class DomainInvenioRDMRecords(InvenioRDMRecords):
    """
    Sets draft and record API classes.  Sets :code:`RDMRecordService` config.
    """
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


def api_finalize_app(app):
    """
    Registered in :code:`invenio_base.api_finalize_app` entry
    point group.  Called in final stage of app loading.
    """
    init_api(app)
    

def init_api(app):
    """
    Registers an error handler for Invenio REST API application
    :code:`jsonschema.exceptions.ValidationError`

    Handler returns a ``422`` response with details of validation 
    error to the client.
    """
    from jsonschema.exceptions import ValidationError

    @app.errorhandler(ValidationError)
    def handle_jsonschema_validation_error(e):
        return str(e), 422
    
        

