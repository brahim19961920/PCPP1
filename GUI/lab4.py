import tkinter as tk


class TrafficLights(tk.Tk):
    def __init__(self):
        super().__init__()

        self.phases = ((True, False, False), (True, True, False), (False, False, True), (False, True, False))
        self.phase_number = 0

        self.canvas = tk.Canvas(self, bg="grey", width=140, height=400)
        self.canvas.pack()

        self.add_lights()

        self.b1 = tk.Button(self, text="Next", command=self.add_lights)
        self.b1.pack()

        self.b2 = tk.Button(self, text="Quit", command=self.destroy)
        self.b2.pack()

    def add_lights(self):
        if self.phase_number == 4:
            self.phase_number = 0

        self.canvas.create_arc(
            20,
            20,
            120,
            120,
            outline="black",
            extent=359,
            style=tk.CHORD,
            width=5,
            fill="red" if self.phases[self.phase_number][0] else "grey",
        )
        self.canvas.create_arc(
            20,
            140,
            120,
            240,
            outline="black",
            extent=359,
            style=tk.CHORD,
            width=5,
            fill="yellow" if self.phases[self.phase_number][1] else "grey",
        )
        self.canvas.create_arc(
            20,
            260,
            120,
            360,
            outline="black",
            extent=359,
            style=tk.CHORD,
            width=5,
            fill="green" if self.phases[self.phase_number][2] else "grey",
        )

        self.phase_number += 1


if __name__ == "__main__":
    TrafficLights().mainloop()
