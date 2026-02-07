print((lambda x: next((n for n, r in zip(
        ["few", "several", "pack", "lots", "horde", "throng", "swarm", "zounds"],
        [5, 10, 20, 50, 100, 250, 500, 1000]
    ) if x < r
), "legion"))(int(input()))
)
