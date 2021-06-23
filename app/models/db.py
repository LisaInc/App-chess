"""DB module."""


class DB:
    """Class with all the method use for the db."""

    table = None

    def serialized(self):
        raise NotImplementedError()

    @classmethod
    def deserialized(cls, serialized):
        raise NotImplementedError()

    def save(self):
        """Save to the db."""
        serialized = self.serialized()
        if self.id:
            self.table.update(serialized, doc_ids=[self.id])
        else:
            self.id = self.table.insert(serialized)

    @classmethod
    def get(cls, id):
        """Return the obj from the id."""
        obj_serialized = cls.table.get(doc_id=id)
        if not obj_serialized:
            print("Wrong id")
            return None
        obj_deserialized = cls.deserialized(obj_serialized)
        obj_deserialized.id = id
        return obj_deserialized

    @classmethod
    def all(cls):
        """Return all the obj in the db."""
        return [cls.deserialized(serialized) for serialized in cls.table.all()]
