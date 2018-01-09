class Gun:
    def __init__(self, new_model):
        """

        :param new_model: gun's model. Such as: AK47
        """
        self.model = new_model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count
        print("Bullet reload completed!")

    def shoot(self):
        self.bullet_count -= 1
        print("Gun shot")


class Soldier:
    def __init__(self, name, new_gun):
        self.name = name
        self.gun = new_gun

    def fire(self):
        if self.gun.bullet_count > 0:
            self.gun.shoot()
            print("Fire.....")
        else:
            print("Please load your bullet")

    def __str__(self):
        return "I am %s who is a soldier, I own a gun whose model is %s" % (self.name, self.gun.model)


gun = Gun("AK47")
gun.add_bullet(3)
xu_soldier = Soldier("Xusanduo", gun)
# print(xu_soldier)
xu_soldier.fire()
xu_soldier.fire()
xu_soldier.fire()
xu_soldier.fire()