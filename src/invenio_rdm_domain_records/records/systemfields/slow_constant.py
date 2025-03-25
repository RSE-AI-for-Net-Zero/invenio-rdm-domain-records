from invenio_records.systemfields import ConstantField

class SlowlyChangingConstantField(ConstantField):
    """
    Differs from invenio_records.systemfields.ConstantField in that
    the key's value is replaced at every call of the pre_init hook.
    """
    def pre_init(self, record, data, model=None, **kwargs):
        """Sets the key in the record during record instantiation.
        """
        if data is None:
        # A deleted record.
            return
        data[self.key] = self.value
            
