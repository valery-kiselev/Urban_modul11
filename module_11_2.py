from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj)
    attr = [attrib for attrib in dir(obj) if not attrib.startswith('__')]
    obj_met = [method for method in dir(obj) if callable(getattr(obj, method))]
    obj_mod = obj.__class__.__module__
    itog = {'type': obj_type, 'attributes': attr, 'methods': obj_met,
         'module': obj_mod}
    return itog

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(self.name, self.number_of_floors)

h1 = House('ЖК Горский', 18)

pprint(introspection_info(h1))
