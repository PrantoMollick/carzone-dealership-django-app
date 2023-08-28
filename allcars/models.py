from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.


class Car(models.Model):

    state_choice = (
        ('Dhaka', 'Dhaka'),
        ('Chattogram', 'Chattogram'),
        ('Khulna', 'Khulna'),
        ('Rajshahi', 'Rajshahi'),
        ('Barishal', 'Barishal'),
        ('Sylhet', 'Sylhet'),
        ('Rangpur', 'Rangpur'),
        ('Mymensingh', 'Mymensingh'),
        ('Cox\'s Bazar', 'Cox\'s Bazar'),
        ('Jessore', 'Jessore'),
        ('Narayanganj', 'Narayanganj'),
        ('Gazipur', 'Gazipur'),
        ('Comilla', 'Comilla'),
        ('Bogra', 'Bogra'),
        ('Tangail', 'Tangail'),
        ('Dinajpur', 'Dinajpur'),
        ('Kushtia', 'Kushtia'),
        ('Brahmanbaria', 'Brahmanbaria'),
        ('Feni', 'Feni'),
        ('Jamalpur', 'Jamalpur'),
        ('Noakhali', 'Noakhali'),
        ('Pabna', 'Pabna'),
        ('Naogaon', 'Naogaon'),
        ('Sirajganj', 'Sirajganj'),
        ('Moulvibazar', 'Moulvibazar'),
        ('Satkhira', 'Satkhira'),
        ('Faridpur', 'Faridpur'),
        ('Lalmonirhat', 'Lalmonirhat'),
        ('Bagerhat', 'Bagerhat'),
        ('Pirojpur', 'Pirojpur'),
        ('Bhola', 'Bhola'),
        ('Chandpur', 'Chandpur'),
        ('Chuadanga', 'Chuadanga'),
        ('Habiganj', 'Habiganj'),
        ('Jhenaidah', 'Jhenaidah'),
        ('Khagrachari', 'Khagrachari'),
        ('Meherpur', 'Meherpur'),
        ('Munshiganj', 'Munshiganj'),
        ('Narail', 'Narail'),
        ('Lakshmipur', 'Lakshmipur'),
        ('Rangamati', 'Rangamati'),
        ('Netrokona', 'Netrokona'),
        ('Sherpur', 'Sherpur'),
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r, r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    CAR_FEATURES_CHOICES = (
        ('abs', 'Anti-lock Braking System (ABS)'),
        ('airbags', 'Airbags'),
        ('air_conditioning', 'Air Conditioning'),
        ('cruise_control', 'Cruise Control'),
        ('power_windows', 'Power Windows'),
        ('power_steering', 'Power Steering'),
        ('keyless_entry', 'Keyless Entry'),
        ('navigation_system', 'Navigation System'),
        ('bluetooth', 'Bluetooth Connectivity'),
        ('backup_camera', 'Backup Camera'),
        ('parking_sensors', 'Parking Sensors'),
        ('heated_seats', 'Heated Seats'),
        ('sunroof', 'Sunroof'),
        ('leather_seats', 'Leather Seats'),
        ('alloy_wheels', 'Alloy Wheels'),
        ('fog_lights', 'Fog Lights'),
        ('automatic_transmission', 'Automatic Transmission'),
        ('all_wheel_drive', 'All-Wheel Drive (AWD)'),
        ('four_wheel_drive', 'Four-Wheel Drive (4WD)'),
        ('convertible', 'Convertible'),
        ('electric_windows', 'Electric Windows'),
        ('cd_player', 'CD Player'),
        ('mp3_player', 'MP3 Player'),
        # Add more features as needed
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=CAR_FEATURES_CHOICES, max_length=300)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
