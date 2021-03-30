class Sku:
    def __init__(self, sku_id, name, domain_id, description, **kwargs):
        self.sku_id = sku_id
        self.name = name
        self.domain_id = domain_id
        self.description = description
