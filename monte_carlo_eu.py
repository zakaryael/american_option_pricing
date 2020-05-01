
import project_option_pricing

class mc_eu(Option):
    def price(self, n):
        x = asset.simulate(n)
        y = self.payoff(x)
        return np.mean(y)

market = Market(0, 0.2, 1)
asset = Asset(market, 100)
option = mc_eu(asset, 90, is_put = False, is_american = True)


print("le prix blbalbjaljbal: ", option.price(100))  