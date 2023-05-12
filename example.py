from HPST.hpst import Experiment
from matplotlib import pyplot as plt

exp = Experiment.load("run.dat", "run.json")  # TODO Replace with actual filepaths
exp.t *= 1e3  # Convert to ms

plt.figure()

plt.title("Pressure")
for num, PCB in exp.PCB.items():
    plt.plot(exp.t, PCB.pressure / 1e5, alpha=0.8, label=f"PCB {num}")
    plt.legend()
if exp.kistler:
    plt.plot(exp.t, exp.kistler.pressure / 1e5, label="Kistler")

plt.xlabel("Time [ms]")
plt.ylabel("Pressure [bar]")

if exp.emission:
    plt.figure()
    plt.title("Emissions")
    for radical in exp.emission:
        plt.plot(exp.t, exp.emission[radical], alpha=0.8, label=radical)

    plt.legend()
    plt.xlabel("Time [ms]")
    plt.ylabel("Normalized Signal")

plt.show()
