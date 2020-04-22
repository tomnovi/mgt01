import numpy as np

class RotationMatrix():

    def rotation(self, angle):
        self.sa = np.sin(angle[0])
        self.ca = np.cos(angle[0])
        self.sb = np.sin(angle[1])
        self.cb = np.cos(angle[1])
        self.sc = np.sin(angle[2])
        self.cc = np.cos(angle[2])

        # Define rotation matrix - Roll (Camber), Pitch (Caster) , Yaw (Toe)
        A = np.array([[1, 0, 0], [0, self.ca, self.sa], [0, -self.sa, self.ca]])
        B = np.array([[self.cb, 0, -self.sb], [0, 1, 0], [self.sb, 0, self.cb]])
        C = np.array([[self.cc, self.sc, 0], [-self.sc, self.cc, 0], [0, 0, 1]])

        # Collect rotation matrices in a dictionary
        R = {'A': A, 'B': B, 'C': C}
        return R

    def first_derivative(self):
        # Calculate first derivative
        # Define rotation matrix - Roll (Camber), Pitch (Caster) , Yaw (Toe)
        dA = np.array([[0, 0, 0], [0, -self.sa, self.ca], [0, -self.ca, -self.sa]])
        dB = np.array([[-self.sb, 0, -self.cb], [0, 0, 0], [self.cb, 0, -self.sb]])
        dC = np.array([[-self.sc, self.cc, 0], [-self.cc, -self.sc, 0], [0, 0, 0]])

        # Collect rotation matrices in a dictionary
        dR = {'dA': dA, 'dB': dB, 'dC': dC}
        return dR

    def second_derivative(self):
        # Calculate second derivative
        # Define rotation matrix - Roll (Camber), Pitch (Caster) , Yaw (Toe)
        d2A = np.array([[0, 0, 0], [0, -self.sa, self.ca], [0, -self.ca, -self.sa]])
        d2B = np.array([[-self.sb, 0, -self.cb], [0, 0, 0], [self.cb, 0, -self.sb]])
        d2C = np.array([[-self.sc, self.cc, 0], [-self.cc, -self.sc, 0], [0, 0, 0]])

        # Collect rotation matrices in a dictionary
        d2R = {'d2A': d2A, 'd2B': d2B, 'd2C': d2C}
