import axelrod as axl

# Initialize players(strategies)
players = (axl.Cooperator(),
           axl.Defector(),
           axl.Grudger(),
           axl.TitForTat(),
           axl.TitFor2Tats(),
           axl.SecondByTester(),
           axl.WinStayLoseShift())

# Create and Run tournament between players
tournament = axl.Tournament(players= players,  turns=10, repetitions=10)
results = tournament.play()

# Write tornoment results to CSV 
results.write_summary("results/2(tornoment_results).csv")

# Plot tornoment results
plot = axl.Plot(results)
plt = plot.winplot()
plt.show()

input("Finish")