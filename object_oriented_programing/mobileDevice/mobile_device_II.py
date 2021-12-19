
class MobileDevice(object):
    """Describe a mobile device"""

    model = ''
    os = ''
    version = 0.0
    has_flash = False
    price = 0
    screen_width = 0.0
    screen_height = 0.0

    def __init__(self, model='', os='', version=0.0, has_flash=False, price=0, screen_width=0.0, screen_height=0.0):
        self.model, self.os, self.version, self.has_flash, self.price, self.screen_width, self.screen_height =\
            model, os, version, has_flash, price, screen_width, screen_height

    def print_parameters(self):
        print('Model { ' + self.model + ' = { Operating System: ' + self.os + ', Version: ' + str(self.version)
              + ', Has Flash: ' + str(self.has_flash) + ', Price: ' + str(self.price) + ' } }')

    def calculate_area(self):
        return self.screen_width * self.screen_height

    def picture_quality(self):
        print('Picture quality: ', end='')
        print('Good Quality') if self.has_flash else print('Bad Quality')

pass

mobile_device = MobileDevice('Samsung', 'Android', 10.3, True, 3200, 3.9, 6.2)
mobile_device.print_parameters()
print('mobile area:', mobile_device.calculate_area())
mobile_device.picture_quality()

