class SolarSystem:

    def init(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def update(self):
        for body in self.bodies:
            body.update()

            


