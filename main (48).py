class Car:
  def __init__(self, make, model, sticker_price):
      self.make = make
      self.model = model
      self.sticker_price = sticker_price

  def discount_price(self):
      return self.sticker_price * 0.90

class Sport(Car):
  def __init__(self, make, model, sticker_price):
      super().__init__(make, model, sticker_price)
      self.sport_wheels = False
      self.sport_engine = False
      self.sport_interior = False

  def add_sport_wheels(self, include):
      self.sport_wheels = include == 'Y'

  def add_sport_engine(self, include):
      self.sport_engine = include == 'Y'

  def add_sport_interior(self, include):
      self.sport_interior = include == 'Y'

  def pricewithoptions(self):
      total_price = self.discount_price()
      if self.sport_wheels:
          total_price += 1000.00
      if self.sport_engine:
          total_price += 3000.00
      if self.sport_interior:
          total_price += 2000.00
      return total_price

# Testing the Sport class
sport_car = Sport("Tesla", "Model S", 70000)

# Adding options
sport_car.add_sport_wheels('Y')
sport_car.add_sport_engine('N')
sport_car.add_sport_interior('Y')

# Calculating price with options
price_with_options = sport_car.pricewithoptions()
print(f"Price for {sport_car.make} {sport_car.model} with options: ${price_with_options}")