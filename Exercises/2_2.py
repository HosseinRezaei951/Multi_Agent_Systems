import axelrod as axl

# Initialize players(strategies)
players = (axl.Defector(),
           axl.Adaptive(),
           axl.Alternator(),
           axl.FirstByDowning(),
           axl.DynamicTwoTitsForTat())

# Create and Run tournament between players
tournament = axl.Tournament(players= players, turns=10, repetitions=10)
results = tournament.play()

# Write tornoment results to CSV 
results.write_summary('results/2_2(tornoment_results).csv')

# Plot tornoment results
plot = axl.Plot(results)
plt = plot.winplot()
plt.show()

input("Finish")