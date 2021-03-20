from models.Domain import Domain


class DomainRepository:
    def __init__(self):
        self.domains = [
            Domain("domain_1", 'Groceries'),
            Domain("domain_2", 'Services'),
            Domain("domain_3", 'Classifieds'),
        ]

    def get_domains(self):
        return self.domains
