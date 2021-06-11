"""DB module."""


class DB:
    """Class with all the method use for the db."""

    @classmethod
    def save(self, obj):
        """Save to the db."""
        serialized = obj.serialized()
        if obj.id:
            obj.table.update(serialized, doc_ids=[obj.id])
        else:
            obj.id = obj.table.insert(serialized)

    @classmethod
    def get(self, class_use, id):
        """Return the obj from the id."""
        obj_serialized = class_use.table.get(doc_id=id)
        if not obj_serialized:
            return None
        obj_deserialized = class_use.deserialized(obj_serialized)
        obj_deserialized.id = id
        return obj_deserialized
