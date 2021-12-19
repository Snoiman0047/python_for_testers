
class MobileDevice(object):
    """Describe a mobile device"""

    model = ''
    os = ''
    version = 0.0
    has_flash = False
    price = 0

    def __init__(self, model='', os='', version=0.0, has_flash=False, price=0):
        self.model = model
        self.os = os
        self.version = version
        self.has_flash = has_flash
        self.price = price

    def print_parameters(self):
        print('Model { ' + self.model + ' = { Operating System: ' + self.os + ', Version: ' + str(self.version)
              + ', Has Flash: ' + str(self.has_flash) + ', Price: ' + str(self.price) + ' } }')
pass

mobile_device = MobileDevice('Samsung', 'Android', 10.3, True, 3200)
mobile_device.print_parameters()
